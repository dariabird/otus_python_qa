import json
import socket

HOST = "127.0.0.1"
PORT = 14985

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    print(f"Binding server on {HOST}:{PORT}")
    s.bind((HOST, PORT))
    s.listen()

    conn, addr = s.accept()
    with conn:
        conn.send("Hello, I am server!\n".encode("utf-8"))

        while True:
            data = conn.recv(4096)
            print(f"Received {data} from {addr}")

            data = data.decode("utf-8")
            data = data.rstrip().split("\r\n")[2:]
            tuples = [tuple(d.split(": ")) for d in data]
            j_data = json.dumps(dict(tuples))
            resp = bytes(f'''HTTP/1.1 200 OK
            Content-Type: application/json; charset=utf-8
            {j_data}''', encoding="utf8")
            conn.send(resp)
            print(f"Send: {j_data}")

            conn.close()
            print(f"Closed:{addr}")
            break
