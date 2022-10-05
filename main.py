'''
RECURSIVE ALGORITHMS
'''

#Calculate Factorials

#Iterative
def iterative_factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact
print(f"iterative factorial = {iterative_factorial(5)}")

#Recursive
def recur_factorial(n):
    if n == 1:
        return n
    else:
        temp = recur_factorial(n-1)
        temp = temp * n
    return temp
print(f"recursive factorial = {recur_factorial(5)}")

#short recursive
def recur_factorial_2(n):
    if n == 1: return n
    else: return n * recur_factorial_2(n-1)
print(f"iterative factorial (2) = {recur_factorial_2(5)}")