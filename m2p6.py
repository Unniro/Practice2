#Задание "Слишком древний шифр"
n = int(input('Введите число из первой вставки (От 3 до 20): '))
while n < 3 or n > 20:
    print('Вы ввели неверное число, повторите ввод!')
    n = int(input('Введите число из первой вставки (От 3 до 20): '))
result = []
for i in range(1, n // 2 + 1):
    for j in range(i + 1, 20):
        if n % (i + j) == 0:
            result.append(i)
        else:
            continue
        result.append(j)
print('Ваш пароль:', *result, sep = '')