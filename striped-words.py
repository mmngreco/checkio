
from string import maketrans, translate, punctuation

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
vow = VOWELS.lower()
cons = CONSONANTS.lower()


def checkio(text):
    text = text.encode('utf-8').lower()  # compatibility with translate

    transtab = maketrans(punctuation, ' ' * len(punctuation))
    transtab_vow = maketrans(vow, '1' * len(vow))
    transtab_cons = maketrans(cons, '0' * len(cons))

    text = text.translate(transtab).split()
    text = [s.strip() for s in text]

    text_bin = [s.translate(transtab_vow) for s in text]
    text_bin = [s.translate(transtab_cons) for s in text_bin]
    result = len(text)

    for i, word in enumerate(text_bin):
        if any(map(str.isdigit, text[i])):  # some character is digit
            result -= 1

        elif any(['11' in word, '00' in word, len(word) < 2]):
            result -= 1

    return result

# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    assert checkio(u"My name is ...") == 3, "All words are striped"
    assert checkio(u"Hello world") == 0, "No one"
    assert checkio(u"A quantity of striped words.") == 1, "Only of"
    assert checkio(u"Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
    assert checkio(u"To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it?") == 8, 'Interrogation'
    print 'All correct!'
