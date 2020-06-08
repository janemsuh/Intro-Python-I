# Write a program to determine if a number, given on the command line, is prime.
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

num = input("Enter a number: ")
num = int(num)

if is_prime(num):
    print(f'{num} is prime!')
else:
    print(f'Not prime.')

# Implement the Sieve of Eratosthenes: print all of the prime numbers less than or equal to num
def allPrimes(num):
    prime = [True for i in range(num+1)]
    p = 2
    while (p <= num**0.5):
        if (prime[p] == True):
            for i in range(p*2, num+1, p):
                prime[i] = False
        p += 1
    for p in range(2, num+1):
        if prime[p]:
            print(p, end = " ")
    print('\n')

num = input("Enter a number: ")
num = int(num)
allPrimes(num)