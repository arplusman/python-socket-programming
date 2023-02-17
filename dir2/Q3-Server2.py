from socket import *
from os.path import isfile
from os import getcwd
from mimetypes import guess_type


def make_server_to_server_connection(ip, port, file_path):
    connection_socket = socket(AF_INET, SOCK_STREAM)
    connection_socket.connect((ip, port))
    request_message = f'GET {file_path} HTTP/1.1\r\nUser-Agent: Server'
    connection_socket.send(request_message.encode())
    message = connection_socket.recv(4000000)
    return message


server_host = '0.0.0.0'
server_port = 8000

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server_socket.bind((server_host, server_port))
server_socket.listen(1)
print(f'listening on port {server_port} ...')

while True:
    client_connection, client_address = server_socket.accept()
    request = client_connection.recv(2048).decode()
    attributes = {}
    path = request.split('\n')[0].split(' ')[1]
    if path == '/favicon.ico':
        client_connection.sendall('HTTP/1.0 200 OK\r\n\r\n'.encode())
        client_connection.close()
        continue
    for attribute in request.split('\n'):
        flag = attribute.split(': ')
        if len(flag) < 2:
            continue
        attributes[flag[0]] = flag[1]
    content = ''
    content_type = ''
    if isfile(getcwd() + path):
        file = open('.' + path, 'rb')
        content = file.read()
        content_type = guess_type('.' + path)[0]
        file.close()
        response = 'HTTP/1.1 200 OK\r\n'
        response = response + 'Content-Type: ' + content_type + '\r\n'
        response = response + 'Content-length: ' + str(len(content)) + '\r\n\r\n'
        response = response.encode() + content
        client_connection.sendall(response)
    elif attributes['User-Agent'] == 'Server':
        response = 'HTTP/1.1 404 NOT FOUND\r\n\r\n'
        response = response + 'FILE NOT FOUND'
        client_connection.sendall(response.encode())
    else:
        response_from_other_servers = make_server_to_server_connection('127.0.0.1', 7000, path)
        if str(response_from_other_servers).split('\\r\\n')[0].split(' ')[1] == '200':
            client_connection.sendall(response_from_other_servers)
        else:
            response_from_other_servers = make_server_to_server_connection('127.0.0.1', 9000, path)
            client_connection.sendall(response_from_other_servers)

client_connection.close()