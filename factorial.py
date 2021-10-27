import time

cache = {}

def factorial_cache(n):
    if n in cache.keys():
        return cache[n]
    
    fact = None
    if n == 1:
        fact = 1
    else:
        fact = n * factorial_cache(n - 1)
    
    cache[n] = fact
    return fact

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def factorial_no_recursivo(n):
    res = 1

    for i in range(1, n + 1):
        res *= i

    return res


if __name__ == '__main__':
    factorial_in = 99
    inicio1 = time.perf_counter()
    res = factorial_cache(factorial_in)
    fin1 = time.perf_counter()
    print(f"El tiempo de ejecucion de {factorial_in}! es {fin1 - inicio1}")
    
    factorial_in = 100
    inicio2 = time.perf_counter()
    res = factorial_cache(factorial_in)
    fin2 = time.perf_counter()
    print(f"El tiempo de ejecucion de {factorial_in}! es {fin2 - inicio2}")

    # factorial_in = 100
    # inicio_recursivo = time.perf_counter()
    # res_recursivo = factorial(factorial_in)
    # fin_recursivo = time.perf_counter()
    # inicio_no_recursivo = time.perf_counter()
    # res_no_recursivo = factorial_no_recursivo(factorial_in)
    # fin_no_recursivo = time.perf_counter()

    # print(f"El tiempo de ejecucion para factorial de {factorial_in} con recursividad es {fin_recursivo - inicio_recursivo} segundos")
    # print(f"El tiempo de ejecucion para factorial de {factorial_in} sin recursividad es {fin_no_recursivo - inicio_no_recursivo} segundos")