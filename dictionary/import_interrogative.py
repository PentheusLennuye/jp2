#!/usr/bin/env python3

import json
import shutil

WE_ARE = '../dictionary/interrogatives'
FILE = "{}.json".format(WE_ARE)


def start():
    try:
        with open(FILE) as fp:
            db = json.load(fp)
    except FileNotFoundError:
        db = {WE_ARE: []}
    while True:
        english = input("English word (or STOP to quit): ").strip()
        if english == '':
            continue
        if english == 'STOP':
            break
        kana = input("Kana: ").strip()
        kanji = input("Kanji: ").strip()
        if kanji == '':
            kanji = None
        confirm = build_confirm(english, kana, kanji)
        entry = build_entry(english, kana, kanji)
        response = None
        while response not in ('', 'y', 'Y', 'n', 'N'):
            response = input(confirm).strip()
        if response in ('', 'y', 'Y'):
            db[WE_ARE].append(entry)

    try:
        shutil.copy(FILE, '{}.bak'.format(FILE))
    except FileNotFoundError:
        pass
    with open(FILE, 'w', encoding='utf-8') as fp:
        json.dump(db, fp, ensure_ascii=False)


def build_confirm(english, kana, kanji):
    confirm = english + ": "
    if kanji:
        confirm += kanji + ' -- '
    confirm += kana
    confirm += "[Y/n] "
    return confirm


def build_entry(english, kana, kanji):
    entry = {'english': english,
             'kana': kana
             }
    if kanji:
        entry['kanji'] = kanji
    return entry


if __name__ == "__main__":
    start()
