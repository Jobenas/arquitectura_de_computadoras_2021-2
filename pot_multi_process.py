from multiprocessing import Pool
import random
import time

def pot(x):
    val = 1
    for i in range(x):
        val *= x
    
    return val

if __name__ == '__main__':
    nums = [x for x in range(30000, 30032)]

    res_serial = [] 
    inicio_serial = time.perf_counter()
    for num in nums:
        res_serial.append(pot(num))
    fin_serial = time.perf_counter()
    
    inicio_paralelo2 = time.perf_counter()
    p = Pool(processes=2)
    res_paralelo2 = p.map(pot, nums)
    p.close()
    p.join()
    fin_paralelo2 = time.perf_counter()
    
    inicio_paralelo8 = time.perf_counter()
    p = Pool(processes=8)
    res_paralelo8 = p.map(pot, nums)
    p.close()
    p.join()
    fin_paralelo8 = time.perf_counter()

    print(f"Tiempo de ejecucion serial: {fin_serial - inicio_serial} segundos")
    print(f"Tiempo de ejecucion paralela con 2 procesos: {fin_paralelo2 - inicio_paralelo2} segundos")
    print(f"Tiempo de ejecucion paralela con 8 procesos: {fin_paralelo8 - inicio_paralelo8} segundos")
