"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""
def input_data(question):
    return int(input(question))

def check_data(data, answer, question):
    while answer != data:
        print("Не верно")
        answer = input_data(question)

question1 = 'В каком году родился А.С.Пушкин? '
answer1 = input_data(question1)
check_data(1799, answer1, question1)

question2 = 'А в какой день? '
answer2 = input_data(question2)
check_data(6, answer2, question2)
print('Верно')

