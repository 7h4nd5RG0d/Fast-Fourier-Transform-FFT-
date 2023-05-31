# Fast-Fourier-Transform-(FFT)
**import math
import cmath 
import numpy as np
from cmath import exp, pi

def nthRootsOfUnity(n): 
    theta = math.pi * 2 / n
    real = math.cos(theta)
    img = math.sin(theta)
    z=complex(real,img)
    return z

def FFT(polynomial):
    
    n=len(polynomial)
    if n==1:
        return polynomial
    
    w=nthRootsOfUnity(n)
    pe=[]
    for j in range(0,int(n/2)):
        {
            pe.append(polynomial[2*j])
        }
    po=[]
    for j in range(0,int(n/2)):
        {
            po.append(polynomial[2*j+1])
        }
    ye=FFT(pe)
    yo=FFT(po)

    y=[0]*n

    for j in range(0,int(n/2)):
        y[j]=ye[j]+yo[j]*(pow(w,j))
        y[j+int(n/2)]=ye[j]-yo[j]*(pow(w,j))
    return(y)
if __name__=='__main__':
    n=[]
    n=list(map(int,input("Enter the coeffecients in increasing order of degree: ").strip().split()))

    #Appending 0 so that polynomial is represnted in powers of 2.
    a=len(n)
    while math.log2(a)%1!=0:
        n.append(0)
        a=a+1
    print(n)
    y=FFT(n)
    print(y)**

