from tkinter import *
from math import *
from random import *

#============= class

class Cible:
    """BarGUI is simple GUI for displaying either a target or a creepy face."""
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=400, height=400, bg='red')
        self.canvas.pack(side=TOP, padx=5, pady=5)
        self.coor=(randint(0,400), randint(0,400))
        (x,y)=(self.coor[0],self.coor[1])
        self.draw_target()
        self.truc1=self.canvas.create_oval(x-5,y-5,x+5,y+5,outline='purple')
        self.truc2=self.canvas.create_line(x-10,y,x+10,y, fill='purple')
        self.truc3=self.canvas.create_line(x,y-10,x,y+10, fill='purple')
        self.move_da_mire(0,300,3000,3)
        self.but1= Button(self.root,text="Feu!", command=self.rafalealeatoire, bg="orange")
        self.but1.pack(side=LEFT,fill=Y)
        self.but2= Button(self.root,text="Quit", command=self.root.destroy, bg="green")
        self.but2.pack(side=RIGHT,fill=Y)
        self.root.bind('p',lambda truc:self.tiraleatoire())
        self.root.bind('f',lambda truc:self.tirvise())
        self.root.mainloop()
    def draw_circle(self, x, y, r, coul1, coul2):
        """Draw un circle of centre (x, y) and radius r."""
        self.canvas.create_oval(x-r, y-r, x+r, y+r, outline=coul1, fill=coul2)
    def draw_target(self):
        """The Canvas is now displaying a target."""
        self.draw_circle(200,200,170,"red","ivory")
        for radius in range(170,0,-30):
            if radius==50:
                self.draw_circle(200, 200, radius, "red","red")
            else:
                self.draw_circle(200, 200, radius, "red","ivory")
        self.canvas.create_line(200, 0, 200, 400, fill='red')
        self.canvas.create_line(0, 200, 400, 200, fill='red')
        for i in range(1,7):
            if i==5:
                self.canvas.create_text(200,45+(i-1)*30,text=str(i),font=('Times',"18",'bold'),fill='white')
            else:
                self.canvas.create_text(200,45+(i-1)*30,text=str(i),font=('Times',"18",'bold'),fill='red')
    def rafalealeatoire(self):
        S=0
        for i in range(5):
            (x,y)=(randint(0,400),randint(0,400))
            rayon=sqrt((x-200)**2+(y-200)**2)
            touche=6-(rayon+10)//30
            S+=max(touche, 0)
            self.draw_circle(x,y,5,'red','black')
        label= Label(self.root, text="Score: {} points".format(S))
        label.pack()
        self.but1["state"]=DISABLED
    def tiraleatoire(self):
        (x,y)=(randint(0,400),randint(0,400))
        rayon=sqrt((x-200)**2+(y-200)**2)
        touche=6-(rayon+10)//30
        self.draw_circle(x,y,5,'red','black')
        label= Label(self.root, text="Score: {} points".format(max(touche,0)))
        label.pack()
    def tirvise(self):
        (x,y)=(self.coor[0],self.coor[1])
        rayon=sqrt((x-200)**2+(y-200)**2)
        touche=6-(rayon+10)//30
        self.draw_circle(x,y,5,'red','black')
        label= Label(self.root, text="Score: {} points".format(max(touche,0)))
        label.pack()
    def move_da_mire(self,t,tempsrandom1,tempsrandom2,tempsentredeplacementenms):
        ampleurdeplacement=max(2,6-(sqrt((self.coor[0]-200)**2+(self.coor[1]-200)**2)+10)//30)
        L=[-ampleurdeplacement,0,ampleurdeplacement]
        if t>tempsrandom2:
            if sqrt((self.coor[0]-200)**2+(self.coor[1]-200)**2)<5:
                  t=0
                  tempsrandom1=randint(0,500)
                  tempsrandom2=randint(1000,2000)
                  (i,j)=(randint(0,2),randint(0,2))
                  (x,y)=(L[i],L[j])
            else:
                if self.coor[0]<200 and self.coor[1]<200:
                    (i,j)=(randint(1,2),randint(1,2))
                    (x,y)=(L[i],L[j])
                elif self.coor[0]>200 and self.coor[1]<200:
                    (i,j)=(randint(0,1),randint(1,2))
                    (x,y)=(L[i],L[j])
                elif self.coor[0]<200 and self.coor[1]>200:
                    (i,j)=(randint(1,2),randint(0,1))
                    (x,y)=(L[i],L[j])
                else:
                    (i,j)=(randint(0,1),randint(0,1))
                    (x,y)=(L[i],L[j])
        elif t<tempsrandom1:
            if self.coor[0]<200 and self.coor[1]<200:
                (i,j)=(randint(0,1),randint(0,1))
                (x,y)=(L[i],L[j])
            elif self.coor[0]>200 and self.coor[1]<200:
                (i,j)=(randint(1,2),randint(0,1))
                (x,y)=(L[i],L[j])
            elif self.coor[0]<200 and self.coor[1]>200:
                (i,j)=(randint(0,1),randint(1,2))
                (x,y)=(L[i],L[j])
            else:
                (i,j)=(randint(1,2),randint(1,2))
                (x,y)=(L[i],L[j])
        else:
            (i,j)=(randint(0,2),randint(0,2))
            (x,y)=(L[i],L[j])
        if self.coor[0]+x<=400 and self.coor[0]+x>=0 and self.coor[1]+y<=400 and self.coor[1]+y>=0:
            self.canvas.move(self.truc1,x,y)
            self.canvas.move(self.truc2,x,y)
            self.canvas.move(self.truc3,x,y)
            self.coor=(self.coor[0]+x,self.coor[1]+y)
        self.canvas.after(tempsentredeplacementenms,lambda :self.move_da_mire(t+tempsentredeplacementenms,tempsrandom1,tempsrandom2,tempsentredeplacementenms))

#============= main

if __name__=='__main__':
    Cible()
