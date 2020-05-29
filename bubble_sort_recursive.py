import pyinputplus as pyip
from random import randrange


def bubble_sort(list, end):
    if end == 0:
        return list
    for i in range(end-1):
        if list[i+1] < list[i]:
            temp = list[i+1]
            list[i+1] = list[i]
            list[i] = temp
    return bubble_sort(list, end-1)


size = pyip.inputNum("What size array would you like sorted? ")
sort = [randrange(0, 1001) for i in range(size)]
print("Initial Array:", sort)
print("Recursively Sorted Array:", bubble_sort(sort, len(sort)))
