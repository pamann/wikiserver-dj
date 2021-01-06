import json
from emusii.models import emoji, node
from extract import json_extract 

with open("./grid.json") as f:
    data = json.load(f)

# ------ add all emojis into DB ------

emojis = json_extract(data, 'emoji')
for _emoji in emojis:
    em, created = emoji.objects.get_or_create(title=_emoji)
    em.save()

# ------ add all nodes w/o nav_options into DB ------

for node_id in data:
    song_id = node_id
    node_d = data[node_id]
    emoji_uni = node_d["emoji"]
    _emoji = emoji.objects.get(title=emoji_uni)
    channel = node_d["channel"]
    title = node_d["title"]

    _node = node(song_id=song_id, title=title, _emoji=_emoji, channel=channel)
    _node.save()

# ------ add nav_options to existing nodes ------

for song_id in data:
    _node = node.objects.get(song_id=song_id)
    node_data = data[song_id]
    for nav in node_data["neighbors"]:
        _nav_node = node.objects.get(song_id=nav)
        _node.nav_options.add(_nav_node)
    _node.save()
