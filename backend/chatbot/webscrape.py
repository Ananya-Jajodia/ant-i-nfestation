import os
import gzip
import requests
from bs4 import BeautifulSoup
from xml.etree import ElementTree as ET
import cloudscraper
import csv


def save_to_csv(data, filename):
    if not data:
        print("No data to save.")
        return
    
    keys = data[0].keys()
    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

def item_not_in_file(item, file_path):
    """Checks if a given item is NOT present in the text file."""
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if item in line:
                return False
    return True

scraper = cloudscraper.create_scraper()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Referer": "https://garden.org/",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1",
    "Connection": "keep-alive"
}

sitemap_path = "/Users/iam_aj/ant-i-nfestation/data/sitemaps/map.1.xml.gz"

with gzip.open(sitemap_path, 'rt', encoding='utf-8') as f:
    print("Sitemap loaded successfully.")
    tree = ET.parse(f)
    root = tree.getroot()

namespaces = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
urls = [elem.text for elem in root.findall('.//ns:loc', namespaces)]

def fetch_page(url):
    """Fetches and extracts content from the page."""
    print(f"Fetching {url}")

    response = scraper.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string.strip() if soup.title else "No Title"
        body_text = ' '.join([p.get_text() for p in soup.find_all('p') if p.get_text()])

        if not body_text:
            print(f"Warning: No text content found on {url}")

        return {
            'URL': url,
            'Title': title,
            'Content': body_text.strip()
        }
    else:
        print(f"Failed to fetch {url}, Status Code: {response.status_code}")
        return None

scraped_data = []
limit = 100 

for url in urls[:limit]:
    if item_not_in_file(url, "/Users/iam_aj/ant-i-nfestation/data/robots.txt"):
        page_data = fetch_page(url)
        if page_data:
            scraped_data.append(page_data)
    else:
        print(f"{url} in robots, access not allowed!")

csv_filename = "scraped_plants_data.csv"
save_to_csv(scraped_data, csv_filename)

print(f"Scraped data saved to {csv_filename}")







