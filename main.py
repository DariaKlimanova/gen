from random import *


def generator_pr(): # формирование списка простых чисел с помощью решета Эратосфена
    n = 2000
    numbers = list(range(2, n + 1))
    for number in numbers:
        if number != 0:
            for candidate in range(2 * number, n+1, number):
                numbers[candidate-2] = 0
    return list(filter(lambda x: x != 0, numbers))


def generate(): # генерация рандомного числа в указанном диапазоне
    p = randint(0, 10000000000000000000)
    p = p | (1 << 0) # приведение числа к нечетной форме
    return p


def proverka(): 
    p = generate()
    lp = generator_pr()
    i = 0
    while i < len(lp): # в цикле делим сгенерированное число на каждый элемент списка простых чисел;
        if p % lp[i] == 0 and p != lp[i]: # если число разделится на простое, не равное себе,
            p = generate() # то запускается генерация нового числа 
            i = 0 # счетчик прохода по списку сбрасывается
        else:
            i += 1
    return p # в итоге вернем число, прошедшее проверку делением на каждое число из списка


def miller(p): # алгоритм Рабина-Миллера
    b = 0
    m = p - 1
    while m % 2 == 0:
        b, m = b + 1, m / 2 # ищем b через наибольшее число делений (p-1) на 2
    for i in range(5): # повторить 5 раз
        a = randint(1, p - 1)
        z = pow(int(a), int(m), p)  # z = a^m mod p
        if z == 1 or z == p - 1:
            continue  # p может быть простым
        for r in range(1, b):
            z = (z * z) % p # z^2 mod p
            if z == 1:
                return 'False'
            if z == p - 1:
                break
        else:
            return 'False'
    return 'True'


p = proverka()
while True:
    # print(p, miller(p))
    if miller(p) == 'False':
        p = proverka()
    else:
        break
print("Сгенерированное число: "+str(p)+'\n'+'Результат проверки:', miller(p))






