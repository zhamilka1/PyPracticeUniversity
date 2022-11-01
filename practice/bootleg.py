import paradox
import wheel_of_fortune
import file_controller
import flight_journal
import book_practice

def boot():
    choise = int(input("What practice you wanna boot?"))
    if(choise == 1):
        print("This is monty hall paradox:")
        iterations = int(input("How many iterations you wanna complicate?"))
        print(paradox.monty_hall(iterations))
    elif(choise == 2):
        print("This is birthday paradox")
        iterations = int(input("Put number of iterations"))
        number = int(input("Put number of people"))
        print(paradox.birthday(iterations, number))
    elif(choise == 3):
        print("This is wheel_of_fortune")
        wheel_of_fortune.play()
    elif(choise == 4):
        print("This is flight journal, it takes bad_journal and makes good_journal")
        flight_journal.journal_parser("good_journal.txt", "bad_journal.txt")
    elif(choise == 5):
        print("This is file error checker")
    elif(choise == 6):
        print("This is file_controller")
        flight_journal.journal_parser("bad_journal.txt", "good_journal.txt")
boot()