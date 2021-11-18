import socket

SOCK_BUFFER = 1024

def exp(n):
    res = 1
    for i in range(n):
        res *= n
    
    return res

if __name__ == "__main__":
    # creamos el socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ("0.0.0.0", 5000)
    print(f"Iniciando servidor en direccion -> {server_address[0]}, puerto -> {server_address[1]}")
    sock.bind(server_address)

    sock.listen(5)

    while True:
        print("Esperando conexiones")

        conn, client_address = sock.accept()

        try:
            data = conn.recv(SOCK_BUFFER)
            if data:
                res = exp(int(data.decode("utf-8")))
                print(f"Recibimos {int(data)}, retornamos {res}")
                conn.sendall(str(res).encode("utf-8"))
            # else:
            #     break
        except Exception as e:
            print(f"Excepcion: {e}")
        finally:
            print("Cliente cerro la conexion")
            conn.close()