from math import *

#============= class

# Exercice 1
class Fraction:
    
    def __init__(self,n,d):
        """Initializes the fraction object with numerator and denominator"""
        self.num=n
        self.denum=d
    def printlafractionstp(self):
        """Prints the fraction"""
        print(str(self.num)+"/"+str(self.denum))
    def lachainedelafraction(self):
        """Returns the fraction as a string"""
        return(str(self.num)+"/"+str(self.denum))
    
    # Exercice 2
    def add(self,frac):
        """x.add(y) adds the fraction y to the fraction x"""
        return(Fraction(self.num*frac.denum+self.denum*frac.num,self.denum*frac.denum))
    def mult(self,frac):
        """x.mult(y) multiplies the fraction y to the fraction x"""
        return(Fraction(self.num*frac.num,self.denum*frac.denum))
    def simplify(self):
        """Simplifies the fraction"""
        return(Fraction(self.num//gcd(self.num,self.denum),self.denum//gcd(self.num,self.denum)))
    def isEqual(self,frac):
        """Returns if the two fractions represent the same number or not"""
        (a,b)=(self.simplify(),frac.simplify())
        return(a.num==b.num and a.denum==b.denum)

# Exercice 5
class Polynomial:
    
    def __init__(self,L):
        "Initializes the polynomial object with a list of its coefficients"
        self.coeff=L
    def printezlepolynomesvp(self):
        "Prints the polynomial in a usual form"
        L=self.coeff
        if not OUESTLEPREMIERPASZERO(L)[0]:
            print("0")
        else:
            p=OUESTLEPREMIERPASZERO(L)[1]
            chaîne=""
            n=len(L)
            for i in range(n-1-p):
                if L[n-1-i]!=0:
                    if L[n-1-i]==1:
                        if n-1-i==1:
                            chaîne+="X + "
                        else:
                            chaîne+="X**{} + ".format(n-1-i)
                    else:
                        if n-1-i==1:
                            chaîne+="{}*X + ".format(L[n-1-i])
                        else:
                            chaîne+="{}*X**{} + ".format(L[n-1-i],n-1-i)
            if p==0:
                chaîne+="{}".format(L[p])
            elif p==1:
                if L[p]==1:
                    chaîne+="X".format(p)
                else:
                    chaîne+="{}*X".format(L[p],p)
            else:
                if L[p]==1:
                    chaîne+="X**{}".format(p)
                else:
                    chaîne+="{}*X**{}".format(L[p],p)
            print(chaîne)
        
    # Exercice 6
    def add(self,pol2):
        """P1.add(P2) adds the polynomial P2 to the polynomial P1"""
        L1=self.coeff
        L2=pol2.coeff
        n1=len(L1)
        n2=len(L2)
        n=max(n1,n2)
        L=[]
        for i in range(n):
            L.append(L1[i]+L2[i])
        if n1==n:
            for j in range(n+1,n2):
                L.append(L2[j])
        else:
            for j in range(n+1,n1):
                L.append(L1[j])
        return(Polynomial(L))
    def deriv(self):
        """Derivates the polynomial"""
        L=self.coeff
        Lf=[]
        for i in range(1,len(L)):
            Lf.append(i*L[i])
        return(Polynomial(Lf))
    def integrate(self,cste):
        """P.integrate(C) integrate the polynomial with the constant term equal to C"""
        L=self.coeff
        Lf=[cste]
        for i in range(len(L)):
            Lf.append((1/(i+1))*L[i])
        return(Polynomial(Lf))
    
#============= functions

# Exercice 3
def nombreharmonique(n):
    """Calcule le nième nombre harmonique"""
    x=Fraction(0,1)
    for i in range(1,n+1):
        x=x.add(Fraction(1,i))
    return x.simplify()

# Exercice 4
def formuledeLeibniz(n):
    """"Calcule le nième terme de la formule de Leibniz"""
    x=Fraction(0,1)
    for i in range(0,n):
        x=x.add(Fraction((-1)**i,2*i+1))
    return x.simplify()

# Exercice 5
def OUESTLEPREMIERPASZERO(L):
    """Permet de trouver le premier coefficient non nul pour un polynôme à partir de sa liste de coefficients"""
    i=0
    while i<len(L):
        if L[i]!=0:
            return((True,i))
        else:
            i+=1
    return ((False,42))

#============= main

if __name__== "__main__":
    
    # Exercice 1
    frac_1 = Fraction(2,3)
    frac_1.printlafractionstp()
    
    # Exercice 2
    frac_2 = Fraction(7,4)
    frac_1.add(frac_2).printlafractionstp()
    frac_1.mult(frac_2).printlafractionstp()
    frac_3= Fraction(42,1281)
    frac_3.simplify().printlafractionstp()
    assert(frac_3.mult(frac_2).add(frac_1.mult(frac_3)).isEqual(Fraction(58,732)))
    
    # Exercice 3
    for i in range(1,11):
        print(nombreharmonique(i).num/nombreharmonique(i).denum)
        nombreharmonique(i).printlafractionstp()
    print(nombreharmonique(10000).num/nombreharmonique(10000).denum)
    nombreharmonique(10000).printlafractionstp()
    
    # Exercice 4
    print(formuledeLeibniz(10000).num/formuledeLeibniz(10000).denum)
    formuledeLeibniz(10000).printlafractionstp()
    
    # Exercice 5
    P1= Polynomial([1,2,3,4,5,1,2,42])
    P2= Polynomial([0,2,0,4,5,0,2,42])
    P3= Polynomial([0,0,0,0,0])
    P4= Polynomial([0,0,1,0,0])
    P1.printezlepolynomesvp()
    P2.printezlepolynomesvp()
    P3.printezlepolynomesvp()
    P4.printezlepolynomesvp()
    
    # Exercice 6
    P1.add(P2).printezlepolynomesvp()
    P1.deriv().printezlepolynomesvp()
    P1.integrate(pi).printezlepolynomesvp()
    
    
    