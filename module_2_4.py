numbers_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in range(len(numbers_)):
    for j in range(2, len(numbers_)):
        if numbers_[i] == 1:
            break
        elif numbers_[i] % j == 0 and j < numbers_[i]:
            is_prime = False
        elif numbers_[i] % j == 0 and j == numbers_[i]:
            is_prime = True
        elif numbers_[i] % j != 0:
            continue
        if is_prime == True:
            primes.append(numbers_[i])
            break
        elif is_prime == False:
            not_primes.append(numbers_[i])
            break
print('Primes: ', primes)
print('Not Primes: ', not_primes)