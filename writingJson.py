import json

def writingJsonFile(data):
    with open("corona-data.json", "a") as f:
        f.write(data)