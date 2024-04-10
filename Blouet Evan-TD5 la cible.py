from tkinter import *
from math import *
from random import *
class BarGUI:
    """BarGUI is simple GUI for displaying either a target or a creepy face."""
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=400, height=400, bg='red')
        self.canvas.pack(side=TOP, padx=5, pady=5)
        self.draw_target()
        self.but1= Button(self.root,text="Feu!!!!!!!!!!!!!!!!!!", command=self.tiraléatoire, bg="orange")
        self.but1.pack(side=LEFT,fill=BOTH)
        self.but2= Button(self.root,text="Ragequit", command=self.root.destroy, bg="green")
        self.but2.pack(side=RIGHT,fill=BOTH)
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
    def tiraléatoire(self):
        S=0
        for i in range(5):
            (x,y)=(randint(0,400),randint(0,400))
            S+=score(x,y)
            self.draw_circle(x,y,5,'red','noir')
        return S
            
BarGUI()

def score(x,y):
    rayon=sqrt((x-200)**2+(y-200)**2)
    touche=6-rayon//30
    return max(touche, 0)