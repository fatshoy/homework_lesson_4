class NonNumericError (Exception):
    pass


class InconsistentDataError (Exception):
    pass


try:
    string = [int(i) for i in input('Введите катеты:').split()]
except ValueError:
    print(NonNumericError)
else:
    if len(string) % 2 != 0:
        print(InconsistentDataError)
    else:
        a = [i for i in string if i % 2 != 0]
        b = [i for i in string if i % 2 == 0]
        c = []
        s = []
        for i in range(len(a)):
            c.append((a[i] ** 2 + b[i] ** 2) ** 0.5)
            s.append((a[i] * b[i]) / 2)
            print(f'Треугольник {i+1} с катетами {a[i]} и {b[i]} имеет площадь {s[i]} и гипотенузу {c[i]}')
