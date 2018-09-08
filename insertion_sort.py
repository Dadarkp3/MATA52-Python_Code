

def insertion_sort(A):
    for j in range(0, len(A)):
        chave = A[j]
        i = j - 1
        while i >= 0 and A[i] > chave:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = chave
    return A

if __name__=="__main__":
    x = [10,20,-1,19,40]
    insertion_sort(x)
    print(x)