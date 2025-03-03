import urllib.robotparser
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

def item_not_in_file(item, file_path):
    """Checks if a given item is NOT present in the text file."""
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if item in line:
                return False  # Item is found, so it's NOT missing
    return True  # Item is NOT found in the file

full_url = "https://garden.org/learn/howto/grow/yarrows/"
headers = {"User-Agent": "Mozilla/5.0"}

# Example usage
file_path = "/Users/iam_aj/ant-i-nfestation/data/robots.txt"  # Replace with your actual file path
item_to_check = full_url

if item_not_in_file(item_to_check, file_path):
    print(f'"{item_to_check}" is NOT in the file.')
    response = requests.get(full_url, headers=headers)
    if response.status_code == 200:
      soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())
      print(f"scraped {full_url}")
    else:
      print(f"Failed, status code: {response.status_code}")
else:
    print(f'"{item_to_check}" is in the file.')
    print(f"scraping not allowed: {full_url}")


# def scrape(base_url, full_url, user_agent = "*"):
#   rp = urllib.robotparser.RobotFileParser()
#   robots_url = rp.set_url(base_url + "/robots.txt")
#   # rp.read()
#   try:
#         response = requests.get(robots_url, headers={"User-Agent": user_agent}, timeout=5)  # Fetch manually to check response
#         print(f"robots.txt response: {response.status_code}")
#         print(response.text)  # Print robots.txt content for verification
#         rp.set_url(robots_url)
#         rp.read()
#   except Exception as e:
#         print(f"Error fetching robots.txt: {e}")
#         return False  # Default to False if fetching fails
#   return rp.can_fetch(user_agent, full_url)
# base_url = "https://garden.org"
# full_url = "https://garden.org/learn/howto/grow/yarrows/"

# print(scrape(base_url=base_url, full_url=full_url, user_agent="*"))

# url = "https://webscraper.io"



# if :
#   print("proceed!")
#   response = requests.get(url, headers=headers)
#   if response.status_code == 200:
#     soup = BeautifulSoup(response.text, "html.parser")
#     # print(soup.prettify())
#     print(f"scraped {url}")
#   else:
#     print(f"Failed, status code: {response.status_code}")
# else:
  