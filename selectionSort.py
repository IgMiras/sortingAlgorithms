# Selection Sort
import random
import timeit
import matplotlib.pyplot as plt


def cria_vetor_aleatorio(num):
    lista = []
    for i in range(num):
        x = random.randint(1, num)
        lista.append(x)
    return lista


def cria_vetor_crescente(num):
    lista = []
    for i in range(num):
        lista.append(i)
    return lista


def cria_vetor_decrescente(num):
    lista = []
    for i in range(num):
        lista.append(num - i)
    return lista


def mini(a):
    minimum = a[0]
    x = 0
    for i in range(1, len(a)):
        if a[i] < minimum:
            minimum, x = a[i], i
    return x


def selectSort(tipo_lista, num):
    if tipo_lista == "aleatoria":
        lista = cria_vetor_aleatorio(num)
    elif tipo_lista == "crescente":
        lista = cria_vetor_crescente(num)
    elif tipo_lista == "decrescente":
        lista = cria_vetor_decrescente(num)
    else:
        print("Tipo de lista invalido!")
        return

    for i in range(0, len(lista)):
        ind = mini(lista[i : len(lista)])
        if (ind + i) > (i):
            lista[i], lista[i + ind] = lista[i + ind], lista[i]

        # print(i+ind,lista)


tamanho_entrada = [1000, 5000, 10000, 15000, 20000, 25000]
tempo_execucao = []

# Entrada Aleatória
for tamanho in tamanho_entrada:
    inicio = timeit.default_timer()
    selectSort("aleatoria", tamanho)
    fim = timeit.default_timer()
    duracao = fim - inicio
    tempo_execucao.append(duracao)

fig, ax = plt.subplots()
ax.bar(tamanho_entrada, tempo_execucao, width=2000)
ax.set_title("Selection Sort com Entrada Aleatoria")
ax.set_xlabel("Tamanho da Entrada")
ax.set_ylabel("Tempo de Execucao")
plt.show()
tempo_execucao.clear()

# Entrada Crescente
for tamanho in tamanho_entrada:
    inicio = timeit.default_timer()
    selectSort("crescente", tamanho)
    fim = timeit.default_timer()
    duracao = fim - inicio
    tempo_execucao.append(duracao)

fig, ax = plt.subplots()
ax.bar(tamanho_entrada, tempo_execucao, width=2000)
ax.set_title("Selection Sort com Entrada Crescente")
ax.set_xlabel("Tamanho da Entrada")
ax.set_ylabel("Tempo de Execucao")
plt.show()
tempo_execucao.clear()

# Entrada Decrescente
for tamanho in tamanho_entrada:
    inicio = timeit.default_timer()
    selectSort("decrescente", tamanho)
    fim = timeit.default_timer()
    duracao = fim - inicio
    tempo_execucao.append(duracao)

fig, ax = plt.subplots()
ax.bar(tamanho_entrada, tempo_execucao, width=2000)
ax.set_title("Selection Sort com Entrada Decrescente")
ax.set_xlabel("Tamanho da Entrada")
ax.set_ylabel("Tempo de Execucao")
plt.show()
tempo_execucao.clear()
