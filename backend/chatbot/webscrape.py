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

import os
import gzip
import requests
from bs4 import BeautifulSoup
from xml.etree import ElementTree as ET

# Load and parse the sitemap file
sitemap_path = "C:\\Users\\Ananya\\ant-i-nfestation\\data\\sitemaps\\map.1.xml.gz"

with gzip.open(sitemap_path, 'rt', encoding='utf-8') as f:
    print("Made it here")
    tree = ET.parse(f)
    root = tree.getroot()

# Extract URLs from the sitemap
namespaces = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
urls = [elem.text for elem in root.findall('.//ns:loc', namespaces)]

def fetch_page(url):
    print("Also got here")
    response = requests.get(url)
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
        print("I think something bad hapened")
    return None

# Scrape each URL and store results
scraped_data = []
for url in urls:
    if fetch_page(url):
        print(fetch_page(url))
        scraped_data.append(fetch_page(url))

# scraped_data = [fetch_page(url) for url in urls if fetch_page(url)]

# # Print results
# for data in scraped_data:
#     print(data)