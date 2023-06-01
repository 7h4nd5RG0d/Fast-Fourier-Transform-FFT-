# Fast-Fourier-Transform-(FFT)
import math
import cmath 
import numpy as np
from cmath import exp, pi

#################################################################################
def nthRootsOfUnity(n): #Calculates nth root of unity
    theta = math.pi * 2 / n
    real = math.cos(theta)
    img = math.sin(theta)
    z=complex(real,img) # e^j(theta) =cos(theta)+ j sin(theta)
    return z

################################################################################
def FFT(polynomial): # The forward transform
    
    n=len(polynomial)
    if n==1:
        return polynomial
    
    w=nthRootsOfUnity(n)
    pe=[] #stores the even powers of the polynomial
    for j in range(0,int(n/2)):
        {
            pe.append(polynomial[2*j])
        }
    po=[] #stores the odd powers of the polynomial
    for j in range(0,int(n/2)):
        {
            po.append(polynomial[2*j+1])
        }
    #recursively traverse till you get degree-0 polynomials
    ye=FFT(pe) 
    yo=FFT(po)

    y=[0]*n #initialising the resultant list
    
    #the main thing in this algo that saves time: 
    #we have basically just used the property 'that roots of unity change asymmetrically with a period of pi'
    for j in range(0,int(n/2)):
        y[j]=ye[j]+yo[j]*(pow(w,j))
        y[j+int(n/2)]=ye[j]-yo[j]*(pow(w,j))
    return(y) #return the result

#########################################################################################################
if __name__=='__main__':
    n=[]
    n=list(map(int,input("Enter the coeffecients in increasing order of degree: ").strip().split()))

    #Appending 0 so that polynomial is represnted in powers of 2.
    a=len(n)
    while math.log2(a)%1!=0:
        n.append(0) 
        a=a+1

    ######################################################################################################
    print("The coeffecients of the entered polynomial with number of terms in power of 2: ",n)
    y=FFT(n)  #calling the forward transform

    #######################################################################################################
    j=0 # this is a precision function as roots of unity can be irrational also
    for img in y:
        e=img.real
        f=img.imag
        if e==0:
            f=round(f)
        if(f==0):
            e=round(e)
        if e!=0 and f!=0:
            e=round(e,2)
            f=round(f,2)
        img=complex(e,f)
        y[j]=img
        j=j+1
    ########################################################################################################
    print("The forward transform of the entered polynomial: ",y) 
