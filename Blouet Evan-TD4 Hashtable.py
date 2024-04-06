from matplotlib import pyplot as plt
from time import *

#============= data

d=open("C:/Users/evanb/Downloads/frenchssaccent.txt","r").read().splitlines()

#============= class

# Exercice 2
class Hashtable:
    
    def __init__(self,f,capacity):
        self.__taille=capacity
        self.__tiroirs=[[] for i in range(capacity)]
        self.__function=f
        self.__nb_elements=0
    def put(self,key,value):
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
        return self.__tiroirs
            
    # Exercice 3
    def get(self,key):
        image=self.__function(key)%self.__taille
        for value in self.__tiroirs[image]:
            if value[0]==key:
                return value[1]
        return None
    
    # Exercice 4
    def repartition(self):
        X=[i for i in range(self.__taille)]
        Y=[len(value) for value in self.__tiroirs]
        plt.plot(X,Y,color='green')
        plt.show()
    
    # Exercice 6
    def resize(self):
        newtable=Hashtable(self.__function,self.__taille*2)
        for tiroir in self.__tiroirs:
            for entree in tiroir:
                newtable.put(entree[0],entree[1])
        (self.__tiroirs,self.__taille)=(newtable.__tiroirs,newtable.__taille)    
    def newput(self,key,value):
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
            
    # Exercice 7
    def taille(self):
        return self.__taille
    
    # Exercice 9
    def __setitem__(self,key,value):
        return self.put(key,value)
    def __getitem__(self,key):
        return self.get(key)
    
        

#============= functions

# Exercice 2
def hash_naïf(chaine):
    return sum([ord(c) for c in chaine])

# Exercice 4
def repardico(hacheur,n):
    Dico=Hashtable(hacheur,n)
    for mot in d:
        Dico.put(mot,len(mot))
    Dico.repartition()

# Exercice 5
def hash_équitable(chaine):
    h=0
    for c in chaine:
        h=h*31+ord(c)
    return h

# Exercice 6
def newrepardico(hacheur,n):
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
    
    # Exercice 9
    tablenumerouno['aaa']
    

