#=========== functions

# ouverture et traitement des données
d=open("C:/Users/evanb/Downloads/mots.sansaccent.txt","r").readlines()
L1=[]
for mot in d:
    L1.append([len(mot)-1,mot[0:len(mot)-1]])
L2=[]
for j in range(1,26):
    Lj=[]
    for mot in L1:
        if mot[0]==j:
            Lj.append(mot[1])
    L2.append(Lj)
    
#L2 contient alors tous les mots triés par nombre de lettres

# Exercice 2

def ok(mot, tirage):
    """ ok(Mot,Tirage) test si le mot "Mot" est réalisable avec le tirage "Tirage" """
    if mot=='':
        return True
    if tirage==[]:
        return False
    for i in range(len(tirage)):
        if mot[0]==tirage[i]:
            l=[]
            for j in range(0,i):
                l.append(tirage[j])
            for j in range(i+1,len(tirage)):
                l.append(tirage[j])
            return ok(mot[1:len(mot)],l)
    return False

                
def biggestmot(tirage):
    """ biggestmot(Tirage) renvoit un des mots les plus longs possibles avec le tirage  "Tirage"
    on commence par regarder les mots à partir du nombre de lettres du tirage.
    on diminue le nombre de lettres recherchées s'il y en a pas
    dès qu'on en trouve 1 accepté, on le renvoit """
    n=len(tirage)
    for i in range(n-1):
        truc=L2[n-i]
        for mot in truc:
            if ok(mot,tirage):
                return mot
    return ("ya pas de mot en fait")



# Exercice3

# On définit certaines listes regroupant les lettres par nombre de point.
# On aurait pu utiliser switch mais trop tard+on a pas encore le droit d'utiliser des dictionnaires
l1=["a","e","i","l","n","o","r","s","t","u"]
l2=["d","g","m"]
l3=["b","c","p"]
l4=["f","h","v"]
l5=["j","q"]
l6=["k","w","x","y","z"]

def point(mot):
    """" point(Mot) renvoie le score du mot "Mot" """
    if len(mot)==0:
        return 0
    lettre=mot[0]
    if lettre in l1:
        return 1+point(mot[1:len(mot)])
    elif lettre in l2:
        return 2+point(mot[1:len(mot)])
    elif lettre in l3:
        return 3+point(mot[1:len(mot)])
    elif lettre in l4:
        return 4+point(mot[1:len(mot)])
    elif lettre in l5:
        return 8+point(mot[1:len(mot)])
    else:
        return 10+point(mot[1:len(mot)])

# motaccepte(Tirage) renvoit la liste des mots acceptés obtenable avec le tirage "Tirage"
def motaccepte(tirage):
    """motaccepte(Tirage) renvoit la liste des mots acceptés obtenable avec le tirage "Tirage" """
    L=[]
    n=len(tirage)
    for i in range(n-1):
        truc=L2[n-i]
        for mot in truc:
            if ok(mot,tirage):
                L.append(mot)
    return L
    
def max_score(tirage):
    """ max_score(Tirage) renvoie un couple formé du meilleur mot formable avec le tirage "Tirage" et de son score"""
    accepte=motaccepte(tirage)
    if len(accepte)==0:
        return ("NaN",0)
    (bestmot,bestpoint)=(accepte[0],point(accepte[0]))
    for i in range(len(accepte)):
        mot=accepte[i]
        pt=point(mot)
        if pt>bestpoint:
            (bestmot,bestpoint)=(mot,pt)
    return (bestmot,bestpoint)

# Exercice 4

def max_score_joker(tirage):
    """max_score_joker(Tirage) renvoie un couple formé du meilleur mot formable avec le tirage "Tirage" et de son score.
     pour prendre en compte le joker, on teste les mots formables avec celui-ci en retirant les points de la lettre qu'il remplace
     mais aussi les mots formables sans le joker (auquel cas on ne retire aucun point)"""
    if "?" in tirage:
        tincomplet=[]
        for j in range(len(tirage)):
            if tirage[j]!="?":
                tincomplet.append(tirage[j])
        alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        malus=[]
        T=[]
        for lettre in alphabet:
            aaa=tincomplet.copy()
            aaa.append(lettre)
            T.append(aaa)
            if lettre in l1:
                malus.append(1)
            elif lettre in l2:
                malus.append(2)
            elif lettre in l3:
                malus.append(3)
            elif lettre in l4:
                malus.append(4)
            elif lettre in l5:
                malus.append(8)
            else: 
                malus.append(10)
        M=[]
        S=[]
        for i in range(len(T)):
            (a,b)=max_score(T[i])
            M.append(a)
            S.append(b-malus[i])
        (a,b)=max_score(tincomplet)
        M.append(a)
        S.append(b)
        x=max(S)
        for i in range(len(S)):
            if S[i]==x:
                return (M[i],S[i])
    else:
        return max_score(tirage)
    
#========== main

print(L2[0])

# Exercice 2
print(ok("bonjour",["b","n","j","u","o","r","a"]))
print(ok("bonjour",["b","n","j","u","o","r","o"]))
print(biggestmot(['a', 'r', 'b', 'g', 'e', 's', 'c', 'j']))

# Exercice 3
print(point("bonjour"))
print(point("baguette"))
print(motaccepte(['a', 'r', 'b', 'g', 'e', 's', 'c', 'j']))
print(max_score(['a', 'r', 'b', 'g', 'e', 's', 'c', 'j']))

# Exercice 4
print(max_score('zxcvrrt'))
print(max_score_joker('zxcvrrt?'))
print(max_score_joker('zxcvrrta'))
