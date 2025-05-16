import urllib.robotparser
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

def item_not_in_file(item, file_path):
    """Checks if a given item is NOT present in the text file."""
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if item in line:
                return False 
    return True 

full_url = "https://garden.org/learn/howto/grow/yarrows/"
headers = {"User-Agent": "Mozilla/5.0"}


file_path = "/Users/iam_aj/ant-i-nfestation/data/robots.txt"  
item_to_check = full_url

if item_not_in_file(item_to_check, file_path):
    print(f'"{item_to_check}" is NOT in the file.')
    response = requests.get(full_url, headers=headers)
    if response.status_code == 200:
      soup = BeautifulSoup(response.text, "html.parser")
      print(f"scraped {full_url}")
    else:
      print(f"Failed, status code: {response.status_code}")
else:
    print(f'"{item_to_check}" is in the file.')
    print(f"scraping not allowed: {full_url}")