import requests
import json
from pprint import pprint

API_KEY = "2b10LOUzU08HpKvhRpcXSiuRDu"	# Your API_KEY here
PROJECT = "all"; # try specific floras: "weurope", "canada"…
api_endpoint = f"https://my-api.plantnet.org/v2/identify/{PROJECT}?api-key={API_KEY}"

image_path_1 = "/Users/MikaFinkman/cs4701/ant-i-nfestation/data/images/daylily.png"
image_data_1 = open(image_path_1, 'rb')

image_path_2 = "/Users/MikaFinkman/cs4701/ant-i-nfestation/data/images/image_2.jpeg"
image_data_2 = open(image_path_2, 'rb')

data = { 'organs': ['flower'] }

files = [
  ('images', (image_path_1, image_data_1)),
#   ('images', (image_path_2, image_data_2))
]

req = requests.Request('POST', url=api_endpoint, files=files, data=data)
prepared = req.prepare()

s = requests.Session()
response = s.send(prepared)
json_result = json.loads(response.text)

pprint(response.status_code)
pprint(json_result['results'][0]['species']['commonNames'][0])