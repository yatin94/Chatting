
import socket
import threading
import time

# sock.setsockopt(SOL_SOCKET,SO_REUSEADDR, 1)
name1 = ""
hostname = socket.gethostname()
port = 5990
print(hostname)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((hostname, port))
sock.listen(5)
print("Listening")
def initialize():
    while True:
        conn,address = sock.accept()
        print("Connection from: " + str(address))
        name = conn.recv(1024).decode()
        name1 = name
        print(name1+" Ready")
        conn.send((name1+" Ready").encode())
        t2 = threading.Thread(target=receive,args=(name1,conn,))
        t3 = threading.Thread(target=send,args=(name1,conn,))
        t2.start()
        t3.start()
    # return name1
# conn, address = sock.accept()
# print("Connection from: " + str(address))


def receive(name1,conn):
    while True:
        try:
            data = conn.recv(1024).decode()
        except:
            print("Connection Closed.....")
            break
        print("\n" +name1+" : "+data) 
    print(name1+" Disconnected")     
            
def send(name1,conn):
    while True:
        try:
            message = input()
            conn.send(message.encode())
        except:
            # print("No messages to send")
            break
t1 = threading.Thread(target=initialize) 



t1.start()





