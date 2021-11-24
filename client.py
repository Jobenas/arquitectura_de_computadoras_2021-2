import socket
import time

SOCK_BUFFER = 1024

def exp_local(n):
    res = 1
    for i in range(n):
        res *= n
    
    return res


def exp_remoto(n):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("192.168.1.25", 5000)

    print(f"Conectando a servidor -> {server_address[0]}, puerto -> {server_address[1]}")

    sock.connect(server_address)


    try:
        sock.sendall(str(n).encode("utf-8"))
        data = sock.recv(SOCK_BUFFER)
    except KeyboardInterrupt:
        print("Usuario cerro abruptamente el programa")
        sock.close()
    except Exception as e:
        print(f"Excepcion: {e}")
    finally:
        print("Cierro conexion")
        sock.close()
    
    return  int(data.decode('utf-8'))


if __name__ == '__main__':
    print("Iniciando programa")

    print("Enviando valor a servidor")
    res = exp_remoto(4)
    print(f"Resultado es {res} y tipo es {type(res)}")

    print("Fin del programa")