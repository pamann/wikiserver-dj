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
    curator = node_d["curator"]
    _emoji = emoji.objects.get(title=emoji_uni)
    channel = node_d["channel"]
    title = node_d["title"]
    _node = node(song_id=song_id, title=title, _emoji=_emoji, channel=channel, curator=curator)
    _node.save()


# ------ add nav_options to existing nodes ------

for song_id in data:
    _node = node.objects.get(song_id=song_id)
    node_data = data[song_id]

    _node.N = node.objects.get(song_id=node_data["N"][0])
    _node.N_em = node_data["N"][1]
    _node.E = node.objects.get(song_id=node_data["E"][0])
    _node.E_em = node_data["E"][1]
    _node.S = node.objects.get(song_id=node_data["S"][0])
    _node.S_em = node_data["S"][1]
    _node.W = node.objects.get(song_id=node_data["W"][0])
    _node.W_em = node_data["W"][1]
    
    _node.save()
