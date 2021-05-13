from .basics import get_kanji, get_furigana


def get_adverb(keyoushi):
    furigana = get_furigana(keyoushi)
    if not furigana:
        furigana = ''
    return [get_kanji(keyoushi), furigana]


def get_predicate(c, doushi, positive=True, polite=True):
    c.set_verb(doushi)
    furigana = get_furigana(doushi)
    if not furigana:
        furigana = ''
    return [c.conjugate(polite=polite, positive=positive), furigana]


def get_invitation(c, doushi):
    c.set_verb(doushi)
    furigana = get_furigana(doushi)
    if not furigana:
        furigana = ''
    conjugated_verb = c.conjugate(positive=False) + 'か'
    return [conjugated_verb, furigana]
