from socket import *
from _thread import *


def send_message_thread(my_client_socket, stat):
    while True:
        message = input()
        if message == 'close connection':
            my_client_socket.close()
            stat[0] = 0
            exit()
            break
        my_client_socket.send(message.encode())


def receive_message_thread(my_client_socket, stat):
    while True:
        if stat[0] == 0:
            exit()
            break
        try:
            answer = my_client_socket.recv(1024).decode()
            if not answer:
                my_client_socket.close()
                exit()
            print(answer)
        except:
            pass


status = [1]
server_name = 'localhost'
server_port = 1026
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))
print(client_socket.recv(1024).decode())
start_new_thread(send_message_thread, (client_socket, status))
start_new_thread(receive_message_thread, (client_socket, status))
while True:
    pass

client_socket.close()

