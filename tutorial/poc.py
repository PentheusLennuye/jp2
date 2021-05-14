#!/usr/bin/env python3.9

import sys
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QLabel,
                               QVBoxLayout, QHBoxLayout, QWidget)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt


default_font = QFont()
default_font.setPointSize(18)
gloss_font = QFont()
gloss_font.setPointSize(10)

h1fontsize = 18
pfontsize = 14

JP = 2
EN = 0

title = 'Chapter Four, Exercise 2b'
instructions = 'Translate into Japanese.'
questions = ['The library is behind the university.', ]
answers = [
            [['図書館', 'としょかん'], ['は', ''], ['大学', 'だいがく'],
            ['の', ''], ['後ろ', 'うし'], ['です', '']],
]


class Title(QLabel):
    def __init__(self, text, parent):
        super().__init__(parent)
        font = QFont()
        font.setPointSize(h1fontsize)
        self.setFont(font)
        self.setText(text)
        self.setAlignment(Qt.AlignCenter)


class Instructions(QLabel):
    def __init__(self, text, parent):
        super().__init__(parent)
        font = QFont()
        font.setPointSize(pfontsize)
        self.setFont(font)
        self.setText(text)
        self.setAlignment(Qt.AlignCenter)
        self.setWordWrap(True)


class GlossBox(QWidget):
    '''Being a vertical box layout with two (2) labels, a maintext
       surmounted by a smaller font gloss (or furigana)'''
    def __init__(self, maintext, gloss, parent):
        super().__init__(parent)

        self.main_label = QLabel(maintext, self)
        self.main_label.setFont(default_font)

        self.gloss_label = QLabel(gloss, self)
        self.gloss_label.setFont(gloss_font)

        layout = QVBoxLayout()
        layout.addWidget(self.gloss_label)
        layout.addWidget(self.main_label)
        self.setLayout(layout)


class PlayfieldSection(QWidget):
    def __init__(self, text, parent):
        super().__init__(parent)

        self.setStyleSheet('background-color: white;')
        layout = QHBoxLayout()
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignCenter)

        if isinstance(text, str):
            widget = QLabel(text, self)
            widget.setFont(default_font)
            layout.addWidget(widget)

        if isinstance(text, list):
            for t in text:
                if isinstance(t, str):
                    widget = QLabel(t, self)
                elif isinstance(t, list):
                    widget = GlossBox(t[0], t[1], self)
                widget.setFont(default_font)
                layout.addWidget(widget)

        self.setLayout(layout)


class Playfield(QWidget):
    def __init__(self, question, answer, parent):
        super().__init__(parent)
        self.setStyleSheet('background-color: white;')
        qwidget = PlayfieldSection(question, self)
        awidget = PlayfieldSection(answer, self)

        playfield_layout = QVBoxLayout()
        playfield_layout.setAlignment(Qt.AlignCenter)
        playfield_layout.addWidget(qwidget)
        playfield_layout.addWidget(awidget)
        self.setLayout(playfield_layout)


class Card(QDialog):
    def __init__(self, title, instructions,
                 questions, answers, parent=None):
        super().__init__(parent)
        self.index = 0
        self.setWindowTitle('日本語の練習')

        title = Title(title, self)
        instructions = Instructions(instructions, self)
        self.playfield = Playfield(
            questions[self.index], answers[self.index], self
        )

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        layout.addWidget(instructions)
        layout.addWidget(self.playfield)
        # layout.addWidget(self.button)
        # layout.addWidget(self.quit)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    card = Card(title, instructions, questions, answers)
    card.show()
    sys.exit(app.exec())
