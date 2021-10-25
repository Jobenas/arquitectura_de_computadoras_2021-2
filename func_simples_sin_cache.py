import time
import random

def suma(x):
    return x + x


if __name__ == '__main__':
    lista = [random.randint(1, 1000) for i in range(50)]
    execs = []
    for item in lista:
        inicio = time.perf_counter()
        res = suma(item)
        fin = time.perf_counter()
        execs.append(fin - inicio)

    exec_avg = 0
    for exec in execs:
        exec_avg += exec
    exec_avg /= len(execs)

    print(f"Tiempo promedio de ejecucion {exec_avg} segundos")
    
    # print(f"El resultado de la operacion es {res}, y ha tomado {fin - inicio} segundos")