def max_heapify(A,k):
    l = left(k)
    r = right(k)
    if l < len(A) and A[l] > A[k]:
        large = l
    else:
        large = k
    if r < len(A) and A[r] > A[large]:
        large = r
    if large != k:
        A[k], A[large] = A[large], A[k]
        max_heapify(A, large)

def left(k):
    return 2 * k + 1

def right(k):
    return 2 * k + 2
def insertion(A, k):
    size = len(A)
    if size == 0:
        A.append(k)
    else:
        A.append(k)
        for i in range(size - 1, -1, -1):
            max_heapify(A, i)
def display(A):
    print("Max-heap array: " + str(A))
    print()


arr = []

insertion(arr, 9)
insertion(arr, 12)
insertion(arr, 1)
insertion(arr, 20)
insertion(arr, 13)
display(arr)


