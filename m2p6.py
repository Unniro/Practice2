#Задание "Слишком древний шифр"
def digit(input('Введите число изображенное на первой вставке (От 3 до 20): '))
while digit < 3 or digit > 20:
digit()
    print('Вы ввели неверное число, повторите ввод')
result = []
for i in range(1, 20):
    for j in range(1, 20):
        if digit % (i + j) == 0:
            result.append(i)
        else:
            continue
        result.append(j)
print ('Ваш пароль:', *result)