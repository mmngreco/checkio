#!/usr/bin/env
# -*- coding:utf-8 -*-

# s.isalnum()
# s.isdigit()
# s.isnumeric()
# s.isalpha()
# s.islower()
# s.isupper()


def checkio(data):
    # Conditions for strong password:
    # n ≥ 10
    # numbers ≥ 1
    # lower ≥ 1
    # upper ≥
    n = len(data)
    d = [w for w in data]

    return all([any(map(lambda e: e.isdigit(), d)),
                any(map(lambda e: e.isalpha(), d))
                any(map(lambda e: e.isupper(), d)),
                any(map(lambda e: e.islower(), d)),
                n >= 10])

print checkio('bAse730onE4')
print checkio('A1213pokl')