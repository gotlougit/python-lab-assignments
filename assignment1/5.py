def is_prime(num):
    if num < 2:
        return False
    for i in range(2, (num//2)+1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(n):
    sum = 0
    for i in range(2, n+1):
        if is_prime(i):
            sum += i
    return sum

n = int(input("Enter a number: "))
result = sum_of_primes(n)
print("Sum of all prime numbers less than or equal to", n, "is", result)
