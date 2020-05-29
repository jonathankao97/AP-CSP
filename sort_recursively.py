import pyinputplus as pyip
from random import randrange
from time import time


def bubble_sort(list, end):
    if end == 0:
        return list
    for i in range(end-1):
        if list[i+1] < list[i]:
            temp = list[i+1]
            list[i+1] = list[i]
            list[i] = temp
    return bubble_sort(list, end-1)


def quick_sort(list, left, right):
    def swap(list, i1, i2):
        temp = list[i2]
        list[i2] = list[i1]
        list[i1] = temp
    if left >= right:
        return list
    pivot = list[right]
    index = left
    for i in range(left, right):
        if list[i] < pivot:
            swap(list, index, i)
            index += 1
    swap(list, right, index)
    quick_sort(list, left, index-1)
    quick_sort(list, index+1, right)
    return list


def rand_arr(size, lower, upper):
    return [randrange(lower, upper+1) for i in range(size)]


size = pyip.inputNum("What size array would you like sorted? (N<=975) ")
lower = pyip.inputNum("Enter lower bound for array values ")
upper = pyip.inputNum("Enter upper bound for array values ")

print('Bubble Sorting')
bubble_start = time()
for i in range(10):
    arr = rand_arr(size, lower, upper)
    print('Input:', arr)
    print('Output:', bubble_sort(arr, len(arr)))
bubble_end = time()
quick_start = time()
for i in range(10):
    arr = rand_arr(size, lower, upper)
    print('Input:', arr)
    print('Output:', quick_sort(arr, 0, len(arr)-1))
quick_end = time()

print('Average bubble sort O(N^2) time for N =', size, (bubble_end-bubble_start)/10, 'seconds')
print('Average quick sort time O(NlogN) time for N =', size, (quick_end-quick_start)/10, 'seconds')
