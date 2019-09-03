# A natural number is called a prime if it is bigger than 1 and has no divisors other than 1 and itself.
# Write a program that takes an integer argument and returns all the primes between 1 and that integer. 
# For example, if the input is 18, you should return <2,3,5,7,11,13,17>.



# Brute force: double loop checking every indices
def generate_primes(n):
    prime = []

    i = 2
    while i <= n:
        bool_prime = 1
        j = 2
        while j < i: 
            if i % j == 0:
                bool_prime = 0
                break
            j += 1
        if bool_prime == 1:
            prime.append(i)
        i += 1
    
    print(prime)



n = 18
# n = 2
# n = 3
generate_primes(n)
