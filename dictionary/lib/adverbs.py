#!/usr/bin/env python3


def get_positivity(current):
    types = ['negative', 'positive']
    return select_choices('verb ending', types, current)


def select_choices(word, choices, current):
    prompt = ''
    i = 0
    while i < len(choices):
        prompt += "{} for {} {}, ".format(i, choices[i], word)
        i += 1
    prompt = prompt[:-2] + " [{}]: ".format(current)
    while True:
        response = input(prompt)
        if response == '':
            return current
        elif int(response) < len(choices):
            return int(response)
