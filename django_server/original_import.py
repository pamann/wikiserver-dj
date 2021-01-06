"""
Terminal Commands:
python manage.py shell
exec(open('loaddatabase_companies.py').read())
"""

import json
import os
from django.utils.text import slugify
from data.models import Company, Investor, Tag

BASE_PATH = ".\\outfiles\\company_jsons" # windows
BASE_PATH = "./outfiles/company_jsons" # linux


for file in os.listdir(BASE_PATH):
    investor_name = os.path.splitext(file)[0]
    # ~~~ Model.objects.get_or_create() does what it sounds like. investor is the model object while inv_create is a boolean if it was created or not ~~~
    investor, inv_create = Investor.objects.get_or_create(name=investor_name)

    with open(os.path.join(BASE_PATH, file)) as f:
        data = json.load(f)
        for c in data:
            slug = slugify(c["name"])

            # ~~~ I used slugs as ids, but use whatever the primary key is for get_or_create() ~~~
            company, created = Company.objects.get_or_create(slug=slug)

            for field in Company._meta.get_fields():
                if field.name == "tag":
                    continue
                if field.name == "investors":
                    # ~~~ Add foreign key fields like this, or if you have the object itself handy, then just use company.investors.add(investor) ~~~
                    company.investors.add(Investor.objects.get(name=investor_name))
                try:
                    # ~~~ getattr() and setattr() were easy ways to not rewrite c['field1'], c['field2'], etc. ~~~
                    if (not getattr(company, field.name)) and (c[field.name] is not None):
                        setattr(company, field.name, c[field.name])
                except KeyError:
                    pass

            company.save()
