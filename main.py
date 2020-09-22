from random import *


def generator_pr():
    n = 2000
    numbers = list(range(2, n + 1))
    for number in numbers:
        if number != 0:
            for candidate in range(2 * number, n+1, number):
                numbers[candidate-2] = 0
    return list(filter(lambda x: x != 0, numbers))


def generate():
    p = randint(0, 10000000000000000000)
    p = p | (1 << 0)
    return p


def proverka():
    p = generate()
    lp = generator_pr()
    i = 0
    while i < len(lp):
        if p % lp[i] == 0 and p != lp[i]:
            p = generate()
            i = 0
        else:
            i += 1
    return p


def miller(p):
    b = 0
    m = p - 1
    while m % 2 == 0:
        b, m = b + 1, m / 2
    for i in range(5):
        a = randint(1, p - 1)
        z = pow(int(a), int(m), p)  # z = a^m mod p
        if z == 1 or z == p - 1:
            continue  # p может быть простым
        for r in range(1, b):
            z = (z * z) % p
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






