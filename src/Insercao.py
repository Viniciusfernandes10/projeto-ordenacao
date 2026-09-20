n = int(input())
lista = input().split()
for i, v in enumerate(lista):
    lista[i] = int(v)


def troca(v, i, j):
    aux = v[i]
    v[i] = v[j]
    v[j] = aux


for i in range(1, n):
    j = i
    while j > 0 and lista[j - 1] > lista[j]:
        troca(lista, j - 1, j)
        j -= 1

#print(*lista)
