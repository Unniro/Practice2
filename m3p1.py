# Задача "Счётчик вызовов"
calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    count_calls()
    string = (len(string), string.upper(), string.lower())
    return string


def is_contains(string, list_to_search):
    count_calls()
    copy_list_to_search = [j.casefold() for j in list_to_search]
    for i in range(len(list_to_search)):
        if string.casefold() in copy_list_to_search:
            return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)