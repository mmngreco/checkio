def checkio(number):
    food = number
    time = 0
    pigeons = [0]

    while food:
        time += 1
        pigeons += [pigeons[-1] + time]
        food -= pigeons[-1]
        p = pigeons[-1]

        if food == p:
            return p
        elif food <= 0:
            pigeons[-1] = pigeons[-1] + food
            return max(pigeons)
