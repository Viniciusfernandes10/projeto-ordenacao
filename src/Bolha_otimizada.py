n = int(input())
lista = input().split()
for i, v in enumerate(lista):
    lista[i] = int(v)


def troca(v, i, j):
    aux = v[i]
    v[i] = v[j]
    v[j] = aux


limite = n - 1
trocou = True
while trocou and limite > 0:
    trocou = False
    for j in range(limite):
        if lista[j] > lista[j + 1]:
            troca(lista, j, j + 1)
            trocou = True
    limite -= 1

#print(*lista)
