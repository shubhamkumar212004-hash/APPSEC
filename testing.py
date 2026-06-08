import socket
from concurrent.futures import ThreadPoolExecutor

target = "127.0.0.1"

def scan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)

        if sock.connect_ex((target, port)) == 0:
            print(f"[+] {port}/tcp open")

        sock.close()
    except:
        pass

with ThreadPoolExecutor(max_workers=200) as executor:
    executor.map(scan, range(1, 1001))