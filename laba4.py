import string
import random
def generate_password(length):
    s = ''.join([i for i in (string.printable[:62]) if i not in ''])
    return (''.join(random.sample(s, length)))
def generate_passwords(count):
    return [generate_password(m) for _ in range(count)]

print("Введите количество паролей:")
n = int(input())
print("\nВведите количество символов в пароле:")
m = int(input())
print(*generate_passwords(n), sep='\n')

import random
def generate_schedule(num_exams, subjects):
    days_of_week = ["понедельник", "вторник", "среда", "четверг", "пятница"]
    hours = list(range(9, 15))
    minutes = ["00", 30]
    for i in range(num_exams):
        subject = random.choice(subjects)
        day = random.choice(days_of_week)
        time = f"{random.choice(hours)}:{random.choice(minutes)}"
        ticket = random.randint(1, 20)
        print(f"Экзамен по дисциплине «{subject}» состоится в {day} в {time}. Ваш счастливый билет {ticket}.")
num_exams = int(input("Введите количество экзаменов: "))
subjects = input("Введите наименование дисциплин через запятую и пробел: ").split(", ")
generate_schedule(num_exams, subjects)

from datetime import datetime
while True:
    year = datetime.now().year
    try:
        day = int(input("Введите дату: "))
        month = int(input("Введите месяц: "))
        start_date = datetime(year, month, day)
        end_date = datetime(year, 7, 4)
    except ValueError as err:
        print(err)
    else:
        break
print("Количество дней до экзамена: ")
print((end_date - start_date).days)

