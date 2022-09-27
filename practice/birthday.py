import random as rnd
days_in_year = 336
students_number = int(input())
students_birthday = []
unique_counters = 0
colab_counters = 0
pares_counter = (students_number * (students_number-1))/2
for i in range(students_number):
    students_birthday.append(int(rnd.randrange(1, days_in_year)))
for i in range(students_number):
    flag = False
    for j in range(i+1, students_number):
        if(students_birthday[i]==students_birthday[j]):
            colab_counters +=1
            flag = True
    if not flag:
        unique_counters+=1
print(unique_counters, colab_counters)

