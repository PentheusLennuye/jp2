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

h1fontsize = 24
pfontsize = 16

JP = 2
EN = 0

title = 'Chapter Four, Exercise 2b'
instructions = 'Translate into Japanese.'
question = 'The library is behind the university.'
answer = [
            ['図書館', 'としょかん'], ['は', ''], ['大学', 'だいがく'],
            ['の', ''], ['後ろ', 'うし'], ['です', '']
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
        layout.addStretch(1)
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignLeft)

        if isinstance(text, str):
            widget = QLabel(text, self)
            self.setFont(default_font)
            layout.addWidget(widget)

        if isinstance(text, list):
            for t in text:
                if isinstance(t, str):
                    widget = QLabel(t, self)
                    layout.addWidget(widget)

        self.setLayout(layout)


class Card(QDialog):
    def __init__(self, title, instructions, parent=None):
        super().__init__(parent)
        self.setWindowTitle('日本語の練習')

        self.title = Title(title, self)
        self.instructions = Instructions(instructions, self)

        self.playfield = QWidget()
        self.playfield = QVBoxLayout()
        self.playfield.setAlignment(Qt.AlignCenter)


        self.question = PlayfieldSection(
            'It is the Japanese language.', self
        )
        self.answer = PlayfieldSection(
            ['日本語', 'です'],
            self
        )

        # self.answer = GlossBox('日本語', 'にほんご', self)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title)
        layout.addWidget(self.instructions)
        layout.addWidget(self.question)
        layout.addWidget(self.answer)
        # layout.addWidget(self.button)
        # layout.addWidget(self.quit)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    card = Card(title, instructions)
    card.show()
    sys.exit(app.exec())
