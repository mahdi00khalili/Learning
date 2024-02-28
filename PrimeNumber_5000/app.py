# prime number:


import gmpy2
import random

def generate_large_prime(digits):
    lower_bound = 10**  (digits - 1)
    upper_bound = 10**  digits - 1

    while True:
        candidate = gmpy2.mpz(random.randint(lower_bound, upper_bound))
        if candidate % 2 == 0:
            candidate += 1  # Make sure the candidate is odd
        if gmpy2.is_prime(candidate):
            return int(candidate)

prime_number = generate_large_prime(5000)

print(prime_number)
