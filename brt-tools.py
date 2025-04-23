import os
import subprocess
import sys
import tkinter as tk
import random
import colorama
from colorama import Fore
import time  # Zaman gecikmesi için eklendi

# Gerekli modülleri yükle
def modül_yükle(modül_adı):
    try:
        __import__(modül_adı)
    except ImportError:
        print(f"{modül_adı} modülü eksik, yükleniyor...")
        subprocess.run([sys.executable, "-m", "pip", "install", modül_adı])
        __import__(modül_adı)

modül_yükle("colorama")

colorama.init(autoreset=True)

def main():
    print(Fore.GREEN + "Merhaba! Komutları görmek için 'help' yazın.")

    while True:
        komut = input(Fore.YELLOW + "Komut girin: ").strip().lower()

        if komut == "help":
            print(Fore.CYAN + "1 - Tarama (trm.exe)\n2 - BIOS Girme (bios.exe)")
        elif komut == "trm.exe":
            print(Fore.MAGENTA + "Tüm programları gösteren tam ekran pencere açılıyor...")
            subprocess.run("explorer shell:AppsFolder")
        elif komut == "bios.exe":
            print(Fore.RED + "Bilgisayar yeniden başlatılıyor...")
            os.system("shutdown /r /t 0")
        else:
            print(Fore.RED + "Bilinmeyen komut! Lütfen 'help' yazın.")

if __name__ == "__main__":
    main()
