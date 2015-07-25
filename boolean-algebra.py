OPERATION_NAMES = ("conjunction",
                   "disjunction",
                   "implication",
                   "exclusive",
                   "equivalence")


def boolean(x, y, operation):
    conjunction = bool(x) and bool(y)
    disjunction = bool(x) or bool(y)
    implication = bool(y) or not disjunction
    exclusive = disjunction and not conjunction
    equivalence = not exclusive

    ops = [conjunction,
           disjunction,
           implication,
           exclusive,
           equivalence]
    return ops[OPERATION_NAMES.index(operation)]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, u"conjunction") == 0, "and"
    assert boolean(1, 0, u"disjunction") == 1, "or"
    assert boolean(1, 1, u"implication") == 1, "material"
    assert boolean(0, 1, u"exclusive") == 1, "xor"
    assert boolean(0, 1, u"equivalence") == 0, "same?"
