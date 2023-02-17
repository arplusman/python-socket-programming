
# Python Socket Programming Assignment
In this assignment, 3 socket programming questions in python are solved. descciption of every question is stated below.
## Question 1: Throughput Calculation
This question in intended to calculate throughput using UDP protocol. There are [Client](./Q1-Client.py) and [Server](./Q1-Server.py) files which act a client and server respectively. Every time, client sends a message to the server, and server sends back that same message to the client as soon as receiving the message. Now, throughput will be caclulated in 4 different situation that will be explained below:
1. send the "troghput" phrase in 10 different times from client to server and calculate mean of throughput.
2. send the "throughput" phrase from server to client, and after receiving the response, send it again. repeat this step 10 times and calculate throughput by diving all spent time by all exchanged bytes.
3. send only one message containing 10 times of "throughput" phrase from clinet to server and caclulate throughput.
4. send only one message containing 10 times of "throughput" phrase from clinet to server and caclulate throughput.

__Note:__ for getting reasonable results, run client and server codes in different devices.

## Question 2: Chatroom
A simple Chatroom is implemented in python using TCP protocol. It is contained of [Client](./Q2-Client.py) and Server files. Server file is implemented in two different ways. There is [one](./Q2-Server.py) that used multi-threading and the [one](./Q2-Server-Without-Thread.py) that did not use multithreading. For running the project, you should run only one of the server files and run two samples of the client file. At first, first client sends "Hi" message to the server, and server sends this message to second client. Second client, if accepting the chat, sends "Hi" to server, and server sends it to first client. Otherwise, second client Should send "Reject" to the server, and server informs the first client that the second client is not willing to establish connection. Also, if one of the clients is disconnetced, the server should inform the other client. This chat will be continued untill one of the clients sends the "Reject" word.

## Questoin 3: HTTP File
in this question, three smiliar servers are implemented in three different folders, named [dir1](./dir1), [dir2](./dir2), [dir3](./dir3), and each of them can only access files of their own directory. Every server receives an `HTTP GET` request that contains relative address of a file. If the file existed in the directory of that server, it should be send as an `HTTP` response to the client. But, if the file does not exist, The server should request the file from two other servers, and if they have had the file, they should send it to requesting server. If that file existed in other server files, the requesting server should send it as an `HTTP` response to the client. But, if it does not exist, the server should send an `HTTP` response with a proper `Response Code`. 

__Note:__ for requesting, no python client file is neede, and you can use web browser to send `HTTP` requests. Also, requested files are not neccessarily text file, and they can be any binary file e.g. audio, video, etc.
