import time
import os
import json

cache = {}

def init_cache():
    if(os.path.exists("./cache")):
        f = open("./cache", "r")
        data = f.read()
        f.close()
        cache = json.loads(data)
        print(cache)
    else:
        cache = {}
        print("No existe ningun archivo de cache")


def write_to_cache_file():
    f = open("./cache", "w+")
    f.write(json.dumps(cache))
    f.close()


def fact_no_recursiva(n):
    fact = 1

    while n > 1:
        fact *= n
        n -= 1
    
    return fact


def fact_recursiva(n):
    if n in cache.keys():
        return cache[n]
    
    if n > 1:
        fact = n * fact_recursiva(n - 1)
        cache[n] = fact
        write_to_cache_file()
        return fact
    else:
        return 1


if __name__ == '__main__':
    print("Inicio de programa")
    
    init_cache()

    res = fact_recursiva(20)

    # inicio_no_recursivo = time.perf_counter()
    # for i in range(5000):
    #     res = fact_no_recursiva(i)
    # fin_no_recursivo = time.perf_counter()
    # print(f"[*] Tiempo de ejecucion para operaciones no recursivas es {fin_no_recursivo - inicio_no_recursivo} segundos")
    
    # inicio_recursivo = time.perf_counter()
    # for i in range(5000):
    #     res = fact_recursiva(i)
    # fin_recursivo = time.perf_counter()
    # print(f"[+] Tiempo de ejecucion para operaciones recursivas es {fin_recursivo - inicio_recursivo} segundos")
    
    print("Fin de programa")