import requests
import json

#for valid modes
def valid_Lmodes():
    list = [] # list of valid Line modes
    mode_req = requests.get("https://api.tfl.gov.uk/Line/Meta/Modes")
    modeS = json.loads(mode_req.text)
    for mode in modeS:
        list.append(mode["modeName"])
    return list

def valid_Jmodes():
    list = [] # valide journey planner modes
    mode_req = requests.get("https://api.tfl.gov.uk/Journey/Meta/Modes")
    modeS = json.loads(mode_req.text)
    for mode in modeS:
        list.append(mode["modeName"])
    return list

def pprint(list) :
    for item in list :
        print(item)





