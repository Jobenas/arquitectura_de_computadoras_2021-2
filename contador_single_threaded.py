import time


CUENTA = 50000000

def cuenta(n):
    while n > 0:
        n -=1


if __name__ == '__main__':
    inicio = time.perf_counter()
    cuenta(CUENTA)
    fin = time.perf_counter()

    print(f"Tiempo de ejecucion: {fin - inicio} segundos")
