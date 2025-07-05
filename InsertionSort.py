def InsertionSort(A):
    for j in range(1, len(A)):
        key =  A[j]
        i = j -1
        while (i>=0) and A[i] > key:
            A[i+1] = A[i]
            i = i-1
            A[i+1] = key


x = [45,78,8,9,6,2,7,3,8,1]
InsertionSort(x)
print(x)