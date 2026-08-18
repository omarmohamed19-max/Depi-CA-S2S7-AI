import json
import random
from pathlib import Path


DataPath= Path(__file__).parent / "data.json"

def load_responses():
    with open(DataPath,"r",encoding="utf-8") as file:
        return json.load(file)

def get_responses(user_input):
    responses=load_responses()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])