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

    response = requests.post(api_endpoint, files=files)

    if response.status_code != 200:
        raise Exception(f"Pl@ntNet API error: {response.status_code} - {response.text}")

    result = response.json()

    try:
        common_name = result['results'][0]['species']['commonNames'][0]
    except (KeyError, IndexError):
        common_name = f"{response.status_code}: {response}"

    return common_name