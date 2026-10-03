from collections import OrderedDict

glossary = {
    'dictionary': 'List of key value items',
    'list': 'editable store of items',
    'tuple': 'uneditable list of things',
    'loops': 'a circular principal',
    'conditions': 'a type of fixed state'
}

glossary2 = OrderedDict(glossary)

for key, value in glossary2.items():
    print(key.title() + ": " + value + ".")