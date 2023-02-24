import json

def Load():

    f = open('setup.json')

    data = json.load(f)
    

    f.close()
    return data["basicSetup"]['tyres']["tyreCompound"]