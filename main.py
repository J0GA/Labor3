import timeit
# Нужен для создания словаря в алг. Бойера-Мура
from collections import defaultdict


def prefix(s):
    P = [0] * len(s)
    i = 0
    j = 1
    while j < len(s):
        if s[i] != s[j]:
            if i > 0:
                i = P[i - 1]
            else:  # i == 0
                j += 1
        else:  # s[i] == s[j]
            P[j] = i + 1
            i += 1
            j += 1
    return P

def kmp(sub,  s, case, space):
    if case == "нет" or "Нет":  # если пользователь хочет найти подстроку, неважно в каком регистре строка и подстрока
        sub = sub.lower()
        s = s.lower()
    if space == "нет" or "Нет":  # если пользователь не хочет обращать внимания на пробелы и их количество
        sub = sub.replace(" ", "")
        s = s.replace(" ", "")
    k = 0
    l = 0
    P = prefix(sub)
    while k < len(s):
        if sub[l] == s[k]:
            k += 1
            l += 1
            if l == len(sub):
                return k - len(sub)
        elif l > 0:
            l = P[l-1]
        else:
            k += 1
    return -1

print("Алгоритм Кнута-Морриса-Пратта")
s1 = input("Введите строку: ")
sub1 = input("Введите подстроку: ")
case1 = input("Чувствительность к регистру, напишите да или нет: ")
space1 = input("Чувствительность к пробелам, напишите да или нет: ")
start_time = timeit.default_timer()
index = kmp(sub1, s1, case1, space1)
if index != -1:
    print(f'Подстрока "{sub1}" найдена под индексом {index}')
else:
    print("Данной подстроки не существует")
print(f"Алгоритм Кнута-Морриса-Пратта выполнил работу за {str(timeit.default_timer() - start_time)} сек")
print()


def displacement(subStr):
    table = [len(subStr)] * 256
    for i in range(len(subStr) - 1):
        table[ord(subStr[i])] = len(subStr) - 1 - i
    return table


# упрощённый алгоритм Бойера-Мура
def bm_search(subStr, line, case, space):
    space = space.lower()
    case = case.lower()
    _subStr = subStr
    _line = line
    if case == "нет" or "Нет":  # если пользователь хочет найти подстроку, неважно в каком регистре строка и подстрока
        _subStr = _subStr.lower()
        _line = _line.lower()
    if space == "нет" or "Нет":  # если пользователь не хочет обращать внимания на пробелы и их количество
        _subStr = _subStr.replace(" ", "")
        _line = _line.replace(" ", "")

    table = displacement(_subStr)
    i = len(_subStr) - 1
    j = i
    k = i
    while j >= 0 and i <= len(_line) - 1:
        j = len(_subStr) - 1
        k = i
        while j >= 0 and _line[k] == _subStr[j]:
            k -= 1
            j -= 1
        i += table[ord(_line[i])]

    if k >= len(_line) - len(_subStr):
        return -1
    else:
        if space == "no":
            m = 0
            n = 0
            spacesNumber = 0
            while m <= k + 1 and n <= len(line):
                if _line[m] == line[n]:
                    m += 1
                    n += 1
                else:
                    if line[n] == " ":
                        spacesNumber += 1
                        n += 1
            return k + 1 + spacesNumber
        else:
            return k + 1

print("Упрощенный алгоритм Бойера-Мура")
s2 = input("Введите строку: ")
sub2 = input("Введите подстроку: ")
case2 = input("Чувствительность к регистру, напишите да или нет: ")
space2 = input("Чувствительность к пробелам, напишите да или нет: ")
startTime = timeit.default_timer()
k = bm_search(sub2, s2, case2, space2)
print(f'Подстрока "{sub2}" найдена под индексом {k}')
print(f"Упрощенный алгоритм Бойера-Мура выполнил работу за {str(timeit.default_timer() - startTime)} сек")
print()


print("Пятнашки")
from queue import PriorityQueue


class Position:
    def __init__(self, position, start_distance, finish_distance):
        self.position = position
        self.start_distance = start_distance
        self.finish_distance = finish_distance
    def __str__(self):
        return '\n'.join((N * '{:3}').format(*[i % (N * N) for i in self.position[i:]]) for i in range(0, N * N, N))
    def __lt__(self, other):
        return self.start_distance + self.finish_distance < other.start_distance + other.finish_distance

N = 4
def shifts(position):
    zeroPosition = position.index(0)
    i, j = divmod(zeroPosition, N)
    displacement = []
    if i > 0: displacement.append(-N)  # вверх
    if i < N - 1: displacement.append(N)  # вниз
    if j > 0: displacement.append(-1)  # влево
    if j < N - 1: displacement.append(1)  # вправо
    for offset in displacement:
        swap = zeroPosition + offset
        yield tuple(
            position[swap] if x == zeroPosition else position[zeroPosition] if x == swap else position[x] for x in
            range(N * N))


def parityOfPairs(state):
    countOfPairs = 0
    for i in range(len(state) - 1):
        if state[i] > state[i + 1]:
            countOfPairs += 1
    return countOfPairs % 2


def fifteenGame(startState):
    terminalState = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)
    if parityOfPairs(startState) == 0:
        print("Нет решений")
    else:
        startState = tuple(startState)
        p = Position(startState, 0, 0)
        print(p)
        print()
        fieldStates = PriorityQueue()
        fieldStates.put(p)
        closePoints = set([p])
        parents = {p.position: None}
        while p.position != terminalState:
            p = fieldStates.get()

            for k in shifts(p.position):
                count = 0
                if k not in closePoints:
                    for m in range(len(k)):
                        if k[m] != terminalState[m]:
                            count += 1
                    fieldStates.put(Position(k, p.start_distance + 1, p.finish_distance + count))
                    parents[k] = p
                    closePoints.add(k)
        path = []
        x = p
        previous = p
        while p.position != startState:
            p = parents[p.position]
            number = p.position[previous.position.index(0)]
            path.append(number)
            previous = p
        path.reverse()
        print(path)
        print(x)


startState = [1, 2, 3, 4, 5, 7, 11, 8, 9, 6, 12, 15, 13, 10, 14, 0]
fifteenGame(startState)
