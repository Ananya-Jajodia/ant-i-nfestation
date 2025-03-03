import os
import gzip
import requests
import pandas as pd
from bs4 import BeautifulSoup
from xml.etree import ElementTree as ET
import cloudscraper
import csv


def save_to_csv(data, filename):
    if not data:
        print("No data to save.")
        return
    
    keys = data[0].keys()  # Get column names from the first dictionary
    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

# Initialize CloudScraper to bypass Cloudflare protections
scraper = cloudscraper.create_scraper()

# Headers to mimic a real browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Referer": "https://garden.org/",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1",
    "Connection": "keep-alive"
}

# Load and parse the sitemap file
sitemap_path = "/Users/Ananya/ant-i-nfestation/data/sitemaps/map.1.xml.gz"

with gzip.open(sitemap_path, 'rt', encoding='utf-8') as f:
    print("Sitemap loaded successfully.")
    tree = ET.parse(f)
    root = tree.getroot()

# Extract URLs from the sitemap
namespaces = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
urls = [elem.text for elem in root.findall('.//ns:loc', namespaces)]

# def extract_plant_name(url):
#     """Extracts plant name from the URL path."""
#     parts = url.split('/')
#     if "grow" in parts:  
#         index = parts.index("grow") + 1
#         if index < len(parts):
#             return parts[index].replace("-", " ").title()  # Format plant name
#     return "Unknown"

def fetch_page(url):
    """Fetches and extracts content from the page."""
    print(f"Fetching {url}")
    
    # Request the page
    response = scraper.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string.strip() if soup.title else "No Title"
        body_text = ' '.join([p.get_text() for p in soup.find_all('p') if p.get_text()])

        if not body_text:
            print(f"Warning: No text content found on {url}")

        return {
            # 'Plant Name': extract_plant_name(url),
            'URL': url,
            'Title': title,
            'Content': body_text.strip()
        }
    else:
        print(f"Failed to fetch {url}, Status Code: {response.status_code}")
        return None

# Scrape each URL and store results
scraped_data = []
limit = 100  # Prevent excessive requests

for url in urls[:limit]:
    page_data = fetch_page(url)
    if page_data:
        scraped_data.append(page_data)

# Convert scraped data to DataFrame and save as CSV
# df = pd.DataFrame(scraped_data)
csv_filename = "scraped_plants_data.csv"
save_to_csv(scraped_data, csv_filename)

print(f"Scraped data saved to {csv_filename}")







