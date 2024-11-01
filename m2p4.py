# Задача "Всё не так уж просто"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    for j in range(len(numbers)):
        print(i, j, numbers[i], numbers[j])
        if numbers[i] % numbers[j] == 0 and i < j:
            primes.append(numbers[i])
        else:
            not_primes.append(numbers[i])
print('Primes: ', primes)
print('Not Primes: ', not_primes)