immutable_var = ([1, 2, 3, 4, 5], "пример", 5)
print(immutable_var)
immutable_var[0][0] = 5
# immutable_var[2] = "новый пример" - в кортеже невозможно изменить элементы, за исключением списка внтури котежа
print(immutable_var)
mutable_list = [1, 2, 3, 4, 5, "пример"]
mutable_list[3] = "пример замены"
print(mutable_list)
