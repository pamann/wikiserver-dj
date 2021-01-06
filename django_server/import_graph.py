"""
Terminal Commands:
python manage.py shell
exec(open('import_graph.py').read())
"""

import json
import os
from emusii.models import emoji, node, activesubgraph, graph


with open('./grid.json') as f:
    data = json.load(f)

    for song in data:
        key = song
        emoji = data[song]['emoji']
        channel = data[song]['channel']
        title = data[song]['title']
        nav_options = [data[song][key] for key in ['N', 'S', 'E', 'W']]
