from tkinter import *
from math import *
from random import *
from time import *

COLORS = ['antiquewhite', 'aqua', 'aquamarine',  'bisque', 'black',  'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgrey', 'darkgreen', 'darkkhaki', 'darkmagenta', 'darkolivegreen']

#============= class

class Graph:
    def __init__(self, graph,taillex,tailley,positions,lescouleurs):
        """Initializes the graph object with an adjacency list and a position list"""
        self.graph=ouhlalajesuistoutdesoriente(graph)
        self.pos=positions
        self.root= Tk()
        # Initializes the canvas object 
        self.can= Canvas(self.root, width=taillex, height=tailley, bg="white")
        self.can.pack()
        self.colors=lescouleurs
        # Draws the graph
        self.draw()
        # Assigning the key 'c' with a colorization of each connected component of the graph
        self.root.bind('c',lambda truc:self.cjolicaaffichedescouleurs())
        self.label=Label(self.root, text="Press 'C' to make the connected components appear")
        self.label.pack()
        self.root.mainloop()
        
    def draw(self):
        """Draws the graph using the adjacency list and the position of each points"""
        N = len(self.graph)
        for e in self.can.find_all():
            self.can.delete(e)
        for i in range(N):
            for j in self.graph[i]:
                self.can.create_line(self.pos[i][0], self.pos[i][1], self.pos[j][0], self.pos[j][1])
        for i in range(N):
            x, y = self.pos[i]
            self.can.create_oval(x-6, y-6, x+6, y+6, fill=self.colors[i])
            #self.can.create_text(x-12,y,text=f"{i}")

# Exercice 3
    def cjolicaaffichedescouleurs(self):
        """Colorizes each connected component with a distinct color"""
        Compcnx=composantesconnexes(self.graph)
        coulor=[0 for i in range(len(self.graph))]
        for i in range(len(Compcnx)):
            lacouleurdelacomposante=color_generator()
            for sommet in Compcnx[i]:
                coulor[sommet]=lacouleurdelacomposante
        self.colors=coulor
        self.draw()

#============ function

# Exercice 1
def ouhlalajesuistoutdesoriente(graphe):
    """Transforms a non oriented graph in a oriented graph"""
    desoriente = {}
    for sommet in range(len(graphe)):
        voisins = graphe[sommet]
        if sommet not in desoriente:
            desoriente[sommet] = set()
        for voisin in voisins:
            if voisin not in desoriente:
                desoriente[voisin] = set()
            desoriente[sommet].add(voisin)
            desoriente[voisin].add(sommet)
    for sommet in desoriente:
        desoriente[sommet] = list(desoriente[sommet])
    desoriente = [desoriente[i] for i in range(len(desoriente))]
    return desoriente

# Exercice 2
def composanteconnexe(listadj,lparcouru,composante,i):
    """Returns the connected component containing the vertex i"""
    if i not in lparcouru:
        lparcouru.append(i)
        composante.append(i)
        for sommet in listadj[i]:
            (lparcouru,composante)=composanteconnexe(listadj,lparcouru,composante,sommet)
    return(lparcouru,composante)
def composantesconnexes(listadj):
    
    """Returns a list with every connected component of the graph"""
    L=[]
    lparcouru=[]
    for i in range(len(listadj)):
        if i not in lparcouru:
            (lparcouru,composante)=composanteconnexe(listadj,lparcouru,[],i)
            L.append(composante)
    return L

# Exercice 4
def color_generator():
    """Generates a random RGB color"""
    r, g, b = randint(0,255), randint(0,255),randint(0,255)
    return f"#{r:02x}{g:02x}{b:02x}"
def creationaleatoiredegigagraphezeroquatre(N):
    """A graph with N^2 vertices, with p=0.4"""
    graphe=[]
    positions=[]
    couleur=[]
    (taillex,tailley)=(20*N,20*N)
    for i in range(N):
        for j in range(N):
            arreteuh=[]
            positions.append([20*j+10,20*i+10])
            couleur.append(color_generator())
            if randint(1,5)>3:
                if i+1<N:
                    arreteuh.append((i+1)*N+j)
            if randint(1,5)>3:
                if j+1<N:
                    arreteuh.append(i*N+j+1)
            graphe.append(arreteuh)
    return Graph(graphe,taillex,tailley,positions,couleur)

# Exercice 5
def creationaleatoiredegigagrapheunechancesurdeux(N):
    """A graph with N^2 vertices, with p=0.5"""
    graphe=[]
    positions=[]
    couleur=[]
    (taillex,tailley)=(20*N,20*N)
    for i in range(N):
        for j in range(N):
            arreteuh=[]
            positions.append([20*j+10,20*i+10])
            couleur.append(color_generator())
            if randint(1,2)==1:
                if i+1<N:
                    arreteuh.append((i+1)*N+j)
            if randint(1,2)==1:
                if j+1<N:
                    arreteuh.append(i*N+j+1)
            graphe.append(arreteuh)
    return Graph(graphe,taillex,tailley,positions,couleur)

#============= main

if __name__=='__main__':
    # Exercice 3
    a=Graph([[2, 7, 11], [3, 4, 9, 10], [5, 8, 0], [10, 1, 4, 6], [3, 1, 6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1, 6, 9], [0]],500,500,[[131, 352], [464, 315], [254, 211], [393, 346], [381, 432], [343,  98], [298, 326], [187, 475], [245, 407], [483, 212], [365, 216], [149, 198]],[COLORS[k] for k in range(12)])
    # Exercice 4
    G=creationaleatoiredegigagraphezeroquatre(35)
    # Exercice 5
    G=creationaleatoiredegigagrapheunechancesurdeux(35)
    # Une grosse composante connexe apparaît