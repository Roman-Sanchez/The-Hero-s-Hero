import json

def load(jsonfile):
    my_data = json.loads(open(jsonfile).read())


