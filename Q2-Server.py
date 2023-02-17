from socket import *
from _thread import *


def thread_client(my_client_socket, my_client_address, contact_index):
    my_client_socket.send('Welcome to the Server'.encode())
    while True:
        message = my_client_socket.recv(1024)
        if not message:
            client_sockets[contact_index][0].send('The other client is not connected anymore'.encode())
            contact_index = 0
            client_sockets.pop(1 - contact_index)
            exit(0)
            break
        if message.decode() == 'Reject':
            client_sockets[contact_index][0].send('The other client is not willing to make connection!'.encode())
            my_client_socket.close()
            break
        client_sockets[contact_index][0].send(message)
        if message.decode() == 'Bye':
            my_client_socket.close()
            break


server_port = 1026
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(1)
print('server is ready to receive...')
clients_number = 0
client_sockets = []
while True:
    client_socket, address = server_socket.accept()
    client_sockets.append((client_socket, address))
    start_new_thread(thread_client, (client_socket, address, 1 - clients_number))
    print(f'Client Number {clients_number} connected')
    clients_number += 1
server_socket.close()