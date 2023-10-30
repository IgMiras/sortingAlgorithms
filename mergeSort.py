# Merge Sort
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


def mergehalf(nums, temp, leftstart, rightend):
    leftend = (leftstart + rightend) // 2
    rightstart = leftend + 1
    left = leftstart
    right = rightstart
    index = leftstart
    while (left <= leftend) and (right <= rightend):
        if nums[left] <= nums[right]:
            if index < len(temp):
                temp[index] = nums[left]
            else:
                temp.insert(index, nums[left])
            left = left + 1
        else:
            if index < len(temp):
                temp[index] = nums[right]
            else:
                temp.insert(index, nums[right])
            right = right + 1
        index = index + 1
    if left <= leftend:
        temp.extend(nums[left : leftend + 1])
    if right <= rightend:
        temp.extend(nums[right : rightend + 1])
    size = rightend - leftstart + 1
    nums[leftstart : leftstart + size] = temp[0:size]


def mergeSort(nums, left, right):
    if left >= right:
        return
    mid = (left + right) // 2
    mergeSort(nums, left, mid)
    mergeSort(nums, mid + 1, right)
    temp = []
    mergehalf(nums, temp, left, right)


tamanho_entrada = [1000, 5000, 10000, 15000, 20000, 25000]
tempo_execucao = []

# Entrada Aleatória
for tamanho in tamanho_entrada:
    lista = cria_vetor_aleatorio(tamanho)
    inicio = timeit.default_timer()
    mergeSort(lista, 0, len(lista) - 1)
    fim = timeit.default_timer()
    duracao = fim - inicio
    tempo_execucao.append(duracao)
    lista.clear()

fig, ax = plt.subplots()
ax.bar(tamanho_entrada, tempo_execucao, width=2000)
ax.set_title("Merge Sort com Entrada Aleatoria")
ax.set_xlabel("Tamanho da Entrada")
ax.set_ylabel("Tempo de Execucao")
plt.show()
tempo_execucao.clear()

# Entrada Crescente
for tamanho in tamanho_entrada:
    lista = cria_vetor_crescente(tamanho)
    inicio = timeit.default_timer()
    mergeSort(lista, 0, len(lista) - 1)
    fim = timeit.default_timer()
    duracao = fim - inicio
    tempo_execucao.append(duracao)
    lista.clear()

fig, ax = plt.subplots()
ax.bar(tamanho_entrada, tempo_execucao, width=2000)
ax.set_title("Merge Sort com Entrada Crescente")
ax.set_xlabel("Tamanho da Entrada")
ax.set_ylabel("Tempo de Execucao")
plt.show()
tempo_execucao.clear()

# Entrada Decrescente
for tamanho in tamanho_entrada:
    lista = cria_vetor_decrescente(tamanho)
    inicio = timeit.default_timer()
    mergeSort(lista, 0, len(lista) - 1)
    fim = timeit.default_timer()
    duracao = fim - inicio
    tempo_execucao.append(duracao)
    lista.clear()

fig, ax = plt.subplots()
ax.bar(tamanho_entrada, tempo_execucao, width=2000)
ax.set_title("Merge Sort com Entrada Decrescente")
ax.set_xlabel("Tamanho da Entrada")
ax.set_ylabel("Tempo de Execucao")
plt.show()
tempo_execucao.clear()
