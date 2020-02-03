import sys
import json

file = sys.argv[1]

with open(file, "r") as notebook:
    nb = json.loads(notebook.read())

for cell in nb['cells']:
    try:
        if cell['source'][0]=='#':
            cell['metadata'] = {'slideshow': {'slide_type': 'slide'}}
        else:
            cell['metadata'] = {'slideshow': {'slide_type': 'subslide'}}
    except IndexError:
        cell['metadata'] = {'slideshow': {'slide_type': 'subslide'}}


with open(sys.argv[2], "w+") as out_nb:
    json.dump(nb, out_nb)
