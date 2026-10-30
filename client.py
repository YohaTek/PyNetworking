import socket

PORT = 5050
#SERVER = "172.31.99.17"
SERVER = "127.0.1.1"

FORMAT = 'utf-8'
HEADER = 64

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDR = (SERVER, PORT)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


def main():
    client.connect(ADDR)
    send("Hellow world!")
    input()
    send("Hello Everbody")
    input()
    send("Hello Yohannes")


if __name__ == "__main__":
    main()
