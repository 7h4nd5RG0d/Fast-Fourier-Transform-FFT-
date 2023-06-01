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
    n=list(map(int,input("Enter the coeffecients of polynomial 1 in increasing order of degree: ").strip().split()))
    m=list(map(int,input("Enter the coeffecients of polynomial 2 in increasing order of degree: ").strip().split()))

    #Appending 0 so that polynomial is represnted in powers of 2.
    a=len(n)
    b=len(m)
    c=(a-1)*(b-1)+1
    while math.log2(c)%1!=0:
        c=c+1
    while a<c:
        a=a+1
        n.append(0)
    while b<c:
        b=b+1
        m.append(0)

    ######################################################################################################
    print("The coeffecients of the entered polynomial 1 with number of terms in power of 2: ",n)
    print("The coeffecients of the entered polynomial 2 with number of terms in power of 2: ",m)

    y=FFT(n)  #calling the forward transform
    z=FFT(n)  #calling the forward transform
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

    j=0 # this is a precision function as roots of unity can be irrational also
    for img in z:
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
        z[j]=img
        j=j+1
    ########################################################################################################
    print("The forward transform of the entered polynomial 1: ",y) 
    print("The forward transform of the entered polynomial 2: ",z) 


    ########################################################################################################
    res=[] #stores the poinwise multiplication
    for j in range(len(z)):
        res.append(y[j]*z[j])
    #######################################################################################################
    j=0 #this is a precision function as roots of unity can be irrational also
    for img in res:
        e=img.real
        f=img.imag
        if e==0:
            f=round(f)
        if(f==0):
            e=round(e)
        if e!=0 and f!=0:
            e=round(e,3)
            f=round(f,3)
        img=complex(e,f)
        res[j]=img
        j=j+1
    ##################################################################################################
    print("The pointwise multiplication of the 2 entered polynomials",res)  #pointwise multiplcation of the y-coordinates,the x-coordinates are the roots of unity
    ###################################################################################################
