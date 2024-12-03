# Задача "Средний балл"
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3],
          [5, 5, 5, 4, 5]]  # Оценки учеников в алфавитном порядке
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}  # Список учеников в классе
for i in range(len(grades)):
    grades[i] = sum(grades[i]) / len(grades[i])  # Вычисляем среднее значение для каждого вложенного списка оценок
sort_students = list(students)  # Меняем тип данных учеников класса с множества на список
sort_students.sort()  # Сортируем список учеников в алфавитном порядке
dict_students = {}  # Создаем пустой словарь
for i in range(len(grades)):
    dict_students[sort_students[i]] = grades[i]  # Заполняем словарь
print('Успеваемость учеников за 1 четверть: ', dict_students)