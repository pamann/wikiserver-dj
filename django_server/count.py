import json
from extract import json_extract 

with open("./grid.json") as f:
    data = json.load(f)

# emojis = json_extract(data, '')
print(len(data))
