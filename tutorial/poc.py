#!/usr/bin/env python3.9

import sys
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QLabel,
                               QVBoxLayout, QHBoxLayout, QWidget)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, Slot, QCoreApplication


default_font = QFont()
default_font.setPointSize(18)
gloss_font = QFont()
gloss_font.setPointSize(10)

h1fontsize = 18
pfontsize = 14

JP = 2
EN = 0


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
        layout.setContentsMargins(1, 1, 1, 1)
        self.setLayout(layout)


class PlayfieldSection(QWidget):
    def __init__(self, text, parent):
        super().__init__(parent)

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
        self.qwidget = PlayfieldSection(question, self)
        self.awidget = PlayfieldSection(answer, self)

        playfield_layout = QVBoxLayout()
        playfield_layout.setAlignment(Qt.AlignCenter)
        playfield_layout.addWidget(self.qwidget)
        playfield_layout.addWidget(self.awidget)
        self.setLayout(playfield_layout)

    def hide_answer(self):
        self.awidget.hide()

    def show_answer(self):
        self.awidget.show()


class Controls(QWidget):
    def __init__(self, parent, init_label, mainfunction, quitfunction):
        super().__init__(parent)
        self.button = QPushButton(init_label)
        self.button.clicked.connect(mainfunction)
        self.button.setAutoDefault(True)
        quitbutton = QPushButton('終わる')
        quitbutton.setStyleSheet('background-color: #c00; color: white;')
        quitbutton.clicked.connect(quitfunction)

        layout = QHBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(quitbutton)
        self.setLayout(layout)

    def set_button(self, label):
        self.button.setText(label)

    def hide_button(self):
        self.button.hide()


POSING_QUESTION = 0
SHOWING_ANSWER = 1


class Card(QDialog):
    def __init__(self, title, instructions,
                 questions, answers, parent=None):
        super().__init__(parent)
        self.index = 0
        self.mode = POSING_QUESTION
        self.button_labels = ['答え', '次の質問']
        self.last_question = len(questions) - 1
        self.setWindowTitle('日本語の練習')

        self.title = Title(title, self)
        self.instructions = Instructions(instructions, self)
        self.playfield = Playfield(
            questions[self.index], answers[self.index], self
        )
        self.playfield.hide_answer()
        self.controls = Controls(self, self.button_labels[self.mode],
                                 self.move_forward, self.quit_me)
        self.layout = QVBoxLayout()
        self.set_layout()

    def set_layout(self):

        self.layout.takeAt(0)
        self.layout.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.instructions)
        self.layout.addWidget(self.playfield)
        self.layout.addWidget(self.controls)
        self.setLayout(self.layout)

    @Slot()
    def move_forward(self):
        if self.mode == POSING_QUESTION:
            self.mode = SHOWING_ANSWER
            self.show_answer()
        else:
            self.mode = POSING_QUESTION
            self.pose_next_question()

    def pose_next_question(self):
        self.index += 1
        self.playfield.setParent(None)
        self.playfield = Playfield(
            questions[self.index], answers[self.index], self
        )
        self.playfield.hide_answer()
        self.controls.set_button(self.button_labels[self.mode])
        self.set_layout()

    def show_answer(self):
        self.playfield.show_answer()
        if self.index < self.last_question:
            self.controls.set_button(self.button_labels[self.mode])
        else:
            self.controls.hide_button()

    @Slot()
    def quit_me(self):
        QCoreApplication.instance().quit()


if __name__ == '__main__':
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
