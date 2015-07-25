from string import *

VOWELS = "AEIOUY".lower()
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ".lower()

word = 'esto,esto.esto.esto-esto.'

transtab = maketrans(punctuation, ' ' * len(punctuation))

str = word.translate(transtab)
print str
