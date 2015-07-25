def left_join(phrases):
    
    list_band = isinstance(phrases, tuple)

    if list_band:
        result = filter(lambda x: len(x) > 1, phrases)
        try:
            result = ','.join(phrases).replace('right', 'left')
        except:
            result = ','.join(phrases)
        return result
    else:
        try:
            result = phrases.replace('right', 'left')
        except:
            result = phrases
        return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
