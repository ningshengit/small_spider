实例 1 
def leftRotate(arr, d, n): 
    for i in range(d): 
        leftRotatebyOne(arr, n) 
def leftRotatebyOne(arr, n): 
    temp = arr[0] 
    for i in range(n-1): 
        arr[i] = arr[i+1] 
    arr[n-1] = temp 
          
  
def printArray(arr,size): 
    for i in range(size): 
        print ("%d"% arr[i],end=" ") 
  

arr = [1, 2, 3, 4, 5, 6, 7] 
leftRotate(arr, 2, 7) 
printArray(arr, 7) 
实例 2 
def leftRotate(arr, d, n): 
    for i in range(gcd(d,n)): 
          
        temp = arr[i] 
        j = i 
        while 1: 
            k = j + d 
            if k >= n: 
                k = k - n 
            if k == i: 
                break
            arr[j] = arr[k] 
            j = k 
        arr[j] = temp 

def printArray(arr, size): 
    for i in range(size): 
        print ("%d" % arr[i], end=" ") 

def gcd(a, b): 
    if b == 0: 
        return a; 
    else: 
        return gcd(b, a%b) 

arr = [1, 2, 3, 4, 5, 6, 7] 
leftRotate(arr, 2, 7) 
printArray(arr, 7) 
实例 3 
def rverseArray(arr, start, end): 
    while (start < end): 
        temp = arr[start] 
        arr[start] = arr[end] 
        arr[end] = temp 
        start += 1
        end = end-1
  
def leftRotate(arr, d): 
    n = len(arr) 
    rverseArray(arr, 0, d-1) 
    rverseArray(arr, d, n-1) 
    rverseArray(arr, 0, n-1) 
  
def printArray(arr): 
    for i in range(0, len(arr)): 
        print (arr[i], end=' ') 
  
arr = [1, 2, 3, 4, 5, 6, 7] 
leftRotate(arr, 2) 
printArray(arr) 
