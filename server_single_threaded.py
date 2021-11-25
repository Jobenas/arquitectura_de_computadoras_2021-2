import socket

SOCK_BUFFER = 4

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ("0.0.0.0", 5000)
    print(f"Iniciando servidor en direccion -> {server_address[0]}, puerto -> {server_address[1]}")
    sock.bind(server_address)

    sock.listen(5)

    while True:
        print("Esperando conexiones")
        
        conn, client_address = sock.accept()

        try:
            print(f"Conexion de {client_address}")

            while True:
                data = conn.recv(SOCK_BUFFER)
                if data:
                    print(f"Recibi {data} de {client_address}")
                    conn.sendall(data)
                else:
                    break
        except Exception as e:
            print(f"Excepcion: {e}")
        finally:
            print("Cliente ha cerrado la conexion")
            conn.close()