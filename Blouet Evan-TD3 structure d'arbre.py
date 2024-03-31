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
            if self.is_leaf():
                return Tree("0")
            elif self.nb_children()==1:
                return self.children()
            else:
                L=list(self.children())
                l=[]
                for i in range(len(L)):
                    if L[i].deriv(var)!=Tree("0"):
                        l.append(L[i].deriv(var))
                if len(l)==0:
                    return Tree("0")
                elif len(l)==1:
                   return Tree(l[0].label(),l[0].children())
                else:
                    return Tree("+",tuple(l))
        elif self.label()=="*":
            L=list(self.children())
            l=[]
            for i in range(len(L)):
                lintermediaire=L+[]
                lintermediaire[i]=lintermediaire[i].deriv(var)
                if lintermediaire[i]!=Tree("0"):
                    l.append(Tree("*",tuple(lintermediaire)))
            if len(l)==0:
                return Tree("0")
            elif len(l)==1:
                return Tree(l[0].label(),l[0].children())
            else:
                return Tree("+",tuple(l))
    
    # Exercice 6
    def oversubstitute(self,t1,t2):
        """Substitutes any occurence (wherever in the original tree) of the sub-tree t1 by the sub-tree t2"""
        if puisjesubstituerdepuislà(self,t1):
            return substituerdepuislà(self,t1,t2)
        elif self.is_leaf():
            return self
        else:
            L=list(self.children())
            l=[]
            for i in range(len(L)):
                l.append(L[i].oversubstitute(t1,t2))
            return Tree(self.label(),tuple(l))
        
    def substitute(self,t1,t2):
        """Substitutes any occurence (at the bottom of the original tree) of the sub-tree t1  by the sub-tree t2"""
        if self.is_leaf() and self!=t1:
            return self
        if self==t1:
            return t2
        else:
            l=[]
            for child in list(self.children()):
                l.append(child.substitute(t1,t2))
            return Tree(self.label(),tuple(l))

    # Exercice 7
    def simplify(self):
        """Simplify the tree according to simple rules such as *('X','0')='0' or +('a','b')='c' where a,b are integers and c=a+b"""
        tree = Tree('')
        simplified = self
        while simplified != tree:
            tree = simplified
            simplified=simplified.substitute(Tree("+",Tree("X"),Tree("0")),Tree("X"))
            simplified=simplified.substitute(Tree("+",Tree("0"),Tree("X")),Tree("X"))
            simplified=simplified.substitute(Tree("*",Tree("X"),Tree("0")),Tree("0"))
            simplified=simplified.substitute(Tree("*",Tree("0"),Tree("X")),Tree("0"))
            simplified=simplified.substitute(Tree("*",Tree("X"),Tree("1")),Tree("X"))
            simplified=simplified.substitute(Tree("*",Tree("1"),Tree("X")),Tree("X"))
            simplified=simplified.simplify_cas_aplusb_et_afoisb()
        return simplified

    def simplify_cas_aplusb_et_afoisb(self):
        """Simplify the tree according to the following rules: +(a,b)=c and *(a,b)=d where a and b represent integers and c=a+b, d=a*b"""
        if self.is_leaf():
            return self
        elif self.nb_children()==1:
            return self.child(0)
        else:
            newchildren=[]
            tosimplify=[]
            for child in self.children():
                if child.label().isdigit():
                    tosimplify.append(int(child.label()))
                else:
                    newchildren.append(child.simplify_cas_aplusb_et_afoisb())
            if self.label() == "+":
                if tosimplify!=[]:
                    newchildren=[Tree(str(sum(tosimplify)))]+newchildren
                return Tree("+",tuple(newchildren))
            if self.label() == "*":
                if tosimplify!=[]:
                    newchildren=[Tree(str(prod(tosimplify)))]+newchildren
                return Tree("*",tuple(newchildren))
    # Exercice 9
    def not_infixe(self):
        """Returns a string of the tree in a infix notation"""
        return pref_to_inf(str(self))
                        
#============= functions

# Exercice 6
def puisjesubstituerdepuislà(arbre,sub):
    """Returns if the sub-tree 'sub' is a sub-tree of the tree 'arbre' from its origin"""
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
def substituerdepuislà(arbre,t1,t2):
    """Returns the tree 'arbre' where the sub-tree 't1', beginning at the origin of the tree 'arbre', has been substituted by the sub-tree 't2' """
    if t1.nb_children()==0:
        return Tree(t2.label(),arbre.children())
    else:
        newchildren=[]
        i=0
        for j in range(arbre.nb_children()):
            if i<t1.nb_children() and arbre.child(j).label()==t1.child(i).label():
                if i<t2.nb_children():
                    newchildren.append(substituerdepuislà(arbre.child(j),t1.child(i),t2.child(i)))
                i+=1
            else:
                newchildren.append(arbre.child(j))
        while i<t2.nb_children():
            newchildren.append(t2.child(i))
            i+=1
        return Tree(t2.label(),tuple(newchildren))
    
#Exercice 7
def prod(list_of_int):
    """Returns the product of the elements of the list"""
    x=int(list_of_int!=[])
    for nombre in list_of_int:
        x=x*nombre
    return x

# Exercice 8
def polynome_en_x(polynome,x):
    """Evaluate the tree 'polynome' representing a polynome at the point x where x is an integer"""
    return str(polynome.substitute(Tree("X"),Tree(str(x))).simplify())

# Exercice 9
def pref_to_inf(car):
    """Transforms an prefix notation in a infix notation"""
    if len(car)==1:
        return car
    else:
        operation=car[0]
        dans_la_parenthese=car[2:-1]
        coupure=0
        parentheseouverte=0
        parenthesefermee=0
        for i in range(len(dans_la_parenthese)):
            if dans_la_parenthese[i]==',' and parenthesefermee==parentheseouverte:
                coupure=i
                parentheseouverte+=42
            elif dans_la_parenthese[i]=='(':
                parentheseouverte+=1
            elif dans_la_parenthese[i]==')':
                parenthesefermee+=1
        gauche=dans_la_parenthese[:coupure]
        droite=dans_la_parenthese[coupure+1:]
        print(gauche,operation,droite)
        return "({}{}{})".format(pref_to_inf(gauche),operation,pref_to_inf(droite))

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
    print(str(Arbre2aderiver))
    print(str(Arbre2aderiver.deriv("X")))
    print(str(Arbre2aderiver.deriv("Y")))
    
    # Exercice 6
    t1=Tree("b",Tree("b3",Tree("fin")))
    t2=Tree("baguette",Tree("fromage",Tree("vin"),Tree("esclavage")))
    print(str(A1.oversubstitute(t1,t2)))
    assert(A1.substitute(t1,t2)==A1)
    print(str(A1.substitute(Tree("fin"),Tree("début",Tree("fin1"),Tree("fin2")))))
    
    # Exercice 7
    print(str(Arbre2aderiver.simplify()))
    print(str(Arbre2aderiver.deriv("X").simplify()))
    print(str(Arbre2aderiver.deriv("Y").simplify()))
    
    # Exercice 8
    print(str(polynome_en_x(Arbre2aderiver,0)))
    print(str(polynome_en_x(Arbre2aderiver,1)))
    print(str(polynome_en_x(Arbre2aderiver,42)))
    print(str(polynome_en_x(Arbre2aderiver,666)))
    
    # Exercice 9
    print(Arbre2aderiver.not_infixe())
    print(Arbre2aderiver.deriv("X").simplify().not_infixe())
        