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

#radix sort random list
from random import randint
def countingSort(arr, place):
    output = [0] * (len(arr))
    count = [0] * (10)

    for i in range(0, len(arr)):
        index = arr[i]//place
        count[index % 10] += 1
    for i in range(1, 10):
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
