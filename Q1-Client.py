from socket import *
from time import time
from sys import getsizeof

server_name = '168.119.202.153'
server_port = 200

print('starting to send 10 separate messages 10 times and calculate throughput by' +
      'calculating mean of throughputs...')
client_socket = socket(AF_INET, SOCK_DGRAM)
message = 'throughput'
sum_of_thorughputs = 0
for i in range(10):
    start_time = time()
    client_socket.sendto(message.encode(), (server_name, server_port))
    answer, server_address = client_socket.recvfrom(200)
    print(answer.decode())
    end_time = time()
    sum_of_thorughputs += getsizeof(message) / (end_time - start_time)
throughput = sum_of_thorughputs / 10
print(f'so the throughput is equal to {throughput}')
client_socket.close()

print('-' * 20)
print('starting to send 10 separate messages 10 times and calculate throughput by ' +
      'calculating all_time / all_bytes_received...')
client_socket = socket(AF_INET, SOCK_DGRAM)
message = 'throughput'
start_time = time()
for i in range(10):
    client_socket.sendto(message.encode(), (server_name, server_port))
    answer, server_address = client_socket.recvfrom(200)
    print(answer.decode())
client_socket.close()
end_time = time()
print(f'this program took {end_time - start_time} milliseconds to bde done' +
      f' and {getsizeof(message) * 10} bytes were sent at all')
throughput = getsizeof(message) * 10 / (end_time - start_time)
print(f'so the throughput is equal to {throughput}')
client_socket.close()

print('-' * 20)
print('starting to send a message which includes 10 times of the word \"throughput\"')
client_socket = socket(AF_INET, SOCK_DGRAM)
message = 'throughput' * 10
start_time = time()
client_socket.sendto(message.encode(), (server_name, server_port))
answer, server_address = client_socket.recvfrom(200)
print(answer.decode())
end_time = time()
throughput = getsizeof(message) / (end_time - start_time)
print(f'so the throughput is equal to {throughput}')
client_socket.close()

print('-' * 20)
print('starting to send a message which includes 100 times of the word \"throughput\"')
client_socket = socket(AF_INET, SOCK_DGRAM)
message = 'throughput' * 100
start_time = time()
client_socket.sendto(message.encode(), (server_name, server_port))
answer, server_address = client_socket.recvfrom(200)
print(answer.decode())
end_time = time()
throughput = getsizeof(message) / (end_time - start_time)
print(f'so the throughput is equal to {throughput}')
client_socket.close()
