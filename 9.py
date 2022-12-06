from random import randint
import logging
logging.basicConfig(level=logging.INFO, filename="Задание_9_Логирование.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

def k_check():  # обработчик ошибки ввода числа k
    while True:
        try:
            k = int(input("Введите кол-во попыток отгадать число: "))
            return k
        except ValueError:
            print("Нужно ввести цифру!")

def N_check():  # обработчик ошибки ввода числа N
    while True:
        try:
            N = int(input("Введите верхний предел чисел: "))
            return N
        except ValueError:
            print("Нужно ввести цифру!")

def Try_check():  # обработчик ошибки ввода числа пользователя
    while True:
        try:
            Try = int(input("Введите ваше число: "))
            return Try
        except ValueError:
            print("Нужно ввести цифру!")

i = 0
k = k_check()
logging.info('Пользователь выбрал данное число : ' + str(k))
N =  N_check()
logging.info('Пользователь выбрал данное число N: ' + str(N))
num = randint(1, N) #узнаем число
logging.info('Программа выбрала данное число: ' + str(num))
while i != k+1:
    if i == k:
        print ('Попытки кончились :(')
        logging.info('У пользователя кончились попытки')
        break
    Try = Try_check()
    logging.info('Пользователь ввёл данное число: ' + str(Try))
    if Try < num:
        print ('Ваше число меньше, чем загаданное')
        i += 1
        logging.info('Число пользователя (' + str(Try) +') оказалось меньше, чем загаданное (' + str(num) + ')')
    if Try > num:
        print ('Ваше число больше, чем загаданное')
        i += 1
        logging.info('Число пользователя (' + str(Try) +') оказалось больше, чем загаданное (' + str(num) + ')')
    if Try == num:
        print ('Вы угадали!')
        logging.info('Пользователь отгадал число ' + str(num) +' c ' + str(i) + ' попытки')
        break
