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