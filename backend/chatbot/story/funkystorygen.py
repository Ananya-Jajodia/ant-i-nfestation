import requests

def generate_story(plant_type, plant_name, plant_details, story_length):
    prompt = f"""
    Write a fun, whimsical, and funky story about a {plant_type} plant named {plant_name}. 
    The plant should have a quirky personality and go on a silly adventure. 
    The story should also incorporate the following details: {plant_details}.
    Make it a {story_length} word story.
    """

    response = requests.post(
        'http://localhost:11434/api/generate',
        json={
            'model': 'llama3',
            'prompt': prompt,
            'stream': False
        }
    )
    return response.json()['response']


name = input("What is your plant's name?")
type = input("What type of plant is "+name+"? ")
otherdeets = input("What other details about "+name+" do you want included in the story? ")
length = input("How long do you want the story to be (number of words)? ")
print(generate_story(plant_type=type, plant_name=name, plant_details=otherdeets, story_length=length))