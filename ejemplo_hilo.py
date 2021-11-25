from threading import Thread
import time

def func_hilo(nombre):
    print(f"Hilo {nombre}: iniciando...")
    time.sleep(nombre)
    print(f"Hilo {nombre}: Terminando")


if __name__ == '__main__':
    hilos = []
    for i in range(3):
        h = Thread(target=func_hilo, args=(i + 1, ))
        hilos.append(h)
    print(f"Main: Antes de empezar el hilo")
    for h in hilos:
        h.start()
    print(f"Main: Esperando a que los hilos terminen")
    hilos[2].join()
    print("Hilo 1 completo")
    # hilos[1].join()
    print("Hilo 2 completo")
    # hilos[2].join()
    print("Hilo 3 completo")
    print(f"Main: Todos los hilos terminaron")