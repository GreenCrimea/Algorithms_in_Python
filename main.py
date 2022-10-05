from math import factorial

'''
RECURSIVE ALGORITHMS
'''

#Calculate Factorials

#iterative
def iterative_factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact
#print(f"iterative factorial = {iterative_factorial(5)}")

#recursive
def recur_factorial(n):
    if n == 1:
        return n
    else:
        temp = recur_factorial(n-1)
        temp = temp * n
    return temp
#print(f"recursive factorial = {recur_factorial(5)}")

#short recursive
def recur_factorial_2(n):
    if n == 1: return n
    else: return n * recur_factorial_2(n-1)
#print(f"iterative factorial (2) = {recur_factorial_2(5)}")


#Permutations

#iterative
def permutations(str):
    for p in range(factorial(len(str))):
        print("".join(str))
        i = len(str) - 1
        while i > 0 and str[i - 1] > str[i]:
            i -= 1
        str[i:] = reversed(str[i:])
        if i > 0:
            q = i
            while str[i - 1] > str[q]:
                q += 1
            temp = str[i - 1]
            str[i - 1] = str[q]
            str[q] = temp
s = "abc"
s = list(s)
permutations(s)

#recursive
def permute(string, pocket=""):
    if len(string) == 0:
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[0:i]
            back = string[i+1:]
            together = front + back
            permute(together, letter + pocket)
#print(permute("ABCDEF", ""))