

def checkio(number):
    num_txt = str(number).replace('0', '')
    return reduce(int.__mul__, map(int, num_txt))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
