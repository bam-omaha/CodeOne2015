#!/usr/bin/env python

import jinja2
from server import model

with open("base.fcfg.jinja") as f:
    base_fcfg = "\n".join(f.readlines())

template = jinja2.Template(base_fcfg)

categories = model.Category.query.all()
category_names = []
for cat in categories:
    name = cat.title
    category_names.append(name.lower())

    if '/' in name:
        for x in name.split('/'):
            category_names.append(x.lower())

    if ' ' in name:
        for x in name.split(' '):
            category_names.append(x.lower())

category_names.remove("")
category_names.remove("and")

knowledges = model.Knowledge.query.all()

with open("grammar.fcfg", "w+") as f:
    f.write(template.render(categories=category_names, knowledges=knowledges))
