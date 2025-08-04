'''def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
        else:
            return True

def get_primes(nums):
    primes = []
    for num in nums:
        if is_prime(num):
            primes.append(num)
    return primes

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Primes:", get_primes(numbers))


wrong Primes: [2, 3, 5, 7, 9]
correct Primes: [2, 3, 5, 7]

'''



def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True          #problem in the else statement

def get_primes(nums):
    primes = []
    for num in nums:
        if is_prime(num):
            primes.append(num)
    return primes

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Primes:", get_primes(numbers))
