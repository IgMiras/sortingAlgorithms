# Heap Sort
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


def heapify(arr, n, i):
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(tipo_lista, num):
    if tipo_lista == "aleatoria":
        lista = cria_vetor_aleatorio(num)
    elif tipo_lista == "crescente":
        lista = cria_vetor_crescente(num)
    elif tipo_lista == "decrescente":
        lista = cria_vetor_decrescente(num)
    else:
        print("Tipo de lista invalido!")
        return

    n = len(lista)

    # Build max heap
    for i in range(n // 2, -1, -1):
        heapify(lista, n, i)

    for i in range(n - 1, 0, -1):
        # Swap
        lista[i], lista[0] = lista[0], lista[i]

        # Heapify root element
        heapify(lista, i, 0)


tamanho_entrada = [1000, 5000, 10000, 15000, 20000, 25000]
tempo_execucao = []

# Entrada Aleatória
for tamanho in tamanho_entrada:
    inicio = timeit.default_timer()
    heapSort("aleatoria", tamanho)
    fim = timeit.default_timer()
    duracao = fim - inicio
    tempo_execucao.append(duracao)

fig, ax = plt.subplots()
ax.bar(tamanho_entrada, tempo_execucao, width=2000)
ax.set_title("Heap Sort com Entrada Aleatoria")
ax.set_xlabel("Tamanho da Entrada")
ax.set_ylabel("Tempo de Execucao")
plt.show()
tempo_execucao.clear()

# Entrada Crescente
for tamanho in tamanho_entrada:
    inicio = timeit.default_timer()
    heapSort("crescente", tamanho)
    fim = timeit.default_timer()
    duracao = fim - inicio
    tempo_execucao.append(duracao)

fig, ax = plt.subplots()
ax.bar(tamanho_entrada, tempo_execucao, width=2000)
ax.set_title("Heap Sort com Entrada Crescente")
ax.set_xlabel("Tamanho da Entrada")
ax.set_ylabel("Tempo de Execucao")
plt.show()
tempo_execucao.clear()

# Entrada Decrescente
for tamanho in tamanho_entrada:
    inicio = timeit.default_timer()
    heapSort("decrescente", tamanho)
    fim = timeit.default_timer()
    duracao = fim - inicio
    tempo_execucao.append(duracao)

fig, ax = plt.subplots()
ax.bar(tamanho_entrada, tempo_execucao, width=2000)
ax.set_title("Heap Sort com Entrada Decrescente")
ax.set_xlabel("Tamanho da Entrada")
ax.set_ylabel("Tempo de Execucao")
plt.show()
tempo_execucao.clear()
