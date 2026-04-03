import socket
import threading
import time
import os

def hold_port():
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    port = int(os.environ.get('PORT', 10000))
    s.bind(('0.0.0.0', port))
    s.listen(5)
    print(f"Preload holding port {port}")
    # Keep alive until Rasa takes over
    while True:
        try:
            conn, addr = s.accept()
            conn.close()
        except:
            break

t = threading.Thread(target=hold_port, daemon=True)
t.start()
time.sleep(2)  # Give it a moment to bind before Rasa starts
