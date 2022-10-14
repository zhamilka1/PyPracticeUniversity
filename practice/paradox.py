import random as rnd
def monty_hall(n):
    stay = 0
    change = 0
    for i in range(0, n):
        car = rnd.randrange(1, 4)
        watcher = rnd.randrange(1, 4)
        if (car == watcher):
            stay += 1
        else:
            change += 1
    print(f"if we dont change: {round(stay/n, 2)*100} if we change everytime: {round(change/n, 2) *100}")


def birthday_paradox(n, number):
    year = 365
    counter = 0
    for i in range(0, n):
        birthdays = []
        for i in range(0, number):
            birthday = rnd.randrange(1, year)
            if(birthday in birthdays):
                counter +=1
                break
            birthdays.append(birthday)
    print(counter/n)