import requests
import json

mode_req = requests.get("https://api.tfl.gov.uk/Line/Meta/Modes")
modeS = json.loads(mode_req.text)
#for valid modes
def valid_modes():
    list = []
    mode_req = requests.get("https://api.tfl.gov.uk/Line/Meta/Modes")
    modeS = json.loads(mode_req.text)
    for mode in modeS:
        list.append(mode["modeName"])
    return list

def pprint(list) :
    for item in list :
        print(item)


pprint(valid_modes())



