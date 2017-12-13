# a)
def is_prime(n):
  if n > 1:
   for x in range(2,n):
       if (n % x) == 0:
           print(False)
           break
   else:
       print(True)
  else:
    print(False)

is_prime(3)


# b)
def is_prime_dos(n):
        if n == 2 or n ==3:
            return print(True)
        if n % 2 == 0 or n % 3 == 0:
            return print(False)

        i = 5
        x = 2
        squared = int(n ** .5) + 1
        while i <= squared:
            if n % i == 0:
                return print(False)
            i += x
            x = 6 - x
        return print(True)

is_prime_dos(1)


# c)
def prime_numbers(n):
    prime_list = []
    for number in range(1, n+1):
        if all(number % i != 0 for i in range(2, number)):
            prime_list.append(number)
    print(prime_list)
    
prime_numbers(100)


# d)
def first_n_primes(n):
    prime_list = []

    i = 2
    while len(prime_list) != n:
        for number in range(2, i// 2 + 1):
            if i % number == 0:
                break
        else:
            prime_list.append(i)
        i += 1

    return print(prime_list)

first_n_primes(10)
