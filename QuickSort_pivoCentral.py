# Quick Sort com Pivô sendo o elemento central
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


def partition(nums, left, right, pivot):
    while left <= right:
        while nums[left] < pivot:
            left = left + 1
        while nums[right] > pivot:
            right = right - 1
        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left = left + 1
            right = right - 1
    return left


def quickSort(nums, left, right):
    if left >= right:
        return
    pivot = nums[(right + left) // 2]
    index = partition(nums, left, right, pivot)
    quickSort(nums, left, index - 1)
    quickSort(nums, index, right)


tamanho_entrada = [1000, 5000, 10000, 15000, 20000, 25000]
tempo_execucao = []

# Entrada Aleatória
for tamanho in tamanho_entrada:
    lista = cria_vetor_aleatorio(tamanho)
    inicio = timeit.default_timer()
    quickSort(lista, 0, len(lista) - 1)
    fim = timeit.default_timer()
    duracao = fim - inicio
    tempo_execucao.append(duracao)
    lista.clear()

fig, ax = plt.subplots()
ax.bar(tamanho_entrada, tempo_execucao, width=2000)
ax.set_title("Quick Sort com Pivô central - Entrada Aleatoria")
ax.set_xlabel("Tamanho da Entrada")
ax.set_ylabel("Tempo de Execucao")
plt.show()
tempo_execucao.clear()

# Entrada Crescente
for tamanho in tamanho_entrada:
    lista = cria_vetor_crescente(tamanho)
    inicio = timeit.default_timer()
    quickSort(lista, 0, len(lista) - 1)
    fim = timeit.default_timer()
    duracao = fim - inicio
    tempo_execucao.append(duracao)
    lista.clear()

fig, ax = plt.subplots()
ax.bar(tamanho_entrada, tempo_execucao, width=2000)
ax.set_title("Quick Sort com Pivô central - Entrada Crescente")
ax.set_xlabel("Tamanho da Entrada")
ax.set_ylabel("Tempo de Execucao")
plt.show()
tempo_execucao.clear()

# Entrada Decrescente
for tamanho in tamanho_entrada:
    lista = cria_vetor_decrescente(tamanho)
    inicio = timeit.default_timer()
    quickSort(lista, 0, len(lista) - 1)
    fim = timeit.default_timer()
    duracao = fim - inicio
    tempo_execucao.append(duracao)
    lista.clear()

fig, ax = plt.subplots()
ax.bar(tamanho_entrada, tempo_execucao, width=2000)
ax.set_title("Quick Sort com Pivô central - Entrada Decrescente")
ax.set_xlabel("Tamanho da Entrada")
ax.set_ylabel("Tempo de Execucao")
plt.show()
tempo_execucao.clear()
