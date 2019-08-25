import socket
import sys
import threading

try:
    hostname = socket.gethostname()
    port = 5990
    client_socket = socket.socket()  # instantiate
    client_socket.connect((hostname, port))  # connect to the server

    print("Success")
    Name = input("Enter your name\n")
    client_socket.send(Name.encode())
    print(client_socket.recv(1024).decode())
    def send():
        while True:
            Message = input()
            if(Message != 'Bye'):
                client_socket.send(Message.encode())
            else:
                break
        client_socket.close()
    def receive():
        while True:
            try:
                Data = client_socket.recv(1024).decode()
            except:
                print("connection lost")
                break
            print("\n" +"Server :" +Data)
            # print(client_socket.__getstate__())
        print("Thank You for Connecting")
        input()
    t1 = threading.Thread(target=receive)
    t2=threading.Thread(target=send)
    t1.start()
    t2.start()


except:
    print("Unexpected error:", sys.exc_info()[0])
    client_socket.close()
    input()



