"""
HOW TO RUN THIS:
python3 manage.py shell
exec(open('import_graph.py').read())
"""

# COMMENT THIS UP
# write the SPC stuff

import json
import os
# from emusii.models import emoji, emusii, graph # this causes an issue...


with open('./grid.json') as f:
    data = json.load(f)

    for song in data:
        key = song
        emoji = data[song]['emoji']
        channel = data[song]['channel']
        title = data[song]['title']
        neighbors = [data[song][key] for key in ['N', 'S', 'E', 'W']]
        print(neighbors)
