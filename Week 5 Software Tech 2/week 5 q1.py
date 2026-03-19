def sum_of_natural_numbers(n):
    if n == 1:
        return 1 # Base case
    else:
        return n + sum_of_natural_numbers(n - 1) # Recursive case
    



def sum_of_integers1(n):  
    sum1 = 0
    for x in range (0, n + 1): 
        sum1 =(sum1 + x)
    return(sum1) 



      

# RECURSIVELY CALCULATING FIBONACCI SEQUENCE (more difficult example)
# f(n) = f(n - 1) + f(n - 2)
def fibonacci(n):
    if n <= 0:
        return 0 # Base case
    elif n == 1:
        return 1 # Base case 
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) # Recursive case 
    
result = fibonacci(5)  
print(result)
result = fibonacci(7) 
print(result)
result = fibonacci(9)  
print(result)
    

def fibbonacci1(n): 
    seq = [0, 1]
    for i in range(n): 
        seq.append(seq[-1] + seq[-2]) 
    return seq[-2] 

result = fibbonacci1(5) 
print(result) 
result = fibbonacci1(7)  
print(result)
result = fibbonacci1(9)  
print(result) 

# CHALLENGE: Use recursion to calculate the factorial.
def factorial(n):

    if n == 0:
        return 1  # Base case: factorial of 0 is 1
    else:
        return n * factorial(n - 1)  # Recursive case: n! = n * (n-1)!  
    

def factorial1(n):
    result = 1
    for x in range(1, n + 1):
        result *= x
    return(result)

