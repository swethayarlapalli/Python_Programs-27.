#PYTHON BASIC PROGRAMS.
# 1 .program to find Area of a circle
def findArea(r):
    PI = 3.142
    return PI * (r * r);
print("Area is %.6f" % findArea(4));
# 2.program to add two numbers
num1 = 15
num2 = 12
sum = num1 + num2
print("Sum of", num1, "and", num2, "is", sum)
# 3.program to find the maximum of two numbers
def maximum(a, b):
    if a >= b:
        return a
    else:
        return b
a = 2
b = 4
print(maximum(a, b))
# 4.program to find factorial of given number
def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)
num = 5
print("Factorial of", num, "is", factorial(num))
# 5. program to find simple interest for given principal amount, time and rate of interest.
def simple_interest(p, t, r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is', r)
    si = (p * t * r) / 100
    print('The Simple Interest is', si)
    return si
simple_interest(8, 6, 8)
# 6.program to find compound interest for given values.
def compound_interest(principal, rate, time):
    Amount = principal * (pow((1 + rate / 100), time))
    CI = Amount - principal
    print("Compound interest is", CI)
compound_interest(10000, 10.25, 5)
#7.program to check whether the given number is armstrong or not without using power function
n = 153
s = n
b = len(str(n))
sum1 = 0
while n != 0:
    r = n % 10
    sum1 = sum1 + (r ** b)
    n = n // 10
if s == sum1:
    print("The given number", s, "is armstrong number")
else:
    print("The given number", s, "is not armstrong number")
num = 51
if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
# 8.Program to find Function for nth Fibonacci number
def Fibonacci(n):
    if n <= 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)
print(Fibonacci(10))
# 9.Program to print ASCII Value of Character
c = 'g'
print("The ASCII value of '" + c + "' is", ord(c))
# 10.Program to find sum of square of first n natural numbers
def squaresum(n):
    sm = 0
    for i in range(1, n + 1):
        sm = sm + (i * i)
    return sm
n = 4
print(squaresum(n))
#11. program to find maximum in arr[] of size n
def largest(arr, n):
    max = arr[0]
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max
arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr, n)
print("Largest in given array ", Ans)
#12. Program to swap first and last element of a list
def swapList(newList):
    size = len(newList)
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
    return newList
newList = [12, 35, 9, 56, 24]
print(swapList(newList))
# 13.Program to swap elements at given positions
def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3
print(swapPositions(List, pos1 - 1, pos2 - 1))
#14.Program to Reversing a list using slicing technique
def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst
lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))
# 15.Program to add two matrices using nested loop
X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
Y = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
for r in result:
    print(r)
# 16.Program for function which return reverse of a string
def isPalindrome(s):
    return s == s[::-1]
s = "malayalam"
ans = isPalindrome(s)
if ans:
    print("Yes")
else:
    print("No")
#17. Program to demonstrate working of Extract Unique values dictionary values
test_dict = {'gfg': [5, 6, 7, 8],
             'is': [10, 11, 7, 5],
             'best': [6, 12, 10, 8],
             'for': [1, 2, 5]}
print("The original dictionary is : " + str(test_dict))
res = list(sorted({ele for val in test_dict.values() for ele in val}))
print("The unique values list is : " + str(res))
#18. Program to find size of a tuple
import sys
Tuple1 = ("A", 1, "B", 2, "C", 3)
Tuple2 = ("Geek1", "Swetha", "Geek2", "Mahitha", "Geek3", "Bhavitha")
Tuple3 = ((1, "Lion"), (2, "Tiger"), (3, "Fox"), (4, "Wolf"))
print("Size of Tuple1: " + str(sys.getsizeof(Tuple1)) + "bytes")
print("Size of Tuple2: " + str(sys.getsizeof(Tuple2)) + "bytes")
print("Size of Tuple3: " + str(sys.getsizeof(Tuple3)) + "bytes")
#19.Program to find Maximum and Minimum K elements in Tuple
test_tup = (5, 20, 3, 7, 6, 8)
print("The original tuple is : " + str(test_tup))
K = 2
res = []
test_tup = list(sorted(test_tup))
for idx, val in enumerate(test_tup):
    if idx < K or idx >= len(test_tup) - K:
        res.append(val)
res = tuple(res)
print("The extracted values : " + str(res))
# 20.Program to find Binary Search Using bisect
import bisect
def binary_search_bisect(arr, x):
    i = bisect.bisect_left(arr, x)
    if i != len(arr) and arr[i] == x:
        return i
    else:
        return -1
arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search_bisect(arr, x)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
# 21.Program for Insertion Sort
def insertionSort(arr):
    n = len(arr)
    if n <= 1:
        return
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print(arr)
# 22. Program for quick sort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)
arr = [1, 7, 4, 1, 10, 9, -2]
sorted_arr = quicksort(arr)
print("Sorted Array in Ascending Order:")
print(sorted_arr)
#23.Program for Bubble Sort
def bubblesort(elements):
    swapped = False
    for n in range(len(elements) - 1, 0, -1):
        for i in range(n):
            if elements[i] > elements[i + 1]:
                swapped = True
                elements[i], elements[i + 1] = elements[i + 1], elements[i]
        if not swapped:
            return
elements = [39, 12, 18, 85, 72, 10, 2, 18]
print("Unsorted list is,")
print(elements)
bubblesort(elements)
print("Sorted Array is, ")
print(elements)
#24.Program For Merge Sort
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
def mergeSort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Given array is")
for i in range(n):
    print("%d" % arr[i], end=" ")
mergeSort(arr, 0, n - 1)
print("\n\nSorted array is")
for i in range(n):
    print("%d" % arr[i], end=" ")
#25.Program for Current time – Using date time object
from datetime import datetime
now_method = datetime.now()
currentTime = now_method.strftime("%H:%M:%S")
print("Current Time =", currentTime)
#26 Program to find yesterday, today and tomorrow
from datetime import datetime, timedelta
presentday = datetime.now()
yesterday = presentday - timedelta(1)
tomorrow = presentday + timedelta(1)
print("Yesterday = ", yesterday.strftime('%d-%m-%Y'))
print("Today = ", presentday.strftime('%d-%m-%Y'))
print("Tomorrow = ", tomorrow.strftime('%d-%m-%Y'))
#27.Program for Tower of Hanoi
def TowerOfHanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    TowerOfHanoi(n - 1, source, auxiliary, destination)
    print("Move disk", n, "from source", source, "to destination", destination)
    TowerOfHanoi(n - 1, auxiliary, destination, source)
n = 4
TowerOfHanoi(n, 'A', 'B', 'C')
####THANK YOU

