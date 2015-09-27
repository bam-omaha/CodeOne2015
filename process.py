import nltk

def parse(question):
    cp = nltk.load_parser('grammar.fcfg',cache=False)
    parsed = list(cp.parse(question.lower().split()))

    if len(parsed) < 1:
        return None

    tree = list(parsed)[0]
    return "".join(tree.label()['SEM']), "".join(tree.label()['QT'])

