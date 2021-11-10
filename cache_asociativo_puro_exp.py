import time

cache_size = 10
cache = [[0, 0]] * cache_size
idx = 0
total = 0
hit = 0
miss = 0


# Politica de reemplazo FIFO
# TODO: Implementar con politica de reemplazo LFU (Least Frequently Used)
def exp(n):
    global total, hit, miss, idx
    total += 1
    for i in range(cache_size):
        if cache[i][0] == n:
            hit += 1
            return cache[i][1]    
    miss += 1
    res = 1

    for i in range(n):
       res *= n
    
    cache[idx] = [n, res]
    if idx == 9:
        idx = 0
    else:
        idx += 1

    return res


if __name__ == '__main__':
    lista_n = [5000, 220, 457, 12, 323, 440, 323, 5000, 220, 440]

    for num in lista_n:
        inicio = time.perf_counter()
        resultado = exp(num)
        fin = time.perf_counter()

        print(f"El tiempo de ejecucion para exp de {num} es {fin - inicio}")

    porcentaje_hit = (float(hit) / float(total)) * 100
    porcentaje_miss = (float(miss) / float(total)) * 100

    print(f"Porcentaje de hit: {porcentaje_hit}%, porcentaje miss: {porcentaje_miss}%, total de accesos: {total}")