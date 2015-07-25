FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    txt_num = str(number).strip()
    number = int(txt_num)
    n = len(str(number))

    if n == 1:  # one digit
        return FIRST_TEN[number - 1]

    elif n == 2:  # two digits
        ii = int(txt_num[0])  # tens
        i = int(txt_num[1])  # units

        if ii == 1:  # in first tens
            return SECOND_TEN[number - 10]

        elif ii >= 2:  # in other tens
            if i == 0:  # round number
                return OTHER_TENS[ii - 2]
            else:
                return OTHER_TENS[ii - 2] + ' ' + FIRST_TEN[i - 1]

    elif n == 3:  # three digits
        i = int(txt_num[2])  # hundred
        ii = int(txt_num[1])  # tens
        iii = int(txt_num[0])  # units

        if ii >= 2:  # other tens
            if i == 0:  # round number
                return FIRST_TEN[iii - 1] + ' ' + HUNDRED + ' ' + OTHER_TENS[ii - 2]
            else:
                return FIRST_TEN[iii - 1] + ' ' + HUNDRED + ' ' + OTHER_TENS[ii - 2] + ' ' + FIRST_TEN[i - 1]

        elif ii == 1:  # first tens
            return FIRST_TEN[iii - 1] + ' ' + HUNDRED + ' ' + SECOND_TEN[i]

        elif ii == 0:  # 0 = tens
            if i == 0:  # 0 = units
                return FIRST_TEN[iii - 1] + ' ' + HUNDRED
            else:
                return FIRST_TEN[iii - 1] + ' ' + HUNDRED + ' ' + FIRST_TEN[i - 1]

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print u"All correct!"
