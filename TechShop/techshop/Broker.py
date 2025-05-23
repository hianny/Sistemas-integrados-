import threading
import socket

# Lista para armazenar os clientes conectados
clients = []
servers = []

def main():
    broker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    broker.bind(("0.0.0.0", 4000))  # Porta do broker
    broker.listen()
    print("Broker rodando na porta 4000...")

    while True:
        client, addr = broker.accept()
        print(f"Cliente conectado ao Broker: {addr}")

        # Adiciona o cliente à lista de clientes conectados
        clients.append(client)

        # Cria uma nova thread para tratar as mensagens
        thread = threading.Thread(target=tratamentoMensagens, args=[client])
        thread.start()

def tratamentoMensagens(client):
    while True:
        try:
            msg = client.recv(2048)
            if not msg:
                break
            print(f"Mensagem recebida do cliente: {msg.decode()}")

            # Repassa para todos os outros clientes
            broadcast(msg, client)

        except:
            print("Erro de comunicação com o cliente.")
            clients.remove(client)
            client.close()
            break


def conectar_servidores():
    servidores = [("localhost", 10001), ("localhost", 10002)]
    for srv in servidores:
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.connect(srv)
            servers.append(server_socket)
            print(f"Conectado ao servidor {srv[0]}:{srv[1]}")
        except:
            print(f"Não foi possível conectar ao servidor {srv[0]}:{srv[1]}")

def broadcast(msg, client):
    # Envia para os outros clientes
    for other_client in clients:
        if other_client != client:
            try:
                other_client.send(msg)
            except:
                clients.remove(other_client)
                other_client.close()

    # Envia para os servidores
    for server in servers:
        try:
            server.send(msg)
        except:
            print("Erro na comunicação com o servidor.")
            servers.remove(server)
            server.close()


if __name__ == "__main__":
    conectar_servidores()
    main()
