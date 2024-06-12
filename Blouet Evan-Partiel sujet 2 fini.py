from math import *

#============= class

# Exercice 5
class Chiffreur:
    
    def __init__(self, description):
        """Initiates a chiffreur object which represents an operation (can be multiple transformations) by its description"""
        suiteop=description.split(";")
        self.op=suiteop
        self.nbtransformelem=len(suiteop)
        
    def evaluate(self,a_chiffrer):
        """Evaluates a Chiffreur with the string 'a_chiffrer' """
        for transformelem in self.op:
            a_chiffrer=chiffre(a_chiffrer,transformelem)
        return a_chiffrer
            
    def simplify(self):
        """ Simplify some transformations inside the Chiffreur object"""
        suiteop=self.op
        newop=[]
        j=0
        for i in range(self.nbtransformelem):
            if newop==[] or newop[j-1][:3]!=suiteop[i][:3]:
                newop.append(suiteop[i])
                j+=1
            else:
                if suiteop[i][:3]=="MIR":
                    newop.pop()
                    j-=1
                elif suiteop[i][:3] in ["ROT","TRA"]:
                    newop[j-1]=newop[j-1][:3]+str(int(newop[j-1][3:])+int(suiteop[i][3:]))
        description=''
        for mot in newop:
            description+=mot+";"
        return Chiffreur(description[:-1])

#============= functions
# Exercice 1
def rot(string,n):
    """Rotates all letters contained in the string 'string' by 'n' letters, only with ASCII caracters with an ord between 32(SPACE) and 126(~) included"""
    mottransforme=''
    for c in string:
        if ord(c)<32 or ord(c)>126:
            print('Cette fonction ne porte que sur les caractères ASCII entre 32 et 126 compris...')
        mottransforme+=chr((ord(c)-32+n)%95+32)
    return mottransforme

# Exercice 2
def miroir(string):
    """Miroir the string 'string', such that for example, the caracter 'SPACE' become '~', ..."""
    mottransforme=''
    for c in string:
        if ord(c)<32 or ord(c)>126:
             print('Cette fonction ne porte que sur les caractères ASCII entre 32 et 126 compris...')
        mottransforme+=(chr(94-(ord(c)-32)+32))
    return mottransforme

# Exercice 3
def translation(string,n):
    """Translates the string by n letters: the i-th letter is now in position i+n"""
    mottransforme=''
    N=len(string)
    for i in range(N):
        mottransforme+=string[(i+n)%N]
    return mottransforme

# Exercice 4
def chiffre(s1,s2):
    """Encoding a string "s1" by another string "s2" representing a sequence of elementary transformations"""
    for opelementaire in s2.split(";"):
        if opelementaire[:3]=='ROT':
            s1=rot(s1,int(opelementaire[3:]))
        elif opelementaire[:3]=='MIR':
            s1=miroir(s1)
        elif opelementaire[:3]=='TRA':
            s1=translation(s1,int(opelementaire[3:]))
        else:
            print("Y'a un problème dans la forme de l'opérateur de chiffrement, opération "+opelementaire+" ignorée")
    return s1

#============= main

if __name__== "__main__":
    
    # Exercice 1
    assert(rot("La licorne n'a pas voulu regarder le lac",10)=="Vk*vsmy|xo*x1k*zk}*!y v *|oqk|no|*vo*vkm")
    print(rot('Uwu',51))
    assert(rot('Uwu',51+666*95)==rot('Uwu',51))
    
    # Exercice 2
    assert(miroir("La licorne n'a pas voulu regarder le lac")=="R=~25;/,09~0w=~.=+~(/)2)~,97=,:9,~29~2=;")
    print(miroir("Uwu"))
    assert(miroir(miroir("Uwu"))=="Uwu")
    
    # Exercice 3
    assert(translation("La licorne n'a pas voulu regarder le lac",12)=="'a pas voulu regarder le lacLa licorne n")
    print(translation("amongus",4))
    assert(translation("amongus",2)==translation("amongus",2+7*69))
    
    # Exercice 4
    assert(chiffre("La licorne n'a pas voulu regarder le lac","ROT10;TRA5;MIR")=='1%"&/t&m3t$3!t}%~(~t"/-3"0/"t(/t(31H3t(+')
    print(chiffre("Kawaii","ROT4;MIR;TRA2;ROT2;MIR"))
    
    # Exercice 5
    assert(Chiffreur("MIR").evaluate("La licorne n'a pas voulu regarder le lac")=="R=~25;/,09~0w=~.=+~(/)2)~,97=,:9,~29~2=;")
    descriptionchiffreur="MIR;ROT22;TRA666;MIR;MIR;ROT13;ROT32;TRA1;TRA2;TRA3;MIR"
    chiff=Chiffreur(descriptionchiffreur)
    print(chiff.op,chiff.nbtransformelem)
    
    # Exercice 6
    chiffsimp=chiff.simplify()
    print(chiffsimp.op,chiffsimp.nbtransformelem)
    
    