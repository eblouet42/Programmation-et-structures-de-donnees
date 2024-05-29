from math import *
from random import *

#============= data

Proust="C:/Users/evanb/Downloads/proust.txt"
Ernaux="C:/Users/evanb/Downloads/ernaux.txt"
Flaubert="C:/Users/evanb/Downloads/flaubert.txt"
Baudelaire="C:/Users/evanb/Downloads/baudelaire.txt"

#============= class

class Node:
    def __init__(self, etiquette, children):
        """Initializes the node object with a label and a tuple representing the children (trees)"""
        self.etiquette=etiquette
        self.children=children
    def nb_children(self):
        """Returns the number of children of the node"""
        return len(self.children)
    def is_leaf(self):
        """Returns if the node is but a leaf (no children)"""
        return self.children==[]
    def depth(self):
        """Returns the depth of the node"""
        if self.is_leaf():
            return 0
        else:
            l=[]
            for child in self.children:
                l.append(child.depth())
            return 1+max(l)
    def __eq__(self,node):
        """Returns if the two nodes are exactly the same
        (same label, same children)"""
        return self.etiquette==node.etiquette and self.children==node.children
    def __str__(self):
        """Returns a string representing the tree"""
        if self.is_leaf():
            return self.etiquette
        else:
            chaine= "{}[".format(self.etiquette)
            c=self.children
            for i in range(len(c)-1):
                chaine+="{},".format(c[i].__str__())
            chaine+="{}]".format(c[len(c)-1].__str__())
            return chaine
        
    # Exercice 3
    def child(self, i):
        """Returns the i-th child of the node"""
        return self.children[i]
    def tree_at(self,position):
        """ Returns the node following the position tuple 'position' in the tree"""
        if type(position)==int:
            position=(position,)
        if position==():
            return self
        else:
            return self.child(position[0]).tree_at(position[1:])
    
    # Exercice 4
    def changer(self,position,newnode):
        """ Changes the node at the position 'position' by the node 'newnode' """
        if type(position)==int:
            position=(position,)
        if position==():
            self.etiquette=newnode.etiquette
            self.children=newnode.children
        else:
            self.child(position[0]).changer(position[1:],newnode)
            
    # Exercice 5
    def pos_au_pif(self,liste_pos):
        """ Returns a random position tuple, beginning at the node at the position liste_pos
        Choose liste_pos=[] for a perfect random position tuple"""
        n=len(self.children)
        if self.children==[]:
            return tuple(liste_pos)
        else:
            i=randint(0,n-1)
            liste_pos.append(i)
            return self.child(i).pos_au_pif(liste_pos)
            
    
#============= functions

# Exercice 2
def read_file(fileName):
    f = open(fileName)
    l = f.readline()
    liste = []
    for i in range(int(l)):
        args = f.readline().rstrip()
        fields = args.split(" ")
        if len(fields) > 1:
            liste.append(Node(fields[0], [Node(fields[1], [])]))
        else:
            liste.append(Node(args, []))
    for line in f:
        l1, l2 = line.split("->")
        liste[int(l1)].children.append(liste[int(l2)])
    return liste[0]
def écraser(chaine,ponct):
    """ Creates a more readable string of a normal string for a tree"""
    phrase=""
    crochet=False
    for i in range(len(chaine)):
        if chaine[i]=="[":
            crochet=True
            j=i+1
        if chaine[i]=="]" and crochet==True:
            mot=chaine[j:i]
            if "â€™" in mot:
                phrase+="c'"
            else:
                phrase+=chaine[j:i]+" "
            crochet=False
    newphrase=''
    for i in range(len(phrase)):
        if i==0:
            newphrase+=phrase[i].upper()
        elif not ponct or (i!=len(phrase)-3 and i!=len(phrase)-1):
            newphrase+=phrase[i]
    return newphrase
def citation(chemin_fichier):
    """ Returns a string containing a famous quote from a french author """
    return écraser(str(read_file(chemin_fichier)),True)
def permute(tree1,p1,tree2,p2):
    """ Permutes the node of tree1 at position 'p1' by the node of tree2 at position 'p2' """
    copiteur1=Node(tree1.tree_at(p1).etiquette,tree1.tree_at(p1).children.copy())
    tree1.changer(p1,tree2.tree_at(p2))
    tree2.changer(p2,copiteur1)
    print(écraser(str(tree1),True)) 
    print(écraser(str(tree2),True))
    return None
def au_pif(tree1,tree2):
    """ Randomly permutes two nodes of the two trees 'tree1' and 'tree2' """
    p1,p2=tree1.pos_au_pif([]),tree2.pos_au_pif([])
    print(p1,p2)
    permute(tree1,p1,tree2,p2)
    return None
    
#============= main

if __name__== "__main__":
    # Exercice 1
    jeandort=Node("S",[Node("NP",[Node("Jean",[])]),Node("V",[Node("dort",[])])])
    print(jeandort)
    # Exercice 2
    print(read_file(Proust))
    print(citation(Proust))
    print(citation(Ernaux))
    print(citation(Flaubert))
    print(citation(Baudelaire))
    # Exercice 3
    Ern=read_file(Ernaux)
    Pr=read_file(Proust)
    Baud=read_file(Baudelaire)
    Fl=read_file(Flaubert)
    print(Ern.tree_at((0,2,1,0)))
    print(Pr.tree_at(2))
    print(écraser(str(Pr.tree_at(2)),False))
    # Exercice 4
    permute(Pr,(1,1,0),Ern,(0,2,1,0))
    permute(Baud,(2,0,1,0),Fl,(0,1,0))
    # Exercice 5
    au_pif(Fl,Baud)
    
    