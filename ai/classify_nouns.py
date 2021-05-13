#!/usr/bin/env python3

from conf import DICTIONARY_DIR, AI_DIR
from lib.basics import load_from_json, save_to_json

import math


class TerminalNotAListError(Exception):
    pass


class DuplicateCategoryError(Exception):
    pass


def start():
    relations = load_from_json("{}/relations.json".format(AI_DIR),
                               "relation")
    nouns = load_from_json("{}/nouns.json".format(DICTIONARY_DIR),
                           "nouns")
    donefile = "{}/relations.index".format(AI_DIR)
    completed = open(donefile).read().splitlines()
    categories = {}
    get_terminal_names(None, '', relations, categories)
    category_names = list(categories.keys())
    category_names.sort()
    place_nouns(nouns, categories, category_names, completed)
    save_to_json("{}/relations.json".format(AI_DIR),
                 {"relation": relations})
    with open(donefile, 'w') as fp:
        for noun in completed:
            fp.write(noun + "\n")


def get_terminal_names(parent, parent_name, node, terminals):
    if isinstance(node, dict):
        children = list(node.keys())
        for child in children:
            get_terminal_names(node, child, node[child], terminals)
    elif isinstance(node, list):
        if parent_name in terminals:
            raise DuplicateCategoryError
        terminals[parent_name] = node
    else:
        print("Error!" + node)
        raise TerminalNotAListError


def place_nouns(nouns, categories, category_names, completed):
    menu(category_names, 4)
    noun_count = 0
    for noun in nouns:
        if noun['english'] in completed:
            continue
        noun_count += 1
        if noun_count > 10:
            menu(category_names, 4)
            noun_count = 0
        english = noun['english']
        article = get_article(english)
        to_be = get_to_be(english)
        print("What {}{}{}? (STOP to stop): ".format(to_be, article,
                                                     english))
        answer = ''
        while answer == '':
            answer = input("> ").strip()
        if answer == 'STOP':
            break
        answer = category_names[int(answer) - 1]  # Fencepost
        print("Aha! It belongs to '{}'.".format(answer))
        categories[answer].append(noun['english'])
        completed.append(noun['english'])


def menu(category_names, num_cols):
    num_cn = len(category_names)
    num_rows = math.ceil(num_cn / num_cols)
    row = 0
    while row < num_rows:
        line = ''
        col = 0
        while col < num_cols:
            i = row + (num_rows * col)
            if i < num_cn:
                line += "{:2}. {:22}".format(i + 1, category_names[i])
            col += 1
        print(line)
        row += 1


def get_to_be(word):
    if word == "I":
        return "am "
    if not is_plural(word):
        return "is "
    else:
        return "are "


def is_plural(word):
    if word[-1] != 's':
        return False
    elif word[-2] == 's':
        return False
    else:
        return True


def get_article(word):
    if is_plural(word):
        return ''
    if word in ['honour', 'honourable', 'herb']:
        return 'an '
    first_letter = word[0].lower()
    if first_letter in ('a', 'e', 'i', 'o', 'u'):
        return 'an '
    else:
        return 'a '


if __name__ == "__main__":
    start()
