import socket
import threading
import time

def hold_port():
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    port = int(__import__('os').environ.get('PORT', 10000))
    s.bind(('0.0.0.0', port))
    s.listen(1)
    time.sleep(300)
    s.close()

t = threading.Thread(target=hold_port, daemon=True)
t.start()
