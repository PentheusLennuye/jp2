#!/usr/bin/env python3.9

import sys

from PySide6.QtWidgets import QApplication

from lib.card import Card


app = QApplication(sys.argv)
title = 'Chapter Four, Exercise 2b'
instructions = 'Translate into Japanese.'
questions = ['The library is behind the university.',
             'The hospital is in front of the department store.']
answers = [
    [['図書館', 'としょかん'], ['は', ''], ['大学', 'だいがく'],
     ['の', ''], ['後ろ', 'うし'], ['です', '']],
    [['病院', 'びょういん'], ['は', ''], ['デパート', ''],
     ['の', ''], ['前', 'まえ'], ['です', '']]
]
card = Card(title, instructions, questions, answers)
card.show()
sys.exit(app.exec())

