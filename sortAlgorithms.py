# 1. bubble Sort
def bubbleSort(arr):
    size = len(arr)
    flag = 1
    for i in range(size-1):
        for j in range(1, size-i):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                flag = 0
        if flag:
            break
        flag = 1  
        
# 2. selection Sort
def selectionSort(arr):
    size = len(arr)
    for i in range(size-1):
        min_index = i
        for j in range(i+1, size):
            if arr[j] < arr[i]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]

# 3. insertion Sort
def insertionSort(arr):
    size = len(arr)
    for i in range(1, size):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# 4. merge Sort
def merge(arr, l, m, r):
    arrL = []
    arrR = []
    sizeL = m - l + 1
    sizeR = r - m
    for i in range(sizeL):
        arrL.append(arr[l + i])
    for j in range(sizeR):
        arrR.append(arr[m + j + 1])
     
    i = 0
    j = 0    
    k = l
    while i < sizeL and j < sizeR:
        if arrL[i] <= arrR[j]:
            arr[k] = arrL[i]
            i += 1
        else:
            arr[k] = arrR[j]
            j += 1
        k += 1
    while i < sizeL:
        arr[k] = arrL[i]
        i += 1
        k += 1
    while j < sizeR:
        arr[k] = arrR[j]
        j += 1
        k += 1
        
def mergeSort(arr, l, r):
    if l >= r:
        return
    m = (r+l)//2
    mergeSort(arr, l, m)
    mergeSort(arr, m + 1, r)
    merge(arr, l, m, r) 


# 5.1 quick Sort1, pivit - last
def partition1(arr, l, r):
    x = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i + 1

def quickSort1(arr, l, r):
    if l < r:
        pivot = partition1(arr, l, r)
        quickSort1(arr, l, pivot - 1)
        quickSort1(arr, pivot + 1, r)
        
        
# 5.2 quick Sort2, pivot = first       
def partition2(arr, l, r):
    pivot = arr[l]
    j = l
    for i in range(l+1, r):
        if arr[i] <= pivot:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j
        
def quickSort2(arr, l, r):
    if l < r:
        pivot = partition2(arr, l, r)
        quickSort2(arr, l, pivot - 1)
        quickSort2(arr, pivot + 1, r)
              
# 5.3 quick Sort3, pivot - random
import random
def partition3(arr, l, r):
    i = random.randint(l, r)
    arr[i], arr[r] = arr[r], arr[i]
    pivot = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1

def quickSort3(arr, l, r):
    if l < r:
        rand = partition3(arr, l, r)
        quickSort3(arr, l, rand - 1)
        quickSort3(arr, rand + 1, r) 
        
        
# 6. counting Sort 
def counting_sort_stable(arr):
    mi = min(arr)
    ma = max(arr)
    
    l = ma - mi + 1
    count = [0] * l
    sortedArr = [0] * len(arr)
    
    for num in arr:
        count[num-mi] += 1
        
    for i in range(1, l):
        count[i] += count[i-1]
    print(count)
        
    for i in range(l-1, 0, -1):
        count[i] = count[i-1]
    count[0] = 0
    
    print(count)
    for num in arr:
        sortedArr[count[num-mi]] = num
        count[num-mi] += 1
        
    return sortedArr

# 7. radix Sort
def counting_sort_stable(arr, exp):
    count = [0] * 10
    sortedArr = [0] * len(arr)
    
    for num in arr:
        count[(num // exp) % 10] += 1
        
    for i in range(1, 10):
        count[i] += count[i-1]
        
    for i in range(9, 0, -1):
        count[i] = count[i-1]
    count[0] = 0
    
    for num in arr:
        sortedArr[count[(num//exp)%10]] = num
        count[(num//exp)%10] += 1
        
    for i in range(len(arr)):
        arr[i] = sortedArr[i]

def radixSort(arr):
    maxNum = max(arr)
    exp = 1
    while maxNum // exp > 0:
        counting_sort_stable(arr, exp)
        print(arr)
        exp *= 10
