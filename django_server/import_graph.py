"""
Terminal Commands:
python manage.py shell
exec(open('import_graph.py').read())
"""

import json
import os
from emusii.models import emoji, emusii, graph


with open('./grid.json') as f:
    data = json.load(f)

    print(data)


    
    # investor, inv_create = Investor.objects.get_or_create(name=investor_name)
    # for c in tqdm(data, desc="Loading companies into database for {}".format(investor_name)):
    #     if not c or not c["name"] or not slugify(c["name"]):
    #         continue
    #     slug = slugify(c["name"])

    #     company, created = Company.objects.get_or_create(slug=slug)

    #     # if not created: # if updating an existing value
    #     for field in Company._meta.get_fields():
    #         if field.name == "tag":
    #             continue
    #         if field.name == "investors":
    #             company.investors.add(Investor.objects.get(name=investor_name))
    #         try:
    #             if (not getattr(company, field.name)) and (c[field.name] is not None):
    #                 setattr(company, field.name, c[field.name])
    #         except KeyError:
    #             pass
    #     try:
    #         if c['relevant'] == False:
    #             company.relevant = False
    #             company.save()
    #     except KeyError:
    #         pass
    #     try:
    #         if c['dead'] == True:
    #             company.dead = True
    #             company.relevant = False
    #             company.save()
    #     except KeyError:
    #         pass
    #     try:
    #         if len(c['description']) > len(company.description):
    #             company.description = c['description']
    #             company.save()
    #     except KeyError:
    #         pass
    #     try:
    #         if c['team_size'] is not None and c['team_size'] > 500:
    #             company.relevant = False
    #             company.save()
    #     except KeyError:
    #         pass

    #     company.investors.add(investor)
    #     company.save()
