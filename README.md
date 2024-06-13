# PyNetworking

This Python repository delves into the fascinating realm of computer networking, empowering you to establish robust client-server connections using sockets.

Key Features:

Socket Programming Fundamentals: Gain a solid understanding of sockets, the cornerstone of network communication, and leverage them to construct effective client-server interactions.
Client-Server Connection Establishment: Master the art of creating reliable connections between clients and servers, enabling data exchange and seamless communication.

## Socket Programming

The procedure to create and use sockets to connect with other devices differs for the Client and Server devices. For the Server, the following procedure applies
### Create Cocket
The server must create socket first
### Bind Socket
Then the server binds its address (ip, and port number) to the socket it has created
### Listen for connections
Then Actively listens to Clients who want to connect to the server, the function that does the listening is listen().
### Accept client connections
When request for connection comes, then the server accepts. The function is accept().
### Handle Clients
After accepting the connection, the server needs to handle the clients. Receiving and sending packets to/from the clients is done here.
### Close Socket
The final stage is to terminate the connection, and the server should be able to do that safely.

These are the processes one should undergo to successfully connent create the server and connect to the clients.
In the client side, the only processes needed are creating socket, connecting to the server, and start sending and receiving packets.

## Clone the Repository:

git clone https://YohaTek/PyNetworking.git

Navigate to the Project Directory:
cd PyNetworking

## Set Up Your Development Environment:
Ensure you have Python (version 3 recommended) and Git installed on your system.
The modules imported are already found in python installation, so no need for additional packages.

client.py: Contains the code for the client-side application, responsible for initiating connections and sending data to the server.
server.py: Houses the server-side code, tasked with listening for incoming connections, receiving data from clients, and potentially responding.


I warmly welcome contributions from the Python and networking community! Feel free to submit pull requests to enhance the repository's functionality or provide valuable feedback through issues.
