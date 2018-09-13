def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            aux = A[i]
            A[i] = A[j]
            A[j] = aux
    aux = A[i + 1]
    A[i + 1] = A[r]
    A[r] = aux
    return i + 1


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


if __name__ == "__main__":
    lista = [54, 26, 93, 17, 77, 31, 44, 55, 20, 1]
    quicksort(lista, 0, len(lista) - 1)
    print(lista)
