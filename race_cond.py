import time
import concurrent.futures
import threading

class FakeDb:
    def __init__(self):
        self.value = 0
    
    def update(self, name):
        print(f"Thread {name}: empezando update")
        local_copy = self.value
        local_copy += 1
        # print(f"Thread {name} esta escribiendo sobre la db")
        self.value = local_copy
        print(f"Threading {name} ha escrito en la db")
        time.sleep(0.1)
        print(f"Thread {name}: terminando update")

    
if __name__ == "__main__":
    workers = 8
    db = FakeDb()
    print(f"Valor inicial de la base de datos: {db.value}")
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        for index in range(workers):
            executor.submit(db.update, index)
    print(f"Valor final de la base de datos: {db.value}")
