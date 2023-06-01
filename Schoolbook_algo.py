import time

def multiply(A, B, m, n):
  
    prod = [0] * (m + n - 1)
      
    # Multiply two polynomials term by term
      
    # Take ever term of first polynomial
    for i in range(m):
          
        # Multiply the current term of first 
        # polynomial with every term of 
        # second polynomial.
        for j in range(n):
            prod[i + j] += A[i] * B[j]
  
    return prod
  
# A utility function to print a polynomial
def printPoly(poly, n):
  
    for i in range(n):
        print(poly[i], end = "")
        if (i != 0):
            print("x^", i, end = "")
        if (i != n - 1):
            print(" + ", end = "")
  
# Driver Code
  
# The following array represents
# polynomial 5 + 10x^2 + 6x^3
A = [5, 0, 10, 6]
  
# The following array represents 
# polynomial 1 + 2x + 4x^2
B = [1, 2, 4]
m = len(A)
n = len(B)
start=time.time() 
print("First polynomial is ")
printPoly(A, m)
print("\nSecond polynomial is ")
printPoly(B, n)
  
prod = multiply(A, B, m, n)
  
print("\nProduct polynomial is ")
printPoly(prod, m+n-1)
end=time.time()
print()
print(end-start)
