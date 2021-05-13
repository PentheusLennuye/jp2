#!/usr/bin/env python3

from conf.conf import CHAPTER, DICTIONARY_DIR
from lib.jsontools import load_from_json, save_to_json
from lib.basics import get_basics, confirm

WE_ARE = 'pronouns'
FILE = "{}/{}.json".format(DICTIONARY_DIR, WE_ARE)


def start():
    cur_chapter = CHAPTER
    db = load_from_json(FILE, WE_ARE)
    print("Currently at {} words".format(len(db)))
    while True:
        english, kana, kanji, chapter, cur_chapter = get_basics(cur_chapter)
        if not english:
            break
        entry = {'english': english, 'kana': kana, 'chapter': chapter}
        if kanji:
            entry['kanji'] = kanji

        if confirm(entry):
            db.append(entry)
    save_to_json(FILE, {WE_ARE: db})


if __name__ == "__main__":
    start()
