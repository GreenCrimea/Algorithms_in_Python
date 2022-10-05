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
#permutations(s)

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
#print(permute("ABC", ""))


'''
SEARCH AND SORT
'''

#linear search

def l_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

arr = [45, 82, 19, 68, 26, 29]
target = 19

#print(l_search(arr, target) + 1)


#binary search

def b_search(arr, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            return mid
    return start

arr = [3, 7, 15, 18, 23, 27, 35, 39, 56, 67, 74, 83, 91]
target = 15

print(b_search(arr,0, len(arr) - 1, target))

