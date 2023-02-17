from socket import *


server_port = 1026
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', server_port))
server_socket.listen(1)
print('server is ready to receive...')
clients_number = 0
client_socket_1, address_1 = server_socket.accept()
client_socket_1.send('Welcome to the Server'.encode())
client_socket_2, address_2 = server_socket.accept()
client_socket_2.send('Welcome to the Server'.encode())
# handshaking
message = client_socket_1.recv(1024)
print(f'message {message.decode()} received from cleint 1')
client_socket_2.send(message)
message = client_socket_2.recv(1024)
if message.decode() == 'Reject':
    client_socket_1.send('The other client is not willing to make connection!'.encode())
    client_socket_2.close()
else:
    client_socket_1.send(message)
# start chat
client_1_turn = True
while True:
    if client_1_turn:
        message = client_socket_1.recv(1024)
        client_socket_2.send(message)
        if message.decode() == 'Bye':
            client_socket_1.close()
            # wait for another user
            client_socket_1, address_1 = server_socket.accept()
        elif message.decode() == 'close connection':
            client_socket_1.close()
            client_socket_2.send('The other client is not connected anymore!'.encode())
            client_socket_1, address_1 = server_socket.accept()
    else:
        message = client_socket_2.recv(1024)
        client_socket_1.send(message)
        if message.decode() == 'Bye':
            client_socket_2.close()
            # wait for another user
            client_socket_2, address_2 = server_socket.accept()
        elif message.decode() == 'close connection':
            client_socket_2.close()
            client_socket_1.send('The other client is not connected anymore!'.encode())
            client_socket_2, address_2 = server_socket.accept()

server_socket.close()
