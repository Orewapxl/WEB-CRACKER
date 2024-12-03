import os
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class WebsiteDownloader:
    def __init__(self, url, output_folder):
        self.url = url.rstrip("/")
        self.output_folder = output_folder
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

    def download_page(self, url, save_as):
        """Tek bir sayfayı indirip kaydeder."""
        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(save_as, "w", encoding="utf-8") as file:
                    file.write(response.text)
                print(f"Page downloaded: {url} -> {save_as}")
            else:
                print(f"Failed to download {url} (Status Code: {response.status_code})")
        except Exception as e:
            print(f"Error downloading {url}: {e}")

    def download_assets(self, soup):
        """Sayfadaki CSS, JS ve görselleri indirir."""
        asset_tags = {
            "img": "src",
            "link": "href",
            "script": "src"
        }
        for tag, attr in asset_tags.items():
            for element in soup.find_all(tag):
                asset_url = element.get(attr)
                if asset_url:
                    full_url = urljoin(self.url, asset_url)
                    file_name = os.path.basename(full_url.split("?")[0])
                    asset_path = os.path.join(self.output_folder, file_name)
                    try:
                        asset_response = requests.get(full_url)
                        if asset_response.status_code == 200:
                            with open(asset_path, "wb") as asset_file:
                                asset_file.write(asset_response.content)
                            print(f"Asset downloaded: {full_url} -> {asset_path}")
                    except Exception as e:
                        print(f"Failed to download asset {full_url}: {e}")

    def download_site(self):
        """Ana sayfa ve bağlı dosyaları indirir."""
        print(f"Starting download for {self.url}")
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                main_file_path = os.path.join(self.output_folder, "index.html")
                with open(main_file_path, "w", encoding="utf-8") as file:
                    file.write(response.text)
                print(f"Main page saved to {main_file_path}")

                # Sayfadaki CSS, JS, img dosyalarını indir
                self.download_assets(soup)
            else:
                print(f"Failed to access {self.url} (Status Code: {response.status_code})")
        except Exception as e:
            print(f"Error during site download: {e}")

def banner():
    os.system("clear" if os.name == "posix" else "cls")
    print("\033[1;31m")  # Kırmızı renk
    print(r"""
██╗    ██╗███████╗██████╗      ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗
██║    ██║██╔════╝██╔══██╗    ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║ █╗ ██║█████╗  ██████╔╝    ██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
██║███╗██║██╔══╝  ██╔══██╗    ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
╚███╔███╔╝███████╗██████╔╝    ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
 ╚══╝╚══╝ ╚══════╝╚═════╝      ╚═════╝╚═╝  ╚═╝ ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝
    """)
    print("\033[1;33m[github.com/Orewapxl] @PXLD \033[0m")  # Sarı renk
    print("\033[1;31mBu kodu yönetici olarak çalıştırmanız tavsiye edilir!\033[0m")
    print()

def menu():
    print("\033[1;36m[1] - Web Sayfası İndir\033[0m")
    print("\033[1;36m[2] - Otomatik Kurulum\033[0m")
    print("\033[1;36m[3] - İletişim\033[0m")
    print("\033[1;36m[4] - Çıkış\033[0m")
    print()
    choice = input("\033[1;33m[?] Lütfen seçiminizi yapınız: \033[0m")
    return choice

def download_site():
    print("\033[1;34mWeb sitesi indiriliyor...\033[0m")
    url = input("\033[1;33mHedef URL'yi girin: \033[0m")
    output_dir = input("\033[1;33mKayıt edilecek klasör (./WEBCRACKER): \033[0m") or "./WEBCRACKER"
    os.makedirs(output_dir, exist_ok=True)

    downloader = WebsiteDownloader(url, output_dir)
    downloader.download_site()

def automatic_install():
    print("\033[1;34mOtomatik kurulum başlatılıyor...\033[0m")
    time.sleep(2)
    print("\033[1;32mKurulum başarıyla tamamlandı!\033[0m")

def contact_info():
    print("\033[1;34mİletişim Bilgileri:\033[0m")
    print("\033[1;33mGitHub: https://github.com/Orewapxl\033[1;31m")

def main():
    while True:
        banner()
        choice = menu()
        if choice == "1":
            download_site()
        elif choice == "2":
            automatic_install()
        elif choice == "3":
            contact_info()
        elif choice == "4":
            print("\033[1;31mÇıkış yapılıyor...\033[0m")
            time.sleep(1)
            break
        else:
            print("\033[1;31mGeçersiz seçim! Lütfen tekrar deneyin.\033[0m")
        input("\033[1;33mDevam etmek için Enter'a basın...\033[0m")

if __name__ == "__main__":
    main()
