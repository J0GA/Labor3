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

def kmp(sub:str, s:str):
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


s1 = input()
sub1 = input()
lsub1 = len(sub1)
start_time=timeit.default_timer()
index = kmp(sub1, s1)
if index != -1:
    print(f'Подстрока "{s1[index:index+lsub1]}"найдена под индексом {index}')
else:
    print("Данной подстроки не существует")
print(f"Алгоритм Кнута-Морриса-Пратта выполнил работу за {str(timeit.default_timer() - start_time)} сек")
print()

s2 = input()
sub2 = input()
lsub2 = len(sub1)
start_time=timeit.default_timer()
index = kmp(sub2, s2)
if index != -1:
    print(f'Подстрока "{s1[index:index+lsub1]}"найдена под индексом {index}')
else:
    print("Данной подстроки не существует")
print(f"Алгоритм Кнута-Морриса-Пратта выполнил работу за {str(timeit.default_timer() - start_time)} сек")