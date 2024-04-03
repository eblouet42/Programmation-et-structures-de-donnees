#============= class

# Exercice 2
class Hashtable:
    
    def __init__(self,f,capacity):
        self.__taille=capacity
        self.__tiroirs=capacity*[[]]
        self.__function=f
    def put(self,key,value):
        image=self.__function(key)%self.__taille
        ya=False
        for value in self.__tiroirs[image]:
            if value[0]==key:
                value=(key,value)
                ya=True
        if not ya:
            self.tiroirs[image].append((key,value))
            
    # Exercice 3
    def get(self,key):
        image=self.__function(key)%self.__taille
        for value in self.__tiroirs[image]:
            if value[0]==key:
                return value[1]
        return None
                    
            
        
                

#============= functions

def hachage(chaine):
    return sum([ord(c) for c in chaine])


#============= main

