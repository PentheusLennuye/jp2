#!/usr/bin/env python3.9

# Combines all the pronouns, prepositions, nouns, verbs, adverbs
# etc into one big dictionary, keyed to english.

from ..lib.basics import load_from_json, save_to_json
DICTIONARY_DIR = 'sources'


dictionary = {}

# pos = "Part of speech"

for pos in ['noun', 'adverb', 'verb', 'adjective', 'demonstrative', 'pronoun']:
    pos_plural = pos + 's'
    source = load_from_json(
        "{}/{}.json".format(DICTIONARY_DIR, pos_plural), pos_plural
    )
    for phrase in source:
        key = phrase['english']
        phrase['pos'] = pos
        if key not in dictionary:
            dictionary[key] = phrase

save_to_json('./dictionary.json', {"dictionary": dictionary})
