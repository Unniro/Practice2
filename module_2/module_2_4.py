# Задача "Всё не так уж просто"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    is_prime = True
    for j in range(2, numbers[i] - 1):
        if numbers[i] % j == 0:
            is_prime = False
            break
    if numbers[i] == 0 or numbers[i] == 1:
        continue
    if is_prime is True:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])
print('Primes: ', primes)
print('Not Primes: ', not_primes)