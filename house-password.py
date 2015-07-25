
def checkio(data):

    n = len(data)
    return all([any(map(str.isalpha, data)),
                any(map(str.isdigit, data)),
                any(map(str.isupper, data)),
                any(map(str.islower, data)),
                n >= 10])

# def checkio(data):

#     n = len(data)
#     d = [w for w in data]

#     return all([any(map(lambda e: e.isalpha(), d)),
#                 any(map(lambda e: e.isdigit(), d)),
#                 any(map(lambda e: e.isupper(), d)),
#                 any(map(lambda e: e.islower(), d)),
#                 n >= 10])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print "All correct"