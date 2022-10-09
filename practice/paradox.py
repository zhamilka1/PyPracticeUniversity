import random as rnd
import math
def monty_hall(n):
    success_counter_without_changing = 0
    success_counter_with_random_changing = 0
    success_counter_with_changing = 0
    for i in range(0, n):
        door = rnd.randrange(1, 4)
        choise_of_watcher = rnd.randrange(1, 4)
        choise_of_show = 0
        if (choise_of_watcher == 1):
            if (door == 1):
                choise_of_show = rnd.randrange(2, 4)
                success_counter_without_changing += 1
            elif (door == 2):
                choise_of_show = 3
            else:
                choise_of_show = 2
        elif (choise_of_watcher == 2):
            if (door == 2):
                success_counter_without_changing += 1
                choise_of_show = rnd.randrange(1, 3)
                if (choise_of_show == 1):
                    choise_of_show = 1
                else:
                    choise_of_show = 3
            elif (door == 1):
                choise_of_show = 3
            else:
                choise_of_show = 1
        else:
            if (door == 3):
                success_counter_without_changing += 1
                choise_of_show = rnd.randrange(1, 3)
            elif (door == 2):
                choise_of_show = 1
            else:
                choise_of_show = 2
        change = rnd.randrange(1, 3)
        buffer = 0
        if (change == 1):
            if ((choise_of_watcher == 1) and (choise_of_show == 3)) or (
                    (choise_of_watcher == 3) and (choise_of_show == 1)):
                buffer = 2
            elif ((choise_of_watcher == 2) and (choise_of_show == 3)) or (
                    (choise_of_watcher == 3) and (choise_of_show == 2)):
                buffer = 1
            else:
                buffer = 3
        if (door == buffer):
            success_counter_with_random_changing += 1
        buffer = 0
        if ((choise_of_watcher == 1) and (choise_of_show == 3)) or ((choise_of_watcher == 3) and (choise_of_show == 1)):
            buffer = 2
        elif ((choise_of_watcher == 2) and (choise_of_show == 3)) or (
                (choise_of_watcher == 3) and (choise_of_show == 2)):
            buffer = 1
        else:
            buffer = 3
        if (door == buffer):
            success_counter_with_changing += 1
    print(f"if we dont change: {round(success_counter_without_changing/n, 2)*100} if we randomly change: {round(success_counter_with_random_changing/n, 2)*100} if we change everytime: {round(success_counter_with_changing/n, 2) *100}")


def birthday_paradox(N):
    days = 12 * 28  # DAYS IN YEAR
    var_other = 1  #
    for i in range(1, N + 1):
        var_this_person = i / days
        var_other *= (1 - var_this_person)
        var = 1 - var_other
        if i == (N):
            procent = int
            procent = round(var, 2) * 100
            print(f"{procent}%")
birthday_paradox2(23)

