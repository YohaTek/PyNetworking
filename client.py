import socket

PORT = 5050
SERVER = "172.31.99.17"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDR = (SERVER,PORT)

client.connect(ADDR)
