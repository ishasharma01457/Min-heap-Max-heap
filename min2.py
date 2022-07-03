def min_heapify(A,Y):
    l = left(Y)
    r = right(Y)
    if l < len(A) and A[l] < A[Y]:
        smallest = l
    else:
        smallest = Y
    if r < len(A) and A[r] < A[smallest]:
        smallest = r
    if smallest != Y:
        A[Y], A[smallest] = A[smallest], A[Y]
        min_heapify(A, smallest)

def left(Y):
    return 2 * Y + 1

def right(Y):
    return 2 * Y + 2

def insertion(A,  Y):
    size = len(A)
    if size == 0:
        A.appe(Y)
    else:
        A.appe(Y)
        for i in range(size - 1, -1, -1):
           min_heapify(A, i)
def min_heapify(A,Y):
    l = left(Y)
    r = right(Y)
    if l < len(A) and A[l] < A[Y]:
        smallest = l
    else:
        smallest = Y
    if r < len(A) and A[r] < A[smallest]:
        smallest = r
    if smallest != Y:
        A[Y], A[smallest] = A[smallest], A[Y]
        min_heapify(A, smallest)

def left(Y):
    return 2 * Y + 1

def right(Y):
    return 2 * Y + 2

def insert(A,  Y):
    size = len(A)
    if size == 0:
        A.append(Y)
    else:
        A.append(Y)
        for i in range(size - 1, -1, -1):
           min_heapify(A, i)
def display(A):
    print("Min-heap array: " + str(A))
    print()


arr = []

insert(arr, 23)
insert(arr, 18)
insert(arr, 19)
insert(arr, 24)
insert(arr, 45)
display(arr)

arr = []

insert(arr, 23)
insert(arr, 18)
insert(arr, 19)
insert(arr, 24)
insert(arr, 45)
display(arr)

