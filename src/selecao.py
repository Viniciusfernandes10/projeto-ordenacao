n = int(input())
lista = input().split()
for i, v in enumerate(lista):
    lista[i] = int(v)

def get_indice_menor(v, n, i):
    i_menor = i
    for j in range(i + 1, n):
        if v[j] < v[i_menor]:
            i_menor = j
    return i_menor

for i in range(n):
    j = get_indice_menor(lista, n, i)
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux

#print(*lista)
