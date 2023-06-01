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
    if n==1: # base case
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

########################################################################################################
def IFFT(polynomial): #The function for inverse transform 
    n=len(polynomial)
    if n==1:   #base case
        return polynomial   
    w=nthRootsOfUnity1(n)  #the power of FFT. With only 2 changes in code you can transform from forward transform to its inverse
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
    ye=IFFT(pe)
    yo=IFFT(po)

    y=[0]*n

    for j in range(0,int(n/2)):
        y[j]=(ye[j]+yo[j]*(pow(w,j)))
        y[j+int(n/2)]=(ye[j]-yo[j]*(pow(w,j)))
    return(y)

###############################################################################################################
def nthRootsOfUnity1(n): # just a minor change to that of the above function. Here we will be using -(theta)
    theta = math.pi * 2 / n
    theta=(-1*theta)
    real = round(math.cos(theta),2)
    real=real
    img = round(math.sin(theta),2)
    img=img
    z=complex(real,img)
    return z
##################################################################################################################

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
    z=FFT(m)  #calling the forward transform
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
    res1=IFFT(res) # calling the inverse transform

    ##########################################################################################
    j=0 #Another precision function. The problem of irrationals sadly
    for img in res1:
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
        res1[j]=img
        j=j+1  

    ########################################################################################
    j=0  #Completing the inverse transform
    for img in res1:
        e=img.real
        e=e*1/c #This is the second change w.r.t Forward transform. We have to even divide by n(which in this case will be the determinant of the state matrix of roots of unity)
        e=round(e)
        res1[j]=e
        j=j+1

    ######################################################################################

    print("The final polynomial m*n= ",res1) #Ah...finally the result
