import time
import numpy as np
from multiprocessing import Pool, cpu_count

VECTOR_SIZE = 10000

def suma_exponenciales(a, b):
    total = 0
    for i in range(10000):
        total += a**b
    return total


if __name__ == '__main__':
    array_a = np.random.randint(5, size=(VECTOR_SIZE))
    array_b = np.random.randint(5, size=(VECTOR_SIZE))

    result_serial = []
    inicio_serial = time.perf_counter()
    for i in range(VECTOR_SIZE):
        result_serial.append(suma_exponenciales(array_a[i], array_b[i]))
    fin_serial = time.perf_counter()

    print(f"Tiempo de ejecucion para operacion en serie: {fin_serial - inicio_serial} segundos")

    params = zip(array_a, array_b)
    inicio_paralelo = time.perf_counter()
    p = Pool(processes=cpu_count())
    result_paralelo = p.starmap(suma_exponenciales, params)
    p.close()
    p.join()
    fin_paralelo = time.perf_counter()

    print(f"Tiempo de ejecucion para operacion en paralelo: {fin_paralelo - inicio_paralelo} segundos")
