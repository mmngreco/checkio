

def checkio(words_set):
    if len(words_set) < 2 and isinstance(words_set, tuple):
        return False
    else:
        res = []
        for word in words_set:
            other_words = filter(lambda x: x != word, words_set)
            res += [any([w.endswith(word) for w in other_words])]
        return any(res)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio({u"hello", u"lo", u"he"}) == True, "helLO"
    assert checkio({u"hello", u"la", u"hellow", u"cow"}) == False, "hellow la cow"
    assert checkio({u"walk", u"duckwalk"}) == True, "duck to walk"
    assert checkio({u"one"}) == False, "Only One"
    assert checkio({u"helicopter", u"li", u"he"}) == False, "Only end"