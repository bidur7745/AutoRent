import socket
import threading
import os

def hold_port():
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    port = int(os.environ.get('PORT', 10000))
    s.bind(('0.0.0.0', port))
    s.listen(5)
    print(f"Preload holding HTTP port {port}")
    while True:
        try:
            conn, addr = s.accept()
            conn.sendall(b"HTTP/1.1 200 OK\r\nContent-Length: 2\r\n\r\nOK")
            conn.close()
        except:
            break

t = threading.Thread(target=hold_port, daemon=True)
t.start()

import time
time.sleep(2)
