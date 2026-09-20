n = int(input())
lista = input().split()
for i, v in enumerate(lista):
    lista[i] = int(v)


def troca(v, i, j):
    aux = v[i]
    v[i] = v[j]
    v[j] = aux


def peneira(v, tamanho, raiz):
    maior = raiz
    esq = 2 * raiz + 1
    dir = 2 * raiz + 2

    if esq < tamanho and v[esq] > v[maior]:
        maior = esq
    if dir < tamanho and v[dir] > v[maior]:
        maior = dir

    if maior != raiz:
        troca(v, raiz, maior)
        peneira(v, tamanho, maior)


def constroi_heap(v, n):
    for i in range(n // 2 - 1, -1, -1):
        peneira(v, n, i)


def heap_sort(v, n):
    constroi_heap(v, n)
    for fim in range(n - 1, 0, -1):
        troca(v, 0, fim)
        peneira(v, fim, 0)


heap_sort(lista, n)
#print(*lista)
