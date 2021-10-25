import time

cache = {}

def mult(x):
    if x in cache.keys():
        return cache[x]
    res = 1
    for i in range(x):
        res *= x
    cache[x] = res
    return res

def calc_exec(x):
    inicio = time.perf_counter()
    num = mult(x)
    fin = time.perf_counter()

    tiempo_exec = fin - inicio

    return num, tiempo_exec

if __name__ == '__main__':
    lista = [100000, 110000, 120000, 150000, 100000]
    for elemento in lista:
        valor, tiempo = calc_exec(elemento)
        print(f"El resultado de tiempo de ejecucion para {elemento} es {tiempo} segundos")
