import json

def writingJsonFile(data):
    with open("corona-data.json", "w") as f:
        f.write(data)
        f.write('\n')
        f.close()