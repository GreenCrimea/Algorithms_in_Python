from math import factorial
import numpy as np


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

#iterative
def b_search(arr, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            return mid
    return -1

arr = [3, 7, 15, 18, 23, 27, 35, 39, 56, 67, 74, 83, 91]
target = 83

#print(b_search(arr, 0, len(arr) - 1, target) + 1)

#recursive
def b_search_recur(arr, start, end, target):
    if end >= start:
        mid = (start + end - 1) // 2
        if arr[mid] < target:
            return b_search_recur(arr, mid + 1, end, target)
        elif arr[mid] > target:
            return b_search_recur(arr, start, mid - 1, target)
        else:
            return mid
    else:
        return -1

#print(b_search_recur(arr, 0, len(arr) - 1, target) + 1)


#bubble sort

def bubble_sort(arr):
    iterations = 0
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            iterations += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr, iterations

arr = [67, 46, 86, 32, 57, 21, 46, 35, 56, 98, 31, 58, 42]
#print(bubble_sort(arr))


#insertion sort

def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr

#print(insertion_sort(arr))


#linked list

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    
    def traversal(self):
        first = self.head
        while first:
            print(first.data)
            first = first.next

    def insert_new_header(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head 
        self.head = new_node

    def search(self, x):
        temp = self.head
        while temp is not None:
            if temp.data == x:
                return True
            else:
                return False

    def delete(self, data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next
            prev.next = temp.next


family = LinkedList()
family.head = Node("Bob")
wife = Node("Amy")
first_kid = Node("Max")
second_kid = Node("Jenny")

family.head.next = wife
wife.next = first_kid
first_kid.next = second_kid

family.insert_new_header("Dave")
family.delete("Bob")
#family.traversal()


'''
divide and conquer
'''

#merge sort

class Solution(object):
    
    def sort_array(self, arr):
        mid = len(arr) // 2
        left = sorted(arr[:mid])
        right = sorted(arr[mid:])
        c = []
        while min(len(left), len(right)) > 0:
            if left[0] > right[0]:
                insert = right.pop(0)
                c.append(insert)
            elif left[0] <= right[0]:
                insert = left.pop(0)
                c.append(insert)
        if len(left) > 0:
            for i in left:
                c.append(i)
        if len(right) > 0:
            for i in right:
                c.append(i)
        return c

solution = Solution()
arr = [13, 43, 45, 35, 46, 35, 46, 44, 52, 35, 55, 44, 56, 72, 52, 34, 56 , 37, 46, 24, 76, 47]
#print(solution.sort_array(arr))


#matrix multiplication

x = [[1, 2],
     [2, 3]]

y = [[2, 3],
     [3, 4]]

result = [[0, 0],
          [0, 0]]

def matrix_multiply(x, y, result):
    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(y)):
                result[i][j] += x[i][k] * y[k][j]
    return result

#print(matrix_multiply(x, y, result))


#strassen

x = np.array([[1, 2], [2, 3]])
y = np.array([[2, 3], [3, 4]])

#iterative
def strassen_iter(x, y):
    a, b, c, d = x[0, 0], x[0, 1], x[1, 0], x[1, 1]
    e, f, g, h = y[0, 0], y[0, 1], y[1, 0], y[1, 1]

    p1 = a * (f - h)
    p2 = (a + b) * h
    p3 = (c + d) * e
    p4 = d * (g - e)
    p5 = (a + d) * (e + h)
    p6 = (b - d) * (g + h)
    p7 = (a - c) * (e + f)

    c1 = (p5 + p4 - p2 + p6)
    c2 = (p1 + p2)
    c3 = (p3 + p4)
    c4 = (p1 + p5 - p3 - p7)

    return np.array([[c1, c2], [c3, c4]])

#print(strassen_iter(x, y))


'''
greedy algorithms
'''