import json

def get_plants():
    with open("plants.json", "r") as f:
        plants = json.load(f)
    
    return plants

