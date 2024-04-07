from matplotlib import pyplot as plt
from time import *

#============= data

d=open("C:/Users/evanb/Downloads/frenchssaccent.txt","r").read().splitlines()

#============= class

# Exercice 2
class Hashtable:
    
    def __init__(self,f,capacity):
        """Initializes the Hashtable object with a hash function and a capacity representing the number of list that will append elements"""
        self.__taille=capacity
        self.__tiroirs=[[] for i in range(capacity)]
        self.__function=f
        self.__nb_elements=0
    def put(self,key,value):
        """Puts the tuple (key,value) in the hash table. If the value key is already in the table, change the value of this key to the value 'value'"""
        image=self.__function(key)%self.__taille
        trouvé=False
        for entree in self.__tiroirs[image]:
            if entree[0]==key:
                entree=(key,value)
                trouvé=True
                break
        if not trouvé:
            self.__tiroirs[image].append((key,value))
    def tiroirs(self):
        """Returns a list containing every lists with keys and values as a tuple in it in the hash table"""
        return self.__tiroirs
            
    # Exercice 3
    def get(self,key):
        """Returns the value of the key in the hash table. If the key isn't in the table, return None"""
        image=self.__function(key)%self.__taille
        for value in self.__tiroirs[image]:
            if value[0]==key:
                return value[1]
        return None
    
    # Exercice 4
    def repartition(self):
        """Plots the density in the hash table"""
        X=[i for i in range(self.__taille)]
        Y=[len(value) for value in self.__tiroirs]
        plt.plot(X,Y,color='green')
        plt.show()
    
    # Exercice 6
    def resize(self):
        """Doubles the width of the hash table, and redistributes the element according to this new width"""
        newtable=Hashtable(self.__function,self.__taille*2)
        for tiroir in self.__tiroirs:
            for entree in tiroir:
                newtable.put(entree[0],entree[1])
        (self.__tiroirs,self.__taille)=(newtable.__tiroirs,newtable.__taille)    
    def newput(self,key,value):
        """Works like the 'put' method, but also resizes the hash table if there are too many elements in it"""
        if self.__nb_elements>1.2*self.__taille:
            self.resize()
        image=self.__function(key)%self.__taille
        trouvé=False
        for entree in self.__tiroirs[image]:
            if entree[0]==key:
                entree=(key,value)
                trouvé=True
                break
        if not trouvé:
            self.__tiroirs[image].append((key,value))
            self.__nb_elements+=1
            
    # Exercice 9
    def __setitem__(self,key,value):
        return self.put(key,value)
    def __getitem__(self,key):
        return self.get(key)

# Exercice 8
class HashRobintable:
    
    def __init__(self,f):
        """Initializes a new HashRobintable object which is an open adressing hash table"""
        self.__function=f
        self.__robintable=[]
        self.__taille=0
    def put(self,key):
        """Puts the key in the hash table according to the Robin Hood hashing, using the put_aux auxilary method"""
        self.put_aux(key,self.__function(key),0)
    def put_aux(self,key,DIB,PSL):
        """Puts the key in the hash table according to the Robin Hood hashing, starting at the DIB+PSL-ith entry"""
        entry=(key,DIB)
        puted=False
        while not puted:
            if DIB+PSL>=self.__taille:
                self.__robintable.append(None)
                self.__taille+=1
                print(self.__taille)
                print(DIB+PSL)
            elif self.__robintable[DIB+PSL]==None:
                self.__robintable[DIB+PSL]=entry
                puted=True
            elif PSL>DIB+PSL-self.__robintable[DIB+PSL][1]:
                newpute=self.__robintable[DIB+PSL]
                self.__robintable[DIB+PSL]=entry
                puted=True
                PSL=DIB+PSL-newpute[1]
                self.put_aux(newpute[0],newpute[1],PSL)
            else:
                PSL+=1
        return None  
    def tablebasse(self):
        """Returns the hash table"""
        return self.__robintable
        

#============= functions

# Exercice 2
def hash_naïf(chaine):
    """A naïve hash function""" 
    return sum([ord(c) for c in chaine])

# Exercice 4
def repardico(hacheur,n):
    """Shows the repartition of tuple (word, length of the word) in a dictionnary with n entries"""
    Dico=Hashtable(hacheur,n)
    for mot in d:
        Dico.put(mot,len(mot))
    Dico.repartition()

# Exercice 5
def hash_équitable(chaine):
    """A more equitable hash function"""
    h=0
    for c in chaine:
        h=h*31+ord(c)
    return h

# Exercice 6
def newrepardico(hacheur,n):
    """Works like the repardico method, but using the newput method instead of the put method"""
    Dico=Hashtable(hacheur,n)
    for mot in d:
        Dico.newput(mot,len(mot))
    Dico.repartition()

#============= main

if __name__== "__main__":

    # Exercice 2
    tablenumerouno=Hashtable(hash_naïf,4)
    tablenumerouno.put('abc',3)
    print(tablenumerouno.tiroirs())

    # Exercice 3
    print(tablenumerouno.get('aaa'))
    print(tablenumerouno.get('abc'))

    # Exercice 4
    cmoilatable=Hashtable(hash_naïf,42)
    for i in range(42,666):
        cmoilatable.put(str(i),i)
    cmoilatable.repartition()

    # Exercice 5
    repardico(hash_naïf,320)
    repardico(hash_naïf,10000)
    repardico(hash_équitable,320)
    repardico(hash_équitable,10000)

    # Exercice 6
    newrepardico(hash_naïf,320)
    newrepardico(hash_naïf,10000)
    newrepardico(hash_équitable,320)
    newrepardico(hash_équitable,10000)

    # Exercice 7
    test=Hashtable(hash_équitable,10)
    duree=[]
    for i in range(66666):
        t1=perf_counter()
        test.newput(str(i),i)
        dur=perf_counter()-t1
        if dur<0.0001:
            duree.append(dur)
    plt.plot([i for i in range(len(duree))], duree, color="g")
    
    # Exercice 8
    Tuck=HashRobintable(hash_naïf)
    Tuck.put("uwu")
    Tuck.put("kawaii")
    Tuck.put("noa")
    Tuck.put("nob")
    Tuck.put("ano")
    Tuck.put('noc')
    Tuck.put('con')
    Tuck.put('bon')
    Tuck.put('afghanistan')
    for i in range(42,666):
        Tuck.put(str(i))
    print(Tuck.tablebasse())
    
    # Exercice 9
    print(tablenumerouno['aaa'])
    print(tablenumerouno['abc'])
    
    

