limit = 1000
prime_sum = 0

for n in range(2, limit):
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            break
    else:
        prime_sum += n

print(prime_sum)
