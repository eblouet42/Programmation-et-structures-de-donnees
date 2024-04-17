from tkinter import *
from math import *
from random import *
from time import *
#============= class

class Graph:
    def __init__(self, graph):
        """Initializes the graph object with an adjacency list"""
        self.graph=graph
        self.root= Tk()
        # Initializes the canvas object 
        self.can= Canvas(self.root, width=400, height=400, bg="green")
        self.can.pack()
        # Defining the starting position and speed of each point, and drawing them
        self.pos=[(randrange(0,400),randrange(0,400)) for i in range(len(graph))]
        self.vitesse=[(randrange(-10,10),randrange(-10,10)) for i in range(len(graph))]
        self.draw()
        # Assigning the key 'f' with a deplacement of each point with a spring force between adjacent points
        self.root.bind('f',lambda truc:self.ressort())
        self.root.mainloop()
        
    def draw(self):
        """Draws the graph using the adjacency list and the position of each points"""
        for e in self.can.find_all():
             self.can.delete(e)
        for i in range(len(self.graph)):
            for j in self.graph[i]: # sucs de i a j
                self.can.create_line(self.pos[i][0], self.pos[i][1], self.pos[j][0], self.pos[j][1])
        coul=0
        for (x, y) in self.pos:
            self.can.create_oval(x-4,y-4,x+4,y+4,fill="#{}f{}{}{}f".format(coul,coul,coul,coul))
            if coul==9:
                coul=0
            else:
                coul+=1
                
    def ressort(self):
         """Moves each point with a spring force between each adjacent point"""
         newpos,newvitesse=[(0,0) for i in range(len(self.graph))],[(0,0) for i in range(len(self.graph))]
         pastemporel=0.1
         dubalai=1000
         for i in range(len(self.graph)):
             forceXi,forceYi=0,0
             (xi,yi)=self.pos[i]
             for j in range(len(self.graph)):
                 xj,yj=self.pos[j][0],self.pos[j][1]
                 # Spring force between adjacent points
                 if j in self.graph[i]:
                     l0=400//max(len(self.graph[i]),len(self.graph[j]))
                     l=sqrt((xi-xj)**2+(yi-yj)**2)
                     forceXi+=-(l-l0)*(xi-xj)/l
                     forceYi+=-(l-l0)*(yi-yj)/l
                 # Huge repulsory force between non adjacent points in order to separate connex parts
                 elif j!=i:
                     l0=400//max(len(self.graph[i]),len(self.graph[j]))
                     l=sqrt((xi-xj)**2+(yi-yj)**2)
                     forceXi+=dubalai/l*(xi-xj)/l
                     forceYi+=dubalai/l*(yi-yj)/l        
             (vxi,vyi)=self.vitesse[i]
             # Friction force in order to stop the movement after a while
             forceXi+=-vxi
             forceYi+=-vyi
             newpos[i]=(forceXi*pastemporel**2/2+vxi*pastemporel+xi,forceYi*pastemporel**2/2+vyi*pastemporel+yi)
             newvitesse[i]=(forceXi*pastemporel+vxi,forceYi*pastemporel+vyi)
             # Makes sure the point don't move out of the canva
             if newpos[i][0]<20:
                 newpos[i]=(20,newpos[i][1])
             elif newpos[i][0]>380:
                 newpos[i]=(380,newpos[i][1])
             if newpos[i][1]<20:
                 newpos[i]=(newpos[i][0],20)
             elif newpos[i][1]>380:
                 newpos[i]=(newpos[i][0],380)
         self.pos,self.vitesse=newpos,newvitesse
         self.draw()
                
#============= main

if __name__=='__main__':
    Graph([[2, 7, 11], [3, 4, 9, 10], [5, 8, 0], [10, 1, 4, 6], [3, 1, 6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1, 6, 9], [0]])
