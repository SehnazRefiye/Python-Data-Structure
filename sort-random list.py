#selection sort random list
from random import randint
def selection(arr):
    for i in range(len(arr)):
        kucuk = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[kucuk]:
                kucuk = j
        arr[i], arr[kucuk] = arr[kucuk], arr[i]
arr = []
for i in range(10):
    value = randint(0, 100)
    arr.append(value)
print("Selection Sort")
print("Given array is: ")
print(arr)
selection(arr)
print("Sorted array is: ")
print(arr)
print()

#bubble sort random list
from random import randint
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
arr = []
for i in range(10):
    value = randint(0, 100)
    arr.append(value)
print("Bubble Sort")
print("Given array is: ")
print(arr)
bubbleSort(arr)
print("Sorted array is: ")
print(arr)
print()

#heap sort random list
from random import randint
def heapify(arr, i, heap_size):
    largest = i
    left_index = 2 * i + 1
    right_index = 2 * i + 2
    if left_index < heap_size and arr[left_index] > arr[largest]:
        largest = left_index
    if right_index < heap_size and arr[right_index] > arr[largest]:
        largest = right_index
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, largest, heap_size)
def heapSort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, i, n)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)
arr = []
for i in range(10):
    value = randint(0, 100)
    arr.append(value)
print("Heap Sort")
print("Given array is: ")
print(arr)
heapSort(arr)
print("Sorted array is: ")
print(arr)
print()

#insertion sort random list
from random import randint
def insertionSort(arr):
    for i in range(len(arr)):
        value = arr[i]
        j = i-1
        while j >= 0 and arr[j] > value:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = value
arr = []
for i in range(10):
    value = randint(0, 100)
    arr.append(value)
print("Insertion Sort")
print("Given array is: ")
print(arr)
insertionSort(arr)
print("Sorted array is: ")
print(arr)
print()

#shell sort random list
from random import randint
def shellSort(arr):
    sublistcount = len(arr)//2
    while sublistcount > 0:
        for i in range(sublistcount, len(arr)):
            temp = arr[i]
            j = i
            while j >= sublistcount and arr[j-sublistcount] > temp:
                arr[j] = arr[j-sublistcount]
                j -= sublistcount
            arr[j] = temp
        sublistcount //= 2
arr = []
for i in range(10):
    value = randint(0, 100)
    arr.append(value)
print("Shell Sort")
print ("Given array is: ")
print(arr)
shellSort(arr)
print("Sorted array is: ")
print(arr)
print()

#radix sort random list
from random import randint
def countingSort(arr, place):
    output = [0] * (len(arr))
    count = [0] * (10)

    for i in range(0, len(arr)):
        index = arr[i]//place
        count[index % 10] += 1
    for i in range(1,10):
        count[i] += count[i-1]
    i = len(arr)-1
    while i >= 0:
        index = arr[i]//place
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(0,len(arr)):
        arr[i] = output[i]

def radixSort(arr):
    max_element = max(arr)
    place = 1
    while max_element/place > 0:
        countingSort(arr,place)
        place *= 10
arr = []
for i in range(10):
    value = randint(0, 100)
    arr.append(value)
print("Radix Sort")
print ("Given array is: ")
print(arr)
radixSort(arr)
print("Sorted array is: ")
print(arr)
print()

#merge sort random list
from random import randint
def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                arr[k]=lefthalf[i]
                i=i+1
            else:
                arr[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            arr[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            arr[k]=righthalf[j]
            j=j+1
            k=k+1

def printList(arr):
    for i in range(1):
        print(arr)

if __name__ == '__main__':
    arr = []
    for i in range(10):
        value = randint(0, 100)
        arr.append(value)
    print("Merge Sort")
    print("Given array is: ")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ")
    printList(arr)
    print()

#Quick Sort random list
def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return(i+1)
def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
arr = []
for i in range(10):
    value = randint(0, 100)
    arr.append(value)
print("Quick Sort")
print("Given array is: ")
print(arr)
n = len(arr)
quickSort(arr,0,n-1)
print("Sorted array is: ")
print(arr)
print()
