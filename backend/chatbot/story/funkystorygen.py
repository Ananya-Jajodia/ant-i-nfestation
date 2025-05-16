from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)

CORS(app)

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

@app.route('/api/funky-story', methods=['POST'])
def api_generate_story():
    data = request.json
    plant_type = data.get('plant_type')
    plant_name = data.get('plant_name')
    plant_details = data.get('plant_details')
    story_length = data.get('story_length')
    story = generate_story(plant_type, plant_name, plant_details, story_length)
    return jsonify({'story': story})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
