# Лабораторная работа №6 (Вариант 4)
## Описание проделанной работы
- Задание 1
Условие:Настя составляет 6-буквенные коды из букв Н, А, С, Т, Я. Каждая допустимая гласная буква может входить в код не более одного раза. Сколько кодов может составить Настя?
Решение:
```
from itertools import *
k=0
a = 'НАСТЯ'
for i in product(a,repeat=6):
    s=''.join(i)
    if s.count('А')<=1 and s.count('Я')<=1:
        k+=1
print(k)
```
Результат:
<image src = 1.png alt="результат программы">

- Задание 2
Условие:Значение арифметического выражения 16** 18 * 4** 10 - 46 -16 записали в системе счисления с основанием 4. Сколько цифр 3 содержится в этой записи?
Решение:
```
x = 16**18 * 4**10 - 46 -16
s = []
while x!=0:
    s+=[x%4]
    x//=4
s=s[::-1]
print(s.count(3))
```
Результат:
<image src = 2.png alt="результат программы">

- Задание 3
Условие:Пусть M  — сумма минимального и максимального натуральных делителей целого числа, не считая единицы и самого числа. Если таких делителей у числа нет, то считаем значение M равным нулю. Найдите целые числа, большие 452 021, в порядке возрастания, такие, для которых значение M при делении на 7 даёт в остатке 3. Вывести первые 5 найденных чисел и соответствующие им значения M.

Формат вывода: для каждого из 5 таких найденных чисел в отдельной строке сначала выводится само число, затем  — значение M. Строки выводятся в порядке возрастания найденных чисел.

Например, для числа 20: M = 2 + 10 = 12, остаток при делении на 7 не равен 3; для числа 21: M  =  3 + 7  =  10, остаток при делении на 7 равен 3.
Решение:
```
k = 0
for x in range(452022, 1000000):
    a = []
    for delit in range(2,x):
        if x % delit == 0:
            a.append(delit)
            if len(a) >= 2:
                M = a[0] + a[-1]
            else:
                M = 0
    if M % 7 == 3:
        k += 1
        print(x , M)
    if k == 5:
        break
```
Результат:
<image src = 3.png alt="результат программы">

### Сcылки на используемые материалы
- https://evil-teacher.on.fleek.co/prog_pm/term1/lab06/
- https://doka.guide/tools/markdown/
- https://kompege.ru/course
- https://proglib.io/p/iteriruemsya-pravilno-20-priemov-ispolzovaniya-v-python-modulya-itertools-2020-01-03