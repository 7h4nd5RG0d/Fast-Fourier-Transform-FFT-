# Fast-Fourier-Transform-(FFT)
Fast polynomial multiplication

# What is FFT:
FFT is an algorithm for fast polynomial multiplication.The usual polynomial multiplication takes a complexity of O(n^2) while FFT takes a complexity of O(nlogn).
The following steps illustrate FFT:-


# The forward transform:
Time Complexity = O(nlogn) where n is the degree of the polynomial 

#### PYTHON CODE:
There in FFT.py

### Explanation:
In forward transform we are finding the value of the polynomial at n points. This under usual circumstances takes O(n^2) time but we have an effecient way to do it.
### Steps:
1)Take the polynomial and split it into 2 polynomials having even and odd degree terms.  
2)Calculate the nth root of unity as we will be calculating the value of the polynomial at the nth roots of unity(it gives us totally n points as we wanted)    
3)
