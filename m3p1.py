#Задача "Счётчик вызовов"
calls = 0
def count_calls():
    global calls
    calls = calls + 1
    return calls
def string_info(string):
    count_calls()
    string = (len(string), string.count())
    return string
def is_contains(string, list_to_search):
    count_calls()

string_info(input())
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)