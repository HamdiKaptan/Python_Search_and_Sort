def insertion_sort2(A):
    for i in range(1, len(A)):
        j = i - 1
        while A[j] > A[j + 1] and j >= 0:
            A[j], A[j + 1] = A[j + 1], A[j]
            j -= 1


A = [5, 9, 1, 2, 4, 8, 6, 3, 7]
print(A)
insertion_sort2(A)
print(A)
