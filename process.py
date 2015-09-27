
import nltk

def parse(text):
    cp = nltk.load_parser('thing.fcfg',cache=False)
    thing = cp.parse(text.lower().split())
    tree = list(thing)[0]
    tree.label()['SEM']
    return " ".join(tree.label()['SEM'])

