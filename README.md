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

