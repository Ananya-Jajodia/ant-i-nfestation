import requests
import credentials
from io import BytesIO

def identify_plant(image_bytes):
    """
    Identify the plant from image bytes using Pl@ntNet API without specifying organ data.

    Args:
        image_bytes (bytes): Raw image file contents.

    Returns:
        str: Common name of the most likely plant species.
    """
    PROJECT = "all"
    api_endpoint = f"https://my-api.plantnet.org/v2/identify/{PROJECT}?api-key={credentials.API_KEY}"

    files = [
        ('images', ('upload.jpg', BytesIO(image_bytes), 'image/jpeg')),
    ]

    response = requests.post(api_endpoint, files=files)  # no data argument!

    if response.status_code != 200:
        raise Exception(f"Pl@ntNet API error: {response.status_code} - {response.text}")

    result = response.json()

    try:
        common_name = result['results'][0]['species']['commonNames'][0]
    except (KeyError, IndexError):
        common_name = f"{response.status_code}: {response}"

    return common_name


# import requests
# import json
# from pprint import pprint
# import credentials


# PROJECT = "all"; # try specific floras: "weurope", "canada"…
# api_endpoint = f"https://my-api.plantnet.org/v2/identify/{PROJECT}?api-key={credentials.API_KEY}"

# image_path_1 = "/Users/MikaFinkman/cs4701/ant-i-nfestation/data/images/daylily.png"
# image_data_1 = open(image_path_1, 'rb')

# # image_path_2 = "/Users/MikaFinkman/cs4701/ant-i-nfestation/data/images/image_2.jpeg"
# # image_data_2 = open(image_path_2, 'rb')

# data = { 'organs': ['flower'] }

# files = [
#   ('images', (image_path_1, image_data_1)),
# #   ('images', (image_path_2, image_data_2))
# ]

# req = requests.Request('POST', url=api_endpoint, files=files)
# prepared = req.prepare()

# s = requests.Session()
# response = s.send(prepared)
# json_result = json.loads(response.text)

# pprint(response.status_code)
# pprint(json_result['results'][0]['species']['commonNames'][0])