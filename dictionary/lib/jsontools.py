#!/usr/bin/env python3

import json
import shutil


def load_from_json(path, word_type):
    try:
        with open(path) as fp:
            db = json.load(fp)[word_type]
    except FileNotFoundError:
        print("No dictionary found at {}. I will create a new one. "
              "CTRL-C to cancel")
        db = []
    return db


def save_to_json(path, db):
    try:
        shutil.copy(path, '{}.bak'.format(path))
    except FileNotFoundError:
        pass
    with open(path, 'w', encoding='utf-8') as fp:
        json.dump(db, fp, ensure_ascii=False)


def searchtree(searchitem, path, node, nodename):
    ''' Traverses a dictionary looking for a list item. Returns a reversed list
        of keys leading to the item '''
    if isinstance(node, dict):
        nodenames = list(node.keys())
        for nodename in nodenames:
            if searchtree(searchitem, path, node[nodename], nodename):
                path.append(nodename)
                return True
    elif isinstance(node, list):
        if searchitem in node:
            return True
        return False
    return False
