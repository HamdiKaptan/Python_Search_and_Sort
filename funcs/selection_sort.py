def selection_sort(A):
    for i in range(0, len(A) - 1):
        minindex = i
        for j in range(i + 1, len(A)):
            if A[j] < A[minindex]:
                minindex = j
        if minindex != i:
            A[i], A[minindex] = A[minindex], A[i]


A = [5, 9, 1, 2, 4, 8, 6, 3, 7]
print(A)
selection_sort(A)
print(A)
