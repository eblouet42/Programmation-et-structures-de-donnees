#============= class

# Exercice 2
class Tree:
    
    def __init__(self, etiquette, *children):
        """Initializes the tree object with a label and a tuple representing the children (trees)"""
        self.__etiquette=etiquette
        if len(children) == 1 and type(children[0]) == tuple:
            self.__children = children[0]
        else:
            self.__children = children
    def label(self):
        """Returns the label of the tree"""
        return self.__etiquette
    def children(self):
        """Returns the list of the children of the tree"""
        return self.__children
    def nb_children(self):
        """Returns the number of children of the tree"""
        return len(self.children())
    def child(self, i):
        """Returns the i-th child of the tree"""
        return self.children()[i]
    def is_leaf(self):
        """Returns if the tree is but a leaf (no children)"""
        return self.children()==()
    
    # Exercice 3
    def depth(self):
        """Returns the depth of the tree"""
        if self.is_leaf():
            return 0
        else:
            l=[]
            for child in self.children():
                l.append(child.depth())
            return 1+max(l)
    
    # Exercice 4
    def __str__(self):
        """Returns a string representing the tree"""
        if self.is_leaf():
            return self.label()
        else:
            chaine= "{}(".format(self.label())
            c=self.children()
            for i in range(len(c)-1):
                chaine+="{},".format(c[i].__str__())
            chaine+="{})".format(c[len(c)-1].__str__())
            return chaine
    def eqmaisjavaispascomprisjaifaitpluscompliqué(self,arbre):
        """Returns if the two trees are representing the same tree, 
        meaning that each node from the first tree has the 
        same children as the second tree, not particulary in the same order"""
        if self.is_leaf() or arbre.is_leaf():
            return (self.is_leaf() and arbre.is_leaf() and self.label()==arbre.label())
        else:
            if self.label()!=arbre.label() or self.nb_children()!=arbre.nb_children():
                return False
            else:
                clesmemes=True
                for child1 in self.children():
                    correspondance=False
                    for child2 in arbre.children():
                        if child1.eqmaisjavaispascomprisjaifaitpluscompliqué(child2):
                            correspondance=True
                    if not correspondance:
                        clesmemes=False
                for child2 in arbre.children():
                    correspondance=False
                    for child1 in self.children():
                        if child2.eqmaisjavaispascomprisjaifaitpluscompliqué(child1):
                            correspondance=True
                    if not correspondance:
                        clesmemes=False
                return clesmemes
    def __eq__(self,arbre):
        """Returns if the two trees are exactly the same,
        meaning that each node from the first tree has the 
        same children as the second tree, in the same order"""
        return self.label()==arbre.label() and self.children()==arbre.children()
        
    # Exercice 5
    def deriv(self,var):
        """Derivates the tree with respect of the variable 'var' """
        if self.label() not in ["+","*"]:
            if self.label()==var:
                return Tree("1")
            else:
                return Tree("0")
        elif self.label()=="+":
            return Tree("+",tuple([c.deriv(var) for c in self.children()]))
        else:
            L=list(self.children())
            l=[]
            for i in range(len(L)):
                lintermediaire=L
                lintermediaire[i]=lintermediaire[i].deriv(var)
                l.append(Tree("*",tuple(lintermediaire)))
            return Tree("+",tuple(l))
    
    # Exercice 6
    def substitute(self,t1,t2):
        if self.is_leaf():
            return self
        elif puisjesubstituerdepuislà(self,t1):
            return t2
        else:
            return Tree(self.label(),self.children()[0].substitute(t1,t2),self.children()[1].substitute(t1,t2))
                
        

#============= functions

def puisjesubstituerdepuislà(arbre,sub):
    if sub.nb_children()==0:
        return sub.label()==arbre.label()
    if arbre.nb_children()==0:
        return arbre.__eq__(sub)
    else:
        if arbre.label()!=sub.label() or arbre.nb_children()<sub.nb_children():
            return False
        else:
            (i,j,luicbon)=(0,0,0)
            while i<sub.nb_children() and j<arbre.nb_children():
                if puisjesubstituerdepuislà(arbre.children()[j],sub.children()[i]):
                    (i,j,luicbon)=(i+1,j+1,luicbon+1)
                else:
                    j+=1
            return luicbon==sub.nb_children()
        
#def substituerdepuislà(arbre,t1,t2):
    
    

#============= main

if __name__== "__main__":
    
    # Exercice 2
    Atest= Tree("f",Tree("a"),Tree("b"))
    print(Atest.label())
    print(Atest.child(0).label())
    assert(Atest.child(1).label()=="b")
    assert(Atest.child(1).is_leaf())
    
    # Exercice 3
    A1= Tree("f",Tree("a"),Tree("b",Tree("b1"),Tree("b2"),Tree("b3",Tree("fin"))))
    print(Atest.depth())
    print(A1.depth())
    
    # Exercice 4
    print(str(A1))
    A1presque= Tree("f",Tree("a"),Tree("b",Tree("b1"),Tree("b2"),Tree("b3",Tree("début"))))
    A1presquepareil= Tree("f",Tree("a"),Tree("b",Tree("b2"),Tree("b1"),Tree("b3",Tree("fin"))))
    A1paspareil= Tree("f",Tree("a"),Tree("b",Tree("b1"),Tree("b3"),Tree("b2",Tree("fin"))))
    assert(not A1.eqmaisjavaispascomprisjaifaitpluscompliqué(A1presque))
    assert(A1.eqmaisjavaispascomprisjaifaitpluscompliqué(A1presquepareil))
    assert(not A1.eqmaisjavaispascomprisjaifaitpluscompliqué(A1paspareil))
    A1pareil=Tree("f",Tree("a"),Tree("b",Tree("b1"),Tree("b2"),Tree("b3",Tree("fin"))))
    assert(A1==A1pareil)
    
    # Exercice 5
    Arbre1aderiver=Tree("+",Tree("3"),Tree("X"))
    Arbre2aderiver=Tree("+",Tree("+",Tree("*",Tree("3"),Tree("*",Tree("X"),Tree("X"))),Tree("*",Tree("5"),Tree("X"))),Tree("7"))
    print(str(Arbre1aderiver.deriv("X")))
    print(str(Arbre2aderiver.deriv("X")))
    print(str(Arbre2aderiver.deriv("3")))
    
    # Exercice 6
    t1=Tree("b")
    t2=Tree("baguette")
    print(str(A1.substitute(t1,t2)))