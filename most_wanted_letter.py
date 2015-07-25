#!/usr/bin/env
# -*- coding:utf-8 -*-

from string import punctuation


def checkio(text):

    count = dict()
    for letter in text:
        if letter in punctuation + ' ': continue
        if letter.isnumeric(): continue
        count[letter.lower()] = count.get(letter.lower(), 0) + 1

    count_sorted = sorted([(v, k) for k, v in count.items()], reverse=True)
    count_filter = filter(lambda x: x[0] == count_sorted[0][0], count_sorted)
    return count_filter[-1][1]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"Hello World!") == "l", "Hello test"
    assert checkio(u"How do you do?") == "o", "O is most wanted"
    assert checkio(u"One") == "e", "All letter only once."
    assert checkio(u"Oops!") == "o", "Don't forget about lower case."
    assert checkio(u"AAaooo!!!!") == "a", "Only letters."
    assert checkio(u"abe") == "a", "The First."
    print("Start the long test")
    assert checkio(u"a" * 9000 + u"b" * 1000) == "a", "Long."
    print("The local tests are done.")
