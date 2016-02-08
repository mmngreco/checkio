def checkio(first, second):
    f_list = set(first.split(','))
    s_list = set(second.split(','))
    result = list(f_list & s_list)
    try:
        return ','.join(sorted(result))
    except:
        return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"hello,world", u"hello,earth") == "hello", "Hello"
    assert checkio(u"one,two,three", u"four,five,six") == "", "Too different"
    assert checkio(u"one,two,three", u"four,five,one,two,six,three") == "one,three,two", "1 2 3"
