# <center>Projet Breizhibus</center>

## Thomas Chaigneau

---

Projet lié au brief Simplon `Breizhibus, gestion de lignes de bus`.  
Nous détaillerons dans un premier chapitre le fonctionnement de l'application, dans un second nous expliquerons les choix techniques.
Enfin, dans un dernier point nous présenterons les difficultées rencontrées et leurs solutions.

---

### 1. Présentation de l'application

L'application se compose de 4 pages différentes.  

- La page d'accueil :

![Home Screen](./screenshots/home_screen.png)

Cette page dispose de deux boutons qui permettent de naviguer dans l'application.  
Un bouton pour pouvoir afficher les différentes lignes et les arrêts associés.
Un autre bouton permettant d'afficher tous les bus de la compagnies.

- La page des lignes de bus :

![Lines Screen](./screenshots/lines_screen.png)

Chaque ligne dispose de son bouton personnel pour afficher les arrêts qui lui sont liés.

- La page des bus :

![Bus Screen](./screenshots/bus_screen.png)

Toutes les informations des bus sont listées dans le tableau.
Chaque bus dispose de deux boutons :   
    - `modifier` : ce bouton permet de modifier les informations d'un bus et de sauvegarder les changements dans la base de données    
    - `supprimer` : ce bouton permet de supprimer un bus de la base de données   

le bouton `+` permet d'accèder à la page d'ajout de bus.

- La page d'ajout de bus :

![Add Bus Screen](./screenshots/add_bus_screen.png)

Cette page est accessible via le bouton `+` qui permet d'ajouter un bus.
Si le numéro du bus existe déjà dans la base de données, le bus ne sera ajouté mais modifié directement dans la ligne liée.

### 2. Choix techniques