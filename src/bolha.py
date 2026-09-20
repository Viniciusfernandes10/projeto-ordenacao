n = int(input())



lista = input().split()

for i, v in enumerate(lista):

    lista[i] = int(v)



for i in range(n):

    for j in range(n - 1):

        if lista[j] > lista[j+1]:

            aux = lista[j]

            lista[j] = lista[j+1]

            lista[j+1] = aux

#print(*lista)
