import threading
import socket 
def main():
    client =  socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        client.connect(("localhost",4000))
    except:
        return print('nao foi possivel conectar ao servidor')
    
    username = input('usuario: ')
    print("Usuario conectado")

    thread1 = threading.Thread(target=recebeMensagem,args=[client])
    thread2 = threading.Thread(target=mandaMensagem,args=[client,username])
    thread1.start()
    thread2.start()

def recebeMensagem(client):
    while True:
        try:
            mensagem = client.recv(2048).decode('utf-8')
            print(fr"{mensagem}")
        except:
            print("nao foi possivel permanecer conectado no servidor")
            print("pressione <enter> para continuar!")
            client.close()
            break

        
def mandaMensagem(client,username):
    while True:
        try:
            mensagem = input("\n:")
            client.send(fr"<<{username}>> {mensagem}".encode('utf-8'))
        except:
            return

main()