#!/usr/bin/env python3

# import prepositions
# Note that these are English prepositions. Some English prepositions are
# nouns or particles in Japanese, among other things.

from conf.conf import (CHAPTER,
                       DICTIONARY_DIR,
                       DEFAULT_PREPOSITION_TYPE)
from lib.jsontools import load_from_json, save_to_json
from lib.basics import get_basics, confirm

WE_ARE = 'prepositions'
FILE = "{}/{}.json".format(DICTIONARY_DIR, WE_ARE)


def start():
    cur_chapter = CHAPTER
    cur_preposition_type = DEFAULT_PREPOSITION_TYPE
    db = load_from_json(FILE, WE_ARE)
    print("Currently at {} words".format(len(db)))
    while True:
        english, kana, kanji, chapter, cur_chapter = get_basics(cur_chapter)
        if not english:
            break
        entry = {'english': english, 'kana': kana, 'chapter': chapter}
        if kanji:
            entry['kanji'] = kanji

        # Specific to prepositions
        cur_preposition_type = set_preposition_type(
            entry, cur_preposition_type
        )

        if confirm(entry):
            db.append(entry)
    save_to_json(FILE, {WE_ARE: db})


def set_preposition_type(entry, cur_preposition_type):
    preposition_types = ['time', 'place', 'movement', 'manner', 'agent',
                         'measure', 'source', 'possession']
    menu = ''
    i = 1
    for ppt in preposition_types:
        menu += "\n({}). {}".format(i, ppt)
        i += 1

    answer = input("What is the preposition type? {} [{}]: ".format(
        menu, cur_preposition_type
    ))
    answer = answer.strip()
    if answer == '':
        answer = preposition_types.index(cur_preposition_type) + 1
    answer = int(answer) - 1
    entry['type'] = preposition_types[answer]
    return preposition_types[answer]


if __name__ == "__main__":
    start()
