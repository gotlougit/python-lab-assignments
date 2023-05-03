perfect_numbers = []

for num in range(2, 10000):
    divisor_sum = 0
    for i in range(1, num//2 + 1):
        if num % i == 0:
            divisor_sum += i
    if divisor_sum == num:
        perfect_numbers.append(num)

print(perfect_numbers)
