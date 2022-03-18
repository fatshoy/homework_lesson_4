class NonNumericError(Exception):
    pass


class InconsistentDataError(Exception):
    pass


try:
    a = [int(i) for i in (input('Введите первые катеты a:').split())]
    b = [int(j) for j in (input('Введите вторые катеты b:').split())]
except ValueError:
    print(NonNumericError)
else:
    if len(a) != len(b):
        print(InconsistentDataError)
    else:
        c = []
        s = []
        for i in range(len(a)):
            c.append((a[i] ** 2 + b[i] ** 2) ** 0.5)
            s.append((a[i] * b[i]) / 2)
            print(f'Треугольник {i+1} с катетами {a[i]} и {b[i]} имеет площадь {s[i]} и гипотенузу {c[i]}')
