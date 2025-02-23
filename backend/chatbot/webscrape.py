# import scrapy
# from scrapy.spiders import SitemapSpider

# class MySitemapSpider(SitemapSpider):
#     name = "sitemap_spider"
#     sitemap_urls = ["file:\\\C:\\Users\\Ananya\\ant-i-nfestation\\data\\sitemaps\\map.1.xml.gz"]  # Local path to your sitemap file 

#     def parse(self, response):
#         page_title = response.xpath('//title/text()').get()
#         body_text = response.xpath('//body//text()').getall()
        
#         yield {
#             'url': response.url,
#             'title': page_title,
#             'content': " ".join(body_text).strip()
#         }

# To run this spider, save the script as sitemap_spider.py, then execute:
# scrapy runspider sitemap_spider.py -o output.json

# import os
# import gzip
# import requests
# from bs4 import BeautifulSoup
# from xml.etree import ElementTree as ET
# from requests.auth import HTTPBasicAuth 

# # Load and parse the sitemap file
# sitemap_path = "/Users/iam_aj/ant-i-nfestation/data/sitemaps/map.1.xml.gz"

# with gzip.open(sitemap_path, 'rt', encoding='utf-8') as f:
#     print("Made it here")
#     tree = ET.parse(f)
#     root = tree.getroot()

# # Extract URLs from the sitemap
# namespaces = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
# urls = [elem.text for elem in root.findall('.//ns:loc', namespaces)]
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
# }

# def fetch_page(url):
#     print("Also got here")
#     response = requests.get(url)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')
#         title = soup.title.string if soup.title else "No Title"
#         body_text = ' '.join([p.get_text() for p in soup.find_all('p')])
        
#         return {
#             'url': url,
#             'title': title,
#             'content': body_text.strip()
#         }
#     else:
#         print(f"I think something bad hapened: {response.status_code}")
#     return None

# # Scrape each URL and store results
# scraped_data = []
# for url in urls:
#     if fetch_page(url):
#         print(fetch_page(url))
#         scraped_data.append(fetch_page(url))

# # scraped_data = [fetch_page(url) for url in urls if fetch_page(url)]

# # # Print results
# # for data in scraped_data:
# #     print(data)

import os
import gzip
import requests
from bs4 import BeautifulSoup
from xml.etree import ElementTree as ET
import cloudscraper
import ssl
import certifi

# Initialize CloudScraper (acts like requests)
scraper = cloudscraper.create_scraper()



# Use certifi's CA bundle
scraper.verify = certifi.where()


LOGIN_URL = "https://garden.org/login.php"

# Define login payload
login_payload = {
    "login_field_u": "infestationant@gmail.com",
    "login_field_p": "aipraccers2025"
}

# Perform login
login_response = scraper.post(LOGIN_URL, data=login_payload)

# Check if login was successful
if "logout" in login_response.text.lower():
    print("Login successful!")
else:
    print(f"Login failed! Status Code: {login_response.status_code}")

# Now use `scraper.get(url)` to fetch pages


# # Define login credentials
# LOGIN_URL = "https://garden.org/login.php"  # Update this with the actual login URL
# USERNAME = "infestationant@gmail.com"
# PASSWORD = "aipraccers2025"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Referer": "https://garden.org/",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1",
    "Connection": "keep-alive"
}



# Start a session
session = requests.Session()

# # Login payload (update field names based on the site's login form)
# login_payload = {
#     "login_field_u": USERNAME,  # Change to match form field names
#     "login_field_p": PASSWORD,
# }

# Perform login
# login_response = session.post(LOGIN_URL, data=login_payload, headers=headers)

# # Check if login was successful
# if login_response.status_code != 200:
#     print(f"Login failed: {login_response.status_code}: {login_response.text}")
#     exit()

# print("Login successful!")

# Load and parse the sitemap file
sitemap_path = "/Users/iam_aj/ant-i-nfestation/data/sitemaps/map.1.xml.gz"

with gzip.open(sitemap_path, 'rt', encoding='utf-8') as f:
    print("Made it here")
    tree = ET.parse(f)
    root = tree.getroot()

# Extract URLs from the sitemap
namespaces = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
urls = [elem.text for elem in root.findall('.//ns:loc', namespaces)]

def fetch_page(url):
    print(f"Fetching {url}")
    
    # Use the session to maintain authentication
    response = scraper.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "No Title"
        body_text = ' '.join([p.get_text() for p in soup.find_all('p')])
        
        return {
            'url': url,
            'title': title,
            'content': body_text.strip()
        }
    else:
        print(f"Failed to fetch {url}, Status Code: {response.status_code}")
        return None

# Scrape each URL and store results
scraped_data = []
i = 100
for url in urls:
    page_data = fetch_page(url)
    if page_data:
        scraped_data.append(page_data)
    i -= 1
    if i < 0:
        break

# Print the scraped data
for data in scraped_data:
    print(data)





