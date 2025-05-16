import sys
from plant_identifier import identify_plant
import requests

if __name__ == "__main__":
    image_path = sys.argv[1]
    with open(image_path, "rb") as f:
        image_bytes = f.read()
    print(identify_plant(image_bytes))
