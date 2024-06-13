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
close = "Disconnect"
SERVER = socket.gethostbyname(socket.gethostname())
hostname = socket.gethostname()
print(f'current server {hostname} running')
print(f"IP Address {SERVER} Running")


ADDR = (SERVER,PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    #creation of new socket ,

server.bind(ADDR)
    #binding the created socket to the ADDR, which is to the ip address and port of the server

def handle_client(conn,addr):

    print(f"NEW client {addr} connected")
    
    connection = True
    while connection:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length =int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == close:
                print(f"the message is: {msg}")
                connection = False
            print(f"[{addr}] {msg}")
    conn.close()
        
def start():
    server.listen()
    print(f"Listening {SERVER}")
    while True:
        conn,addr = server.accept();
        thread = threading.Thread(target = handle_client, args=(conn,addr))
        thread.start()
        print(threading.activeCount()-1)

print('Starting: Server is starting ...')
start()        

        














