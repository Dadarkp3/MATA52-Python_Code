def merge(lista, inicio, meio, final):
    n1 = meio - inicio + 1
    n2 = final - meio

    L = lista[inicio:meio + 1]
    R = lista[meio + 1:final + 1]

    L.append(999999999)
    R.append(999999999)

    i = 0
    j = 0

    for k in range(inicio, final+1):
        if L[i] <= R[j]:
            lista[k] = L[i]
            i += 1
        else:
            lista[k] = R[j]
            j += 1


def merge_sort(lista, inicio, final):
    if inicio < final:
        meio = (inicio + final) // 2
        merge_sort(lista, inicio, meio)
        merge_sort(lista, meio+1, final)
        merge(lista, inicio, meio, final)


if __name__=="__main__":
    lista = [54, 26, 93, 17, 77, 31, 44, 55, 20, 1]
    inicio = 0;
    final = len(lista) - 1
    merge_sort(lista, inicio, final)
    print(lista)