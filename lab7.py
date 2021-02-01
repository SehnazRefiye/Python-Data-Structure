#Bubble sort
arr = [10, 54, 50, 43, 11, 12, 90]
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
bubbleSort(arr)
print(arr)
#Selection sort
arr = [10, 54, 50, 43, 11, 12, 90]
for i in range(len(arr)):
    kucuk = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[kucuk]:
            kucuk = j
    arr[i], arr[kucuk] = arr[kucuk], arr[i]
print(arr)

#heap sort
arr = [10, 54, 50, 43, 11, 12, 90]
def heapify(arr, n, i):
    largest = i
    left = 2*i+1
    right = 2*i+2
    if left < n and arr[i] < arr[left]:
        largest = left
    if right< n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr, n, largest)
def heapSort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
heapSort(arr)
n = len(arr)
print(arr)

#insertion sort
arr = [10, 54, 50, 43, 11, 12, 90]
def insertionSort(arr):
    for i in range(len(arr)):
        value = arr[i]
        j = i-1
        while j >= 0 and arr[j] > value:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = value
insertionSort(arr)
print(arr)

#shell sort
arr = [10, 54, 50, 43, 11, 12, 90]
def shellSort(arr):
    sublistcount = len(arr)//2
    while sublistcount > 0:
        for i in range (sublistcount, len(arr)):
            temp = arr[i]
            j = i
            while  j >= sublistcount and arr[j-sublistcount] >temp:
                arr[j] = arr[j-sublistcount]
                j -= sublistcount
            arr[j] = temp
        sublistcount //= 2
shellSort(arr)
print(arr)

#radix sort
arr = [10, 54, 50, 43, 11, 12, 90]
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
radixSort(arr)
print(arr)

#Quick Sort
arr = [10, 54, 50, 43, 11, 12, 90]
def partition(arr,low,high):
    i = (low-1)
    pivot = arr[high]
    for j in range(low , high):
        if arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return (i+1)
def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
n = len(arr)
quickSort(arr,0,n-1)
print(arr)
