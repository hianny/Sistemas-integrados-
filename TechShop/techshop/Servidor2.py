import threading
import socket

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 10002))  # Porta do servidor
    server.listen()
    print("Servidor1 rodando na porta 10001...")

    # Conecta-se ao broker
    broker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    broker.connect(("broker", 4000))  # Conectando ao broker na porta 4000
    print("Servidor1 conectado ao Broker")

    while True:
        client, addr = server.accept()
        print(f"Conectado: {addr}")

        # Passa o broker para a função de tratamento de mensagens
        thread = threading.Thread(target=tratamentoMensagens, args=[client, broker])  # Passando dois parâmetros
        thread.start()

def tratamentoMensagens(client, broker):  # Aceitando dois parâmetros
    while True:
        try:
            msg = client.recv(2048)
            if not msg:
                break
            print(f"Mensagem recebida de {client}: {msg.decode()}")

            # Repassa a mensagem para o broker
            broker.send(msg)

        except:
            print("Cliente desconectado")
            client.close()
            break

if __name__ == "__main__":
    main()
