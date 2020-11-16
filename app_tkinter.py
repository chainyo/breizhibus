import tkinter as tk
from tkinter import ttk, Label, Entry, Frame, Button, Radiobutton, YES, FLAT, BOTTOM, messagebox, PhotoImage
from code_breizhibus import Bdd, Bus, BusLine
import re
import fontawesome as fa


class Page():

    def __init__(self):
        self.container = Frame(app_frame, bg=colors["BG"])
    
    # Méthode pour cacher la frame
    def close_frame(self):
        self.container.pack_forget()

    # Méthode pour montrer la frame
    def show_frame(self):
        self.container.pack(expand=YES)

class MainPage(Page):

    def __init__(self):
        super().__init__()
        # Les différentes frames
        self.title = Frame(self.container, bg=colors["BG"])
        self.btn = Frame(self.container, bg=colors["BG"])
        # Les deux titres
        self.app_title = Label(self.title, text='BREIZHIBUS MANAGER', font=('Helvetica', 40), bg=colors["BG"], fg=colors["FG"]).pack(expand=YES, pady=8)
        self.app_subtitle = Label(self.title, text='Bienvenue sur votre interface. Que voulez-vous faire ?', font=('Helvetica', 14), bg=colors["BG"], fg=colors["FG"]).pack(expand=YES)
        # Les deux boutons
        self.btn_show_stops = Button(self.btn, text='Voir Lignes', bg=colors["FG"], fg=colors["Noir"], height=1, width=12, relief=FLAT, command=lambda:[self.close_frame(), page_stops.show_frame()]).pack(pady=10)
        self.btn_add_bus = Button(self.btn, text='Voir Bus', bg=colors["FG"], fg=colors["Noir"], height=1, width=12, relief=FLAT, command=lambda:[self.close_frame(), page_bus.show_frame()]).pack()
        # Affichage des frames
        self.title.pack(expand=YES, pady=25)
        self.btn.pack(expand=YES)

class StopsPage(Page):

    def __init__(self):
        super().__init__()
        # Les différentes frames
        self.btn = Frame(self.container, bg=colors["BG"])
        self.stops = Frame(self.container, bg=colors["FG"])
        self.btn_home_frame = Frame(self.container, bg=colors["BG"])
        # Récupération des lignes
        self.lines = bdd.stock_bus_lines()
        # Affichage des buttons liés aux lignes
        for v in self.lines.values():
            self.btn_line = Button(self.btn, text=f'{v}', bg=colors[v], fg=colors["FG"], relief=FLAT, command=lambda v=v : self.show_lines(v, bdd.cursor, self.stops)).pack(side=tk.LEFT)
        # Bouton Home
        self.btn_home = Button(self.btn_home_frame, image=homebtn, bg=colors["FG"], fg=colors["Noir"], relief=FLAT, height=20, width=20, command=lambda:[self.close_frame(),self.clean(self.stops), page_main.show_frame()]).pack(side=BOTTOM, padx=30)
        # Affichage des frames
        self.btn.pack(expand=YES, pady=25)
        self.stops.pack(expand=YES, pady=50)
        self.btn_home_frame.pack(expand=YES)

    # Méthode pour affichage des arrêts d'une ligne
    def show_lines(self, name, cur, frame):
        self.x = BusLine(name)
        self.txt = self.x.show_own_stops(cur)
        self.clean(frame)
        self.tit = Label(frame, text=f"Ligne {name}", font=('Helvetica', 20), bg=colors["FG"], fg=colors[name]).pack(expand=YES, pady=10, padx=5)
        self.show_label = Label(frame, text=self.txt, font=('Helvetica', 15), bg=colors["FG"], fg=colors["Noir"]).pack(expand=YES)

    # Nettoyage du cadre d'affichage des arrêts
    def clean(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

class BusPage(Page):

    def __init__(self):
        super().__init__()
        # Les différentes frames
        self.bus_frame = Frame(self.container, bg=colors["FG"])
        self.btn_frame = Frame(self.container, bg=colors["BG"])
        # Récupération des Bus
        self.recup_bus()
        # Boutons
        self.btn_add = Button(self.btn_frame, image=addbtn, bg=colors["FG"], relief=FLAT, height=20, width=20, command=lambda:[self.close_frame(),page_add_bus.clear_entry(), page_add_bus.show_frame()]).grid(column=0, row=0, padx=5)
        self.btn_home = Button(self.btn_frame, image=homebtn, bg=colors["FG"], relief=FLAT, height=20, width=20, command=lambda:[self.close_frame(), page_main.show_frame()]).grid(column=1, row=0)
        # Affichage des frames
        self.bus_frame.pack(expand=YES, pady=25)
        self.btn_frame.pack(expand=YES)
    
    def recup_bus(self):
        # Affichage du titre
        self.tab_title = Label(self.bus_frame, text='BUS DE BREIZHIBUS', font=('Helvetica', 20), bg=colors["FG"], fg=colors['Noir']).grid(row=0, columnspan=6, pady=5)
        # Récupération des lignes
        self.buss = bdd.stock_bus()
        # Affichage des buttons liés aux lignes
        for i, v in enumerate(self.buss.values(), 1):
            self.show_bus = Bus(v[0], v[1], v[2])
            self.show_bus.assign_line(v[3], v[4])
            self.numero = Label(self.bus_frame, text=self.show_bus.num, font=('Helvetica', 12), bg=colors["FG"], fg=colors['Noir'])
            self.numero.grid(column=0, row=i, padx=15)
            self.registration = Label(self.bus_frame, text=self.show_bus.regist, font=('Helvetica', 12), bg=colors["FG"], fg=colors['Noir'])
            self.registration.grid(column=1, row=i, padx=15)
            self.num_place = Label(self.bus_frame, text=self.show_bus.seats, font=('Helvetica', 12), bg=colors["FG"], fg=colors['Noir'])
            self.num_place.grid(column=2, row=i, padx=15)
            self.ligne = Label(self.bus_frame, text=self.show_bus.line_name, font=('Helvetica', 12), bg=colors["FG"], fg=colors["Noir"])
            self.ligne.grid(column=3, row=i, padx=15)
            self.edit_btn = Button(self.bus_frame, image=editbtn, relief=FLAT, bg=colors["Orange"], height=15, width=15, command=lambda b=self.show_bus:self.edit_bus(b))
            self.edit_btn.grid(column=4, row=i, padx=5)
            self.del_btn = Button(self.bus_frame, image=deletebtn, relief=FLAT, bg=colors["Rouge"], height=15, width=15, command=lambda b=self.show_bus:self.delete_bus(b))
            self.del_btn.grid(column=5, row=i, padx=5)

    def update(self):
        for widget in self.bus_frame.winfo_children():
            widget.destroy()
        self.recup_bus()
    
    def edit_bus(self, bus):
        page_bus.close_frame()
        page_add_bus.clear_entry()
        page_add_bus.input_numero.insert(0, bus.num)
        page_add_bus.input_regist.insert(0, bus.regist)
        page_add_bus.input_seats.insert(0, bus.seats)
        page_add_bus.input_line.insert(0, bus.line_name)
        page_add_bus.show_frame()

    def delete_bus(self, bus):
        bdd.cursor.execute(f'''DELETE FROM bus WHERE numero = "{bus.num}"''')
        bdd.commit()
        page_bus.update()

class BusAddPage(Page):

    def __init__(self):
        super().__init__()
        # Les différentes frames
        self.inputs_frame = Frame(self.container, bg=colors["BG"])
        self.btn_frame = Frame(self.container, bg=colors["BG"])
        # Label et Inputs
        self.title = Label(self.inputs_frame, text='AJOUT D\'UN NOUVEAU BUS', font=('Helvetica', 20), bg=colors["BG"], fg=colors['Noir']).grid(row=0, columnspan=2, pady=20)
        self.lab_numero = Label(self.inputs_frame, text='Numero', font=('Helvetica', 12), bg=colors["BG"], fg=colors["FG"]).grid(row=1, column=0)
        self.input_numero = Entry(self.inputs_frame)
        self.input_numero.grid(row=1, column=1, padx=10)
        self.lab_regist = Label(self.inputs_frame, text='Registration', font=('Helvetica', 12), bg=colors["BG"], fg=colors["FG"]).grid(row=2, column=0)
        self.input_regist = Entry(self.inputs_frame)
        self.input_regist.grid(row=2, column=1, padx=10)
        self.lab_seats = Label(self.inputs_frame, text='Seats', font=('Helvetica', 12), bg=colors["BG"], fg=colors["FG"]).grid(row=3, column=0)
        self.input_seats = Entry(self.inputs_frame)
        self.input_seats.grid(row=3, column=1, padx=10)
        self.lab_line = Label(self.inputs_frame, text='Line assigned', font=('Helvetica', 12), bg=colors["BG"], fg=colors["FG"]).grid(row=4, column=0)
        self.input_line = Entry(self.inputs_frame)
        self.input_line.grid(row=4, column=1, padx=10)
        # Affichage des boutons
        self.btn_submit = Button(self.btn_frame, image=addbtn, bg=colors["FG"], fg=colors["Noir"], relief=FLAT, height=20, width=20, command=lambda:[self.submit_bus(), page_bus.update(), page_add_bus.close_frame(), page_add_bus.clear_entry(), page_bus.show_frame()]).grid(row=0, pady=30)
        self.btn_home = Button(self.btn_frame, image=homebtn, bg=colors["FG"], fg=colors["Noir"], relief=FLAT, height=20, width=20, command=lambda:[self.close_frame(), page_bus.show_frame()]).grid(row=1)
        # Affichage des frames
        self.container.pack(expand=YES)
        self.inputs_frame.pack(expand=YES)
        self.btn_frame.pack(expand=YES)

    def submit_bus(self):
        if re.match(r"[A-Z]{2}[0-9]{2}", self.input_numero.get()) :
            if re.match(r"[A-Z]{2}[0-9]{3}[A-Z]{2}", self.input_regist.get()):
                if re.match(r"[0-9]{2}", self.input_seats.get()):
                    new_bus = Bus(self.input_numero.get(), self.input_regist.get(), int(self.input_seats.get()))
                    bdd.cursor.execute(f'''SELECT * FROM bus_lines WHERE name="{self.input_line.get()}"''')
                    self.line_infos = bdd.cursor.fetchall()
                    new_bus.assign_line(*self.line_infos[0])
                    ref = (new_bus.num, new_bus.regist, new_bus.seats, new_bus.line_id)
                    all_bus_li = bdd.recup_bus_num()
                    if new_bus.num in all_bus_li:
                        bdd.cursor.execute(f'''UPDATE bus SET registration = "{new_bus.regist}", num_place = "{new_bus.seats}", id_line = "{new_bus.line_id}" WHERE bus.numero = "{new_bus.num}"''')
                    else :
                        bdd.cursor.execute('''INSERT INTO bus (numero, registration, num_place, id_line) VALUES (%s, %s, %s, %s)''', ref)
                    bdd.commit()
                else :
                    messagebox.showerror("ERROR", "Seats number must be between 01 and 99.")
            else :
                messagebox.showerror("ERROR", "Bus registration must follow this pattern: XX000XXX")
        else :
            messagebox.showerror("ERROR", "Bus numero must follow this pattern: XX00")
    
    def clear_entry(self):
        self.input_numero.delete(0, 'end')
        self.input_regist.delete(0, 'end')
        self.input_seats.delete(0, 'end')
        self.input_line.delete(0, 'end')

# Couleurs utilisées dans tkinter
colors = {"Rouge":"#f94144", "Bleu":"#4260f5", "Vert":"#1c9c1e", "Noir":"#000000", "Orange":"#f3722c", "Jaune":"#f9c74f", "BG":"#a4a4a4", "FG":"white"}

# Fenêtre de l'app
root = tk.Tk()
root.title("Breizhibus App")
root.geometry("800x400")
root.config(bg=colors["BG"])

#Frame principale
app_frame = Frame(root, bg=colors["BG"])
app_frame.pack(expand=YES)

# Images
homebtn = PhotoImage(file="./home.png")
addbtn = PhotoImage(file="./add.png")
deletebtn = PhotoImage(file="./times-circle.png")
editbtn = PhotoImage(file="./edit.png")

# Lancement de la fenêtre
bdd = Bdd()
page_main = MainPage()
page_stops = StopsPage()
page_bus = BusPage()
page_add_bus = BusAddPage()
page_stops.close_frame()
page_bus.close_frame()
page_add_bus.close_frame()
page_main.show_frame()
root.mainloop()