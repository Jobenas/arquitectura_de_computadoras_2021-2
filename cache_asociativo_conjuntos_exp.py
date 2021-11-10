import time

cache_size = 10
num_conjuntos = 2
cache = [[0, 0]] * cache_size
idxo = [0] * num_conjuntos
total = 0
hit = 0
miss = 0


# Politica de reemplazo FIFO
# TODO: Implementar con politica de reemplazo LFU (Least Frequently Used)
def exp(n):
    global total, hit, miss
    total += 1
    idxc = n % num_conjuntos
    p = int(cache_size / num_conjuntos)
    for i in range(idxc * p, idxc * p + p):
        if cache[i][0] == n:
            hit += 1
            return cache[i][1]    
    miss += 1
    res = 1

    for i in range(n):
       res *= n
    
    idx = (idxc * p) + idxo[idxc]
    cache[idx] = [n, res]

    if idxo[idxc] == p - 1:
        idxo[idxc] = 0
    else:
        idxo[idxc] += 1

    return res


if __name__ == '__main__':
    lista_n = [5000, 220, 457, 12, 323, 440, 323, 440, 220, 5000]

    for num in lista_n:
        inicio = time.perf_counter()
        resultado = exp(num)
        fin = time.perf_counter()

        print(f"El tiempo de ejecucion para exp de {num} es {fin - inicio}")

    porcentaje_hit = (float(hit) / float(total)) * 100
    porcentaje_miss = (float(miss) / float(total)) * 100

    print(f"Porcentaje de hit: {porcentaje_hit}%, porcentaje miss: {porcentaje_miss}%, total de accesos: {total}")