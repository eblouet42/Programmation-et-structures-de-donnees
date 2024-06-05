from math import *
from random import *

#============= class

# Exercice 1
class polymod:
    def __init__(self,q,n,coeff):
        self.q=q
        self.n=n
        newcoeff=[0 for i in range(n)]
        for k in range(len(coeff)):
            newcoeff[k%n]=(newcoeff[k%n]+((-1)**(k//n)*coeff[k]))%q
        self.coeff=newcoeff
        
    def printezlepolynomesvp(self):
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
                            chaîne+="{}X + ".format(L[n-1-i])
                        else:
                            chaîne+="{}X**{} + ".format(L[n-1-i],n-1-i)
            if p==0:
                chaîne+="{}".format(L[p])
            elif p==1:
                if L[p]==1:
                    chaîne+="X".format(p)
                else:
                    chaîne+="{}X".format(L[p],p)
            else:
                if L[p]==1:
                    chaîne+="X**{}".format(p)
                else:
                    chaîne+="{}X**{}".format(L[p],p)
            print(chaîne)
    
    # Exercice 2
    def add(self,poly):
        if self.q!=poly.q or self.n!=poly.n:
            print("euh ba c pas les mêmes n ou q")
        else:
            addcoeff=[self.coeff[i]+poly.coeff[i] for i in range(self.n)]
            return polymod(self.q,self.n,addcoeff)
    
    # Exercice 3
    def mul(self,poly):
        if self.q!=poly.q or self.n!=poly.n:
            print("euh ba c pas les mêmes n ou q")
        else:
            mulcoeff=[0 for i in range(self.n)]
            for i in range(self.n):
                for j in range(poly.n):
                    mulcoeff[(i+j)%self.n]=(mulcoeff[(i+j)%self.n]+(self.coeff[i]*poly.coeff[j]))%self.q
            return polymod(self.q,self.n,mulcoeff)
    # Exercice 4
    def scalar(self,c):
        scalcoeff=[(round(c*self.coeff[i]))%self.q for i in range(self.n)]
        return polymod(self.q,self.n,scalcoeff)
    def rescale(self,r):
        return polymod(r,self.n,self.coeff)
    def fscalar(self,r,alpha):
        return self.scalar(alpha).rescale(r) 

#============= functions

# Exercice 1
def OUESTLEPREMIERPASZERO(L):
    """Permet de trouver le premier coefficient non nul pour un polynôme à partir de sa liste de coefficients"""
    i=0
    while i<len(L):
        if L[i]!=0:
            return((True,i))
        else:
            i+=1
    return ((False,42))

# Exercice 5
def gen_uniform_random(q,n,a,b):
    randomcoeff=[randint(ceil(a),floor(b)+1) for i in range(n)]
    return polymod(q,n,randomcoeff)

# Exercice 6
def chiffrement(pk,p):
    (b,a)=pk
    q=b.q
    n=b.n
    t=p.q
    delta=q/t
    sp=p.fscalar(q,delta)
    u=gen_uniform_random(q,n,0,1)
    e1=gen_uniform_random(q,n,-1,1)
    c1=b.mul(u).add(e1).add(sp)
    e2=gen_uniform_random(q,n,-1,1)
    c2=a.mul(u).add(e2)
    return(c1,c2)

def dechiffrement(sk,c,t):
    (c1,c2)=c
    q=c1.q
    p=(c1.add(c2.mul(sk))).fscalar(t,t/q)
    return p

#============= main

if __name__== "__main__":
        
    # Exercice 1
    q=4
    n=4
    coeff1=[0,1,2,3,4,5]
    P1=polymod(q,n,coeff1)
    P1.printezlepolynomesvp()
    # Exercice 2
    coeff2=[1,0,-3,0,-666,0,0,0,0,69]
    P2=polymod(q,n,coeff2)
    P2.printezlepolynomesvp()
    PS=P1.add(P2)
    PS.printezlepolynomesvp()
    
    # Exercice 3
    PM=P1.mul(P2)
    PM.printezlepolynomesvp()
    
    # Exercice 4
    P2scalar=P2.scalar(3.4)
    P2scalar.printezlepolynomesvp()
    P2rescale=P2.rescale(3)
    P2rescale.printezlepolynomesvp()
    P2fscalar=P2.fscalar(3,3.4)
    P2fscalar.printezlepolynomesvp()
    
    # Exercice 5
    random1=gen_uniform_random(10,6,42,666)
    random2=gen_uniform_random(20,6,42,666)
    random1.printezlepolynomesvp()
    random2.printezlepolynomesvp()
    random1.mul(random2.rescale(random1.q)).printezlepolynomesvp()
    
    # Exercice 6
    grosq=97
    grosn=43
    grost=127
    coeffgrosP=[(-1)**i * i for i in range(1000)]
    grosP=polymod(grosq,grosn,coeffgrosP)
    grosP.printezlepolynomesvp()
    sk=gen_uniform_random(grosq,grosn,0,1)
    a=gen_uniform_random(grosq,grosn,0,grosq-1)
    e=gen_uniform_random(grosq,grosn,-1,1)
    moins1=[0 for i in range(grosn)]
    moins1[0]=-1
    Polmoins1=polymod(grosq,grosn,moins1)
    b=Polmoins1.mul(a.mul(sk).add(e))
    pk=(polymod(grosq,grosn,a.coeff),polymod(grosq,grosn,b.coeff))
    chiffré=chiffrement(pk,grosP)
    chiffré[0].printezlepolynomesvp()
    chiffré[1].printezlepolynomesvp()
    
    # Exercice 7
    déchiffré=dechiffrement(sk,chiffré,grost)
    déchiffré.printezlepolynomesvp()
    assert(grosP.coeff==déchiffré.coeff)
    #ca marche po