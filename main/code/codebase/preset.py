import os
import json

def load_preset():
    preset_dict = {}
    try:
        with open(f"{os.environ['HOME']}/.config/.clinic/.preset.json","r") as file_:
            return json.load(file_)
    except json.decoder.JSONDecodeError:
        with open(f"{os.environ['HOME']}/.config/.clinic/.preset.json","w+") as file_:
            preset_dict['operation'] = False
            preset = json.dumps(preset_dict, indent=4)
            file_.write(preset)
            return json.load(file_)


def set_preset():
    username = open(f"{os.environ['HOME']}/.config/.clinic/username.txt", 'r').readline()
    with open(f"{os.environ['HOME']}/.config/.clinic/.preset.json","w+") as file_:
        slot_topic = input('Topic for Clinic: ').capitalize()
        year = input("Year: ")
        operation = True
        preset_dict = {
            'topic' : slot_topic,
            'year' : 2020,
        }
        preset_dict['operation'] = True
        preset = json.dumps(preset_dict, indent=4)
        file_.write(preset)
# file_.close