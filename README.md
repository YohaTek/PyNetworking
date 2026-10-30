# PyNetworking

A small, self-contained Python example of socket programming: a threaded TCP
server and a matching client that exchange length-prefixed text messages over
the local network. It is intended as a readable starting point for learning how
client-server connections are established and how messages are framed.

No third-party packages are required — only the Python standard library.

## Requirements

- Python 3.8 or newer (uses only `socket` and `threading`)
- Two terminals (or two machines on the same network)

## Project layout

```
.
├── client.py   # Connects to the server and sends a few sample messages
├── server.py   # Listens for connections and handles each client on a thread
└── README.md
```

## How the two sides work

Both scripts follow the classic socket lifecycle. On the server side:

1. **Create socket** — `socket.socket(AF_INET, SOCK_STREAM)` opens a TCP socket.
2. **Bind socket** — the socket is bound to an `(IP, port)` address pair.
3. **Listen** — `listen()` marks the socket as ready to accept connections.
4. **Accept** — `accept()` blocks until a client connects and returns a new
   socket for that client.
5. **Handle clients** — the server receives and processes messages, one thread
   per client.
6. **Close socket** — the connection is closed after a disconnect message.

The client performs the shorter path: create socket, connect to the server, then
send and receive messages.

### Message framing

TCP is a byte stream, so each message is prefixed with a fixed-length header:

- `HEADER = 64` — every message is preceded by a 64-byte header containing the
  message length in ASCII, right-padded with spaces.
- `FORMAT = 'utf-8'` — the payload is encoded as UTF-8 text.
- The server reads 64 bytes, converts the header to an integer, then reads
  exactly that many bytes for the payload.

Sending the literal string `Disconnect` tells the server to close the
connection.

## Running it

1. Start the server in one terminal:

   ```sh
   python server.py
   ```

   It prints its hostname, the IP address it bound to, and a listening message.

2. In a second terminal, edit the `SERVER` constant in `client.py` if needed so
   it matches the IP printed by the server, then run:

   ```sh
   python client.py
   ```

   The client sends three sample messages, waiting for Enter between each one so
   you can watch the server output as they arrive.

Both scripts share `PORT = 5050`; change it in both files if the port is already
in use.

## Cloning

```sh
git clone https://github.com/YohaTek/PyNetworking.git
cd PyNetworking
```

## Known limitations

- The client's server address is hard-coded (`SERVER`), and the sample messages
  are placeholders — adjust them for your own experiment.
- The server only receives messages; it does not send replies yet.
- Messages are plain text and unauthenticated, so this should only be used on a
  trusted local network, never on the public internet.

## Contributing

Contributions are welcome. Open an issue to report a problem or suggest a
feature, or send a pull request to improve the examples.
