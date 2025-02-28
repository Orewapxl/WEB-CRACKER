import os
import time
import requests
import hashlib
import random
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class WebsiteDownloader:
    def __init__(self, url, output_folder):
        self.url = url.rstrip("/")
        self.output_folder = output_folder
        self.headers = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:118.0) Gecko/20100101 Firefox/118.0",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
        ]
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

    def download_page(self, url, save_as):
        try:
            response = requests.get(url, headers={"User-Agent": random.choice(self.headers)})
            response.raise_for_status()  
            with open(save_as, "w", encoding="utf-8") as file:
                file.write(response.text)
            print(f"Page downloaded: {url} -> {save_as}")
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred for {url}: {http_err}")
        except Exception as e:
            print(f"Error downloading {url}: {e}")

    def download_assets(self, soup):
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
                    
                    file_name = hashlib.md5(full_url.encode()).hexdigest() + os.path.splitext(full_url)[1]
                    asset_path = os.path.join(self.output_folder, file_name)
                    try:
                        asset_response = requests.get(full_url, headers={"User-Agent": random.choice(self.headers)})
                        if asset_response.status_code == 200:
                            with open(asset_path, "wb") as asset_file:
                                asset_file.write(asset_response.content)
                            print(f"Asset downloaded: {full_url} -> {asset_path}")
                        
                            
                            element[attr] = file_name
                    except Exception as e:
                        print(f"Failed to download asset {full_url}: {e}")
    
       
        updated_html = soup.prettify()
        main_file_path = os.path.join(self.output_folder, "index.html")
        with open(main_file_path, "w", encoding="utf-8") as file:
            file.write(updated_html)

    def download_site(self):
        print(f"Starting download for {self.url}")
        try:
            response = requests.get(self.url, headers={"User-Agent": random.choice(self.headers)})
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            main_file_path = os.path.join(self.output_folder, "index.html")
            with open(main_file_path, "w", encoding="utf-8") as file:
                file.write(response.text)
            print(f"Main page saved to {main_file_path}")
            
            print(f"Downloading assets...")
            self.download_assets(soup)
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as e:
            print(f"Error during site download: {e}")

def banner():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")
    
    print("\033[1;31m")
    print(r"""
██╗    ██╗███████╗██████╗      ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗
██║    ██║██╔════╝██╔══██╗    ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║ █╗ ██║█████╗  ██████╔╝    ██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
██║███╗██║██╔══╝  ██╔══██╗    ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
╚███╔███╔╝███████╗██████╔╝    ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
 ╚══╝╚══╝ ╚══════╝╚═════╝      ╚═════╝╚═╝  ╚═╝ ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝
    """)
    print("\033[1;33m                                                @PXLD\033[0m")
    print("\033[1;33m   [github.com/Orewapxl]\033[0m") 
    print("\033[1;31mBu kodu yönetici olarak çalıştırmanız tavsiye edilir!\033[0m")
    print()

def menu():
    print("\033[1;31m[1] - Web Sayfası İndir\033[0m")
    print("\033[1;31m[2] - Otomatik Kurulum\033[0m")
    print("\033[1;31m[3] - İletişim\033[0m")
    print("\033[1;31m[4] - Çıkış\033[0m")
    print()
    choice = input("\033[1;31m[?] Lütfen seçiminizi yapınız: \033[0m")
    return choice

def download_site():
    url = input("\033[1;33mHedef URL'yi girin: \033[0m")
    output_dir = input("\033[1;33mKayıt edilecek klasör (./WEBCRACKER): \033[0m") or "./WEBCRACKER"
    print("\033[1;31mWeb sitesi indiriliyor...\033[0m")
    time.sleep(2)
    os.makedirs(output_dir, exist_ok=True)

    downloader = WebsiteDownloader(url, output_dir)
    downloader.download_site()

def automatic_install():
    print("\033[1;34mOtomatik kurulum başlatılıyor...\033[0m")
    time.sleep(2)
    print("\033[1;32mKurulum başarıyla tamamlandı!\033[0m")

def contact_info():
    print("\033[1;34mİletişim Bilgileri:\033[0m")
    print("\033[1;31mGitHub: https://github.com/Orewapxl\033[0m")

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
