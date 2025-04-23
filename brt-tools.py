import os

import subprocess

import sys

import tkinter as tk

import random

import winsound

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



def hata_mesaji(adet):

    winsound.MessageBeep(winsound.MB_ICONHAND)  # Hata sesi çal

    

    root = tk.Tk()

    root.withdraw()  # Ana pencereyi gizle



    def pencere_olustur():

        pencere = tk.Toplevel()

        pencere.title("Error")

        pencere.geometry(f"200x100+{random.randint(100, 1000)}+{random.randint(100, 800)}")

        pencere.resizable(False, False)

        

        label = tk.Label(pencere, text="Bir hata oluştu!", font=("Arial", 12), fg="red")

        label.pack(pady=20)



        button = tk.Button(pencere, text="Tamam", command=pencere.destroy)

        button.pack()



    for _ in range(adet):

        pencere_olustur()

        time.sleep(0.1)  # Yarım saniye bekleme süresi



    root.mainloop()



def main():

    print(Fore.GREEN + "Merhaba! Komutları görmek için 'help' yazın.")



    while True:

        komut = input(Fore.YELLOW + "Komut girin: ").strip().lower()



        if komut == "help":

            print(Fore.CYAN + "1 - Tarama (trm.exe)\n2 - BIOS Girme (bios.exe)\n3 - Error Şakası (error.exe)")

        elif komut == "trm.exe":

            print(Fore.MAGENTA + "Tüm programları gösteren tam ekran pencere açılıyor...")

            subprocess.run("explorer shell:AppsFolder")

        elif komut == "bios.exe":

            print(Fore.RED + "Bilgisayar yeniden başlatılıyor...")

            os.system("shutdown /r /t 0")

        elif komut == "error.exe":

            try:

                adet = int(input(Fore.CYAN + "Kaç tane error mesajı almak istiyorsunuz? "))

                hata_mesaji(adet)

            except ValueError:

                print(Fore.RED + "Geçersiz giriş! Lütfen bir sayı girin.")

        else:

            print(Fore.RED + "Bilinmeyen komut! Lütfen 'help' yazın.")



if __name__ == "__main__":

    main()
