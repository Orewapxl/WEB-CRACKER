import os
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
        os.makedirs(output_folder, exist_ok=True)

    def download_page(self, url, save_as):
        try:
            response = requests.get(url, headers={"User-Agent": random.choice(self.headers)})
            response.raise_for_status()
            with open(save_as, "w", encoding="utf-8") as file:
                file.write(response.text)
            print(f"Page downloaded: {url} -> {save_as}")
        except Exception as e:
            print(f"Error downloading {url}: {e}")

    def download_assets(self, soup):
        asset_tags = {"img": "src", "link": "href", "script": "src"}
        for tag, attr in asset_tags.items():
            for element in soup.find_all(tag):
                asset_url = element.get(attr)
                if asset_url:
                    full_url = urljoin(self.url, asset_url)
                    file_name = hashlib.md5(full_url.encode()).hexdigest() + os.path.splitext(full_url)[1]
                    asset_path = os.path.join(self.output_folder, file_name)
                    try:
                        response = requests.get(full_url, headers={"User-Agent": random.choice(self.headers)})
                        if response.status_code == 200:
                            with open(asset_path, "wb") as file:
                                file.write(response.content)
                            element[attr] = file_name
                    except Exception as e:
                        print(f"Failed to download asset {full_url}: {e}")

        with open(os.path.join(self.output_folder, "index.html"), "w", encoding="utf-8") as file:
            file.write(soup.prettify())

    def download_site(self):
        try:
            response = requests.get(self.url, headers={"User-Agent": random.choice(self.headers)})
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            self.download_page(self.url, os.path.join(self.output_folder, "index.html"))
            self.download_assets(soup)
        except Exception as e:
            print(f"Error during site download: {e}")
