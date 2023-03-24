from itertools import permutations, combinations


opus = list(permutations((1, 2, 3, 4)))  # множество всех существующих перестановок из 4 элементов
# print(*perms, sep='\n')

# перестановка записана как набор элементов, получающийся в результате её выполнения
# так, тождественная перестановка это (1, 2, 3, 4)


def composition(perm1: tuple, perm2: tuple) -> tuple:  # эта функция вычисляет композицию двух
    # перестановок
    return tuple(perm1[i - 1] for i in perm2)


def is_group(perms: set) -> int:  # проверка на то, является ли множество перестановок группой
    for a, b in permutations(perms, 2):
        if composition(a, b) not in perms:
            return 0
    for a in perms:
        if composition(a, a) not in perms:
            return 0
    return 1


file = open('S4.txt', 'w')

# далее проверяем для всех множеств перестановок мощности 1, 2, 3, 4, 6, 8, 12, 24 на то,
# являются ли они группами
# можно проверять только эти мощности в силу теоремы Лагранжа

for candidate in combinations(opus, 1):
    if is_group({*candidate}):
        print(*candidate, sep='; ')
        print(*candidate, sep='; ', file=file)

for candidate in combinations(opus, 2):
    if is_group({*candidate}):
        print(*candidate, sep='; ')
        print(*candidate, sep='; ', file=file)

for candidate in combinations(opus, 3):
    if is_group({*candidate}):
        print(*candidate, sep='; ')
        print(*candidate, sep='; ', file=file)

for candidate in combinations(opus, 4):
    if is_group({*candidate}):
        print(*candidate, sep='; ')
        print(*candidate, sep='; ', file=file)

for candidate in combinations(opus, 6):
    if is_group({*candidate}):
        print(*candidate, sep='; ')
        print(*candidate, sep='; ', file=file)

for candidate in combinations(opus, 8):
    if is_group({*candidate}):
        print(*candidate, sep='; ')
        print(*candidate, sep='; ', file=file)

for candidate in combinations(opus, 12):
    if is_group({*candidate}):
        print(*candidate, sep='; ')
        print(*candidate, sep='; ', file=file)

for candidate in combinations(opus, 24):
    if is_group({*candidate}):
        print(*candidate, sep='; ')
        print(*candidate, sep='; ', file=file)

# результат запишем в файл S4.txt
# для перевода в удобоваримый вид воспользуемся кодом из writing.py
