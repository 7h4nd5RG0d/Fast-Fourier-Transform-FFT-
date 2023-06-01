# Fast-Fourier-Transform(FFT)
Fast polynomial multiplication **for polynmials with degree greater than 2 (degree 1 and 0 can be considered trivial for our case)**

# What is FFT:
> FFT is an algorithm for fast polynomial multiplication. The usual polynomial multiplication takes a complexity of O(n^2) while FFT takes a complexity of O(nlogn).
The following steps illustrate FFT:-


# 1)The Forward Transform:
> Time Complexity = O(nlogn) where n is the degree of the polynomial 

#### PYTHON CODE:
Forward_Transform.py

### Explanation:
> In forward transform we are finding the value of the polynomial at n points. This under usual circumstances takes O(n^2) time but we have an efficient way to do it.
### Steps:
> 1)Take the polynomial and split it into 2 polynomials having even and odd degree terms.  
> 2)Calculate the nth root of unity as we will be calculating the value of the polynomial at the nth roots of unity(it gives us totally n points as we wanted)    
> 3)Now recursively follow the above 2 steps till you get degree 0 polynomials.     

### Time complexity explanation:
> Since we are traversing down the polynomial until we get degree 0 terms this takes a time complexity of O(logn)     
If the degree of polynomial =2^n (since we deal with only degrees that are powers of 2) then to break down the polynomial to degree-0 we need (logn) steps.  
Once we have the degree-0 polynomials we have to just calculate the value at the nth roots of unity which takes 'n' computations for each root.

>  Therefore overall complexity is **O(nlogn)**

   
# 2)Point wise multiplication of the polynomials:
>Time Complexity = O(n) where n is the degree of the polynomial as we need to multiply only (n+1) points together

#### PYTHON CODE:
Pointwise_Multiplication.py

### Explanation
> Now that we have got the (n+1) points of interest of both the polynomials the question arises how to multiply them to get just a single set of n points that represents the final polynomial
> This is done through pointwise multiplication.     
>**Note:- if one of the polynomials has degree m and the other has degree n, then they give a polynomial of degree m*n on multiplication. We can state that if we have (m*n+1) distinct points, the resultant polynomial can be uniquely determined.**

# 3)The Inverse Transform:
>Time Complexity = O(nlogn) where n is the degree of the polynomial 

#### PYTHON CODE:
Inverse_Transform.py
### Steps:
> Just 2 minor changes to the Forward Transform and we get the Inverse transform.
> 1)Here we will be using the inverse of the nth roots of unity.
> 2) Finally in the last step we have to divide by 1/n which is the determinant of the DFT matrix.

# Overall Time Complexity
> The overall time complexity= O(nlogn) + O(n) + O(nlogn) = O(nlogn) <<<<<<< O(n^2) 

# The DFT matrix and its inverse:
### DFT:
![image](https://github.com/7h4nd5RG0d/Fast-Fourier-Transform-FFT-/assets/128285431/d3568da8-7b28-4cf4-8b96-836fb970d0d2)

### IDFT:
![image](https://github.com/7h4nd5RG0d/Fast-Fourier-Transform-FFT-/assets/128285431/2d3daad5-5c05-492a-8888-008362b23c76)

> Note that 1)theta to change thetanally we divide by n


# Is it really faster

>Let us take an example to compare it with the schoolbook algorithm:
>Consider m= (5 + 10x^2 + 6x^3)  and n= (1 +2x + 4x^2)


>>**Using the FFT algo gven:-**


![image](https://github.com/7h4nd5RG0d/Fast-Fourier-Transform-FFT-/assets/128285431/a1d083c0-8f5e-4176-901b-7360905630ff)

>>**Using the schoolbook algo given**
>>
![image](https://github.com/7h4nd5RG0d/Fast-Fourier-Transform-FFT-/assets/128285431/03d9d978-a5e9-40b9-b43c-f36aecd8d0e4)


>>**Wow. Just look at the difference of time there, and this is just for a degree 5 resultant polynomial. Consider the case when we use it for Dilithium and Khyber where larger polynomials.  
>>I guess that's why it is the most ingenious algorithm of all time**
