import random as rnd
def monty_hall(n):
    stay = 0
    change = 0
    for i in range(0, n):
        if (rnd.randrange(1, 4) == rnd.randrange(1, 4)):
            stay += 1
        else:
            change += 1
    returnable = str(f"if we dont change: {round(stay/n, 2)*100} % if we change everytime: {round(change/n, 2) *100} %")
    return returnable

def birthday(n, number):
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
    returnable = str(f"possibility is: {round(counter/n*100)} %")
    return returnable
