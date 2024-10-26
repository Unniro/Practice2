first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first == second and second == third:
    print('Из введенных чисел одинаковых: 3')
elif first == second or second == third or first == third:
    print('Из введенных чисел одинаковых: 2')
else:
    print('Из введенных чисел одинаковых нет')
