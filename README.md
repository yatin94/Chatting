# Chatting
Python Chatting application using TCP. This Application uses Sockets and Threads libraries of python 3.7+

Before running the application 2 libraries needs to be downloaded that are:
1. Sockets (pip install sockets)
2. Threads (pip install threads)

Socket is used to communicate between 2 nodes using TCP whereas Threads are used to start a bi directional communication.

Steps to run the application:

First run server.py which will initiate the server. Once the  server is running client can be initialized by opening client.py. The main feature is n number of clients can be initialized and will be given access on the basis of first come first served basis. 

Even if the client is shut down the server will keep running and will change  to listen mode to wait for incoming requests.

To quit the client has to send 'Bye' and the connection will be closed between that specific server and client.
