n = int(input())
lista = input().split()
for i, v in enumerate(lista):
    lista[i] = int(v)

for i in range(1, n):
    chave = lista[i]
    j = i - 1
    while j >= 0 and lista[j] > chave:
        lista[j + 1] = lista[j]
        j -= 1
    lista[j + 1] = chave

#print(*lista)
