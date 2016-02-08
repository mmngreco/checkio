
def checkio(data):

    n = len(data)
    band = True if n % 2 == 0 else False
    data.sort()
    if band:
        return sum(data[n / 2 - 1:n / 2 + 1]) / 2.0
    else:
        return data[n / 2]
