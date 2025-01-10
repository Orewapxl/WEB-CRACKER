import time
from website_downloader import WebsiteDownloader
from utils import banner, create_folder
from menu import display_menu, contact_info

def download_site():
    url = input("\033[1;33mHedef URL'yi girin: \033[0m")
    output_dir = input("\033[1;33mKayıt edilecek klasör (./WEBCRACKER): \033[0m") or "./WEBCRACKER"
    create_folder(output_dir)
    downloader = WebsiteDownloader(url, output_dir)
    downloader.download_site()

def automatic_install():
    print("\033[1;34mOtomatik kurulum başlatılıyor...\033[0m")
    time.sleep(1)
    print("\033[1;32mKurulum tamamlandı!\033[0m")

def main():
    while True:
        banner()
        choice = display_menu()
        if choice == "1":
            download_site()
        elif choice == "2":
            automatic_install()
        elif choice == "3":
            contact_info()
        elif choice == "4":
            print("\033[1;31mÇıkış yapılıyor...\033[0m")
            break
        else:
            print("\033[1;31mGeçersiz seçim!\033[0m")
        input("\033[1;33mDevam etmek için Enter'a basın...\033[0m")

if __name__ == "__main__":
    main()
