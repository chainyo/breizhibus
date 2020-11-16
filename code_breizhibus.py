import mysql.connector

# Connection à la bdd
class Bdd():

    def __init__(self) :
        self.config = {
        'user': 'dbadmin',
        'password': '150k60BRO',
        'host': 'localhost',
        'port': '3306',
        'database': 'projet_breizhibus',
        'raise_on_warnings': True,
        }
        self.link = mysql.connector.connect(**self.config)
        self.cursor = self.link.cursor()

    # Stockage des bus suivant la bdd
    def stock_bus(self):
        self.cursor.execute('''SELECT id_bus, numero, registration, num_place, bus.id_line, bus_lines.name FROM bus JOIN bus_lines ON bus.id_line = bus_lines.id_line ORDER BY numero''')
        self.rows = self.cursor.fetchall()
        self.dic_bus = {}
        for row in self.rows:
            self.dic_bus[row[0]] = (row[1], row[2], row[3], row[4], row[5])
        return self.dic_bus

    # Récupération des numeros de bus
    def recup_bus_num(self):
        self.cursor.execute('''SELECT numero FROM bus ORDER BY numero''')
        self.bus_num = self.cursor.fetchall()
        self.num_li = []
        for v in self.bus_num:
            self.num_li.append(v[0])
        return self.num_li

    # Création des bus suivant la bdd
    def create_bus(self, dic):
        for val in dic.values():
            bus = Bus(val[0], val[1], val[2])

    # Stockage des lignes de bus suivant la bdd
    def stock_bus_lines(self):
        self.cursor.execute('''SELECT name FROM bus_lines''')
        self.rows = self.cursor.fetchall()
        self.dic_bus_lines = {}
        for i, row in enumerate(self.rows, 0):
            self.dic_bus_lines[i] = f'{row[0]}'
        return self.dic_bus_lines
    
    def close(self):
        self.link.close()
        self.cursor.close()

    def commit(self):
        self.link.commit()

# Classe Bus permettant de créer des bus pour la compagnie
# Fonctions actuelles : assigner une ligne au bus
class Bus():

    def __init__(self, num, reg, seats):
        self.num = num
        self.regist = reg
        self.seats = seats
        self.line_id = 0
    
    def __str__(self):
        if self.line_id == 0 :
            return f"Je suis le bus {self.num}, immatriculé {self.regist}, je peux transporter {self.seats} personnes et je n'ai pas encore été attribué à une ligne."
        else :
            return f"Je suis le bus {self.num}, immatriculé {self.regist}, je peux transporter {self.seats} personnes et j'ai été assigné sur la ligne {self.line_id}"

    # Assigner une ligne de bus à un bus en particulier
    def assign_line(self, line_id, line_name):
        self.line_id = line_id
        self.line_name = line_name
        print(f"Le bus {self.num} a été assigné sur la ligne {self.line_name}")

class BusLine():

    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Ligne {self.name} sélectionnée."

    def show_own_stops(self, cur):
        self.stops = ()
        cur.execute(f'''SELECT stops_lines.id_line, stops_lines.id_stop, bus_lines.name, stops.name FROM stops_lines JOIN bus_lines ON stops_lines.id_line = bus_lines.id_line JOIN stops ON stops_lines.id_stop = stops.id_stop WHERE bus_lines.name="{self.name}"''')
        rows = cur.fetchall()
        ref = set()
        for row in rows:
            ref.add(row[3])
        show_str = ''
        for i in ref:
            show_str += f'{i}\n'
        return show_str