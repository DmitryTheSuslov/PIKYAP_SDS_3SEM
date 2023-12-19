import sys
import math


def get_coef(index, prompt):
    try:
        coef_str = sys.argv[index]
    except:
        print(prompt)
        coef_str = input()
    flag = True
    while flag:
        try:
            coef = float(coef_str)
            flag = False
        except:
            coef_str = input("Некорректный ввод. Попробуйте ещё раз: ")
    return coef


def get_squares_roots(a, b, c):
    result = []
    D = b * b - 4 * a * c
    if a == 0:
        result.append(-c / b)
        return result
    if D == 0.0:
        root = -b / (2.0 * a)
        result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)
        result.append(root1)
        result.append(root2)
    return result


def get_roots(roots):
    res = []
    for root in roots:
        if root > 0:
            res.extend([math.sqrt(root), -math.sqrt(root)])
        elif root == 0 and not 0 in res:
            res.append(0)
    return res


def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    squares_roots = get_squares_roots(a, b, c)
    roots = get_roots(squares_roots)
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет действительных корней')
    elif len_roots == 1:
        print('Один действительный корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два действительных корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три действительных корня: {}, {}, {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре действительных корня: {}, {}, {}, {}'.format(roots[0], roots[1], roots[2], roots[3]))

if __name__ == "__main__":
    main()