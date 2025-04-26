import os
import colorama
from colorama import Fore

colorama.init(autoreset=True)

def ekran_temizle():
    # Konsolu temizlemek için
    if os.name == 'nt':  # Windows için
        os.system('cls')
    else:  # Linux/Unix/Android için
        os.system('clear')

def program_baslangici():
    # Konsolu temizle ve metni yazdır
    ekran_temizle()
    print(Fore.CYAN + """
  ____  _____ _______   _______ ____   ____  _       _____ 
 |  _ \\|  __ \\__   __| |__   __/ __ \\ / __ \\| |     / ____|
 | |_) | |__) | | |       | | | |  | | |  | | |    | (___  
 |  _ <|  _  /  | |       | | | |  | | |  | | |     \\___ \\ 
 | |_) | | \\ \\  | |       | | | |__| | |__| | |____ ____) |
 |____/|_|  \\_\\ |_|       |_|  \\____/ \\____/|______|_____/
""")
    print(Fore.GREEN + "Merhaba! Komutları görmek için 'help' yazın.")

def main():
    # Program başlangıcı
    program_baslangici()

    while True:
        komut = input(Fore.YELLOW + "Komut girin: ").strip().lower()

        if komut == "help":
            print(Fore.CYAN + "1 - Tarama (trm.exe)\n2 - BIOS Girme (bios.exe)")
        elif komut == "trm.exe":
            print(Fore.MAGENTA + "Tüm programları gösteren tam ekran pencere açılıyor...")
            os.system("explorer shell:AppsFolder")
        elif komut == "bios.exe":
            print(Fore.RED + "Android cihaz yeniden başlatılıyor...")
            os.system("reboot")  # Android için yeniden başlatma
        else:
            print(Fore.RED + "Bilinmeyen komut! Lütfen 'help' yazın.")

if __name__ == "__main__":
    main()
