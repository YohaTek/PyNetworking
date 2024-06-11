import socket
import threading

#create socket,
#bind socket
#listen
#accept
#handle message
#close socket
# these are the processes one should undergo to successfully connent create the server and connect to the clients


HEADER = 64
FORMAT = 'utf-8'
PORT = 5050
close = "!Disconnect"
SERVER = socket.gethostbyname(socket.gethostname())
print(f"current Server:{socket.gethostname()}")
print(f"IP Address:{SERVER}")


ADDR = (SERVER,PORT)

server = socket.socket(socket.AF_INET, SOCK_STREAM) 
    #creation of new socket ,

server.bind(ADDR)
    #binding the created socket to the ADDR, which is to the ip address and port of the server

def handle_client():
    connection = True
    while connection:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        msg_length =int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg == close:
            print(f"the message is: {msg}")
            connection = False
        else
            print(f"the message is: {msg}")

    server.close()
        
def start():
    while True:
        conn,addr = server.accept();
        thread = threading.Thread(target = handle_client, args(conn,addr))
        thread.start()
        print(threading.activeCount()-1)

        

        














