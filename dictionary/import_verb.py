#!/usr/bin/env python3

from conf.conf import (CHAPTER, DICTIONARY_DIR, DEFAULT_VERB_TYPE,
                       DEFAULT_PARTICLE)
from lib.jsontools import load_from_json, save_to_json
from lib.basics import get_basics, confirm
from lib.verbs import get_type, get_particle

WE_ARE = 'verbs'
FILE = "{}/{}.json".format(DICTIONARY_DIR, WE_ARE)


def start():
    cur_chapter = CHAPTER
    vtype = DEFAULT_VERB_TYPE
    particle = DEFAULT_PARTICLE
    db = load_from_json(FILE, WE_ARE)
    print("Currently at {} words".format(len(db)))
    while True:
        english, kana, kanji, chapter, cur_chapter = get_basics(cur_chapter)
        if not english:
            break
        vtype = get_type(vtype)
        particle = get_particle(particle)
        entry = {'english': english, 'kana': kana, 'chapter': chapter}
        if kanji:
            entry['kanji'] = kanji

        # Specific to verbs
        if particle != 'intrans':  # Intransitive means there is no particle
            entry['particle'] = particle
        entry['type'] = vtype
        # End specific to verbs

        if confirm(entry):
            db.append(entry)
    save_to_json(FILE, {WE_ARE: db})


if __name__ == "__main__":
    start()
