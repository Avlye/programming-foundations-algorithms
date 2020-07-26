def gcd(a, b):
    while b != 0:
        previous_a = a
        a = b
        b = previous_a % b

    return a


print(gcd(60, 96))  # Should be 12
print(gcd(20, 8))  # Should be 4