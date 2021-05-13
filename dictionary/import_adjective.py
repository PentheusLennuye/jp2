#!/usr/bin/env python3

from conf.conf import (CHAPTER,
                       DICTIONARY_DIR,
                       DEFAULT_ADJECTIVE_TYPE,
                       DEFAULT_ADJECTIVE_PARTICLE)
from lib.basics import get_basics, confirm
from lib.jsontools import load_from_json, save_to_json
from lib.adjectives import get_type, get_particle

WE_ARE = 'adjectives'
FILE = "{}/{}.json".format(DICTIONARY_DIR, WE_ARE)


def start():
    cur_chapter = CHAPTER
    atype = DEFAULT_ADJECTIVE_TYPE
    particle = DEFAULT_ADJECTIVE_PARTICLE
    db = load_from_json(FILE, WE_ARE)
    print("Currently at {} words".format(len(db)))
    while True:
        english, kana, kanji, chapter, cur_chapter = get_basics(cur_chapter)
        if not english:
            break
        atype = get_type(atype)
        particle = get_particle(particle)
        entry = {'english': english, 'kana': kana, 'chapter': chapter}
        if kanji:
            entry['kanji'] = kanji

        # Specific to adjectives
        if particle is not None:
            entry['particle'] = particle
        entry['type'] = atype
        # End specific to verbs

        if confirm(entry):
            db.append(entry)
    save_to_json(FILE, {WE_ARE: db})


if __name__ == "__main__":
    start()
