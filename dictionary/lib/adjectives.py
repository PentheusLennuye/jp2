#!/usr/bin/env python3


def get_type(current):
    types = ['', 'い', 'な']
    return select_choices('adjective', types, current)


def select_choices(word, choices, current):
    if word:
        word = '-' + word
    else:
        word = ''
    prompt = ''
    i = 1
    while i < len(choices):
        prompt += "{} for {}{}, ".format(i, choices[i], word)
        i += 1
    prompt = prompt[:-2] + " [{}]: ".format(choices.index(current))
    while True:
        response = input(prompt)
        if response == '':
            return current
        elif int(response) > 0 and int(response) < len(choices):
            return choices[int(response)]


def get_particle(current):
    particles = ['', 'が', None]
    return select_choices(None, particles, current)
