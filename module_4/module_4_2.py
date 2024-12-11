def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()


# inner_function() - При вызове вложенной функции, её имя не определяется,
#                   так как она в объемлющем пространстве имен функции test_function
#                   и может быть вызвана только внутри нее
test_function()