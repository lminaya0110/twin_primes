
def is_prime(candidate):
    for num in range(2, candidate):
       if candidate % num == 0:
            return False
       else:
           return True


def find_twin_primes(upper_bound):
    twin_primes = []
    for num in range(2, upper_bound):
        second = num + 2
        if is_prime(num) and is_prime(second):
            twin_primes.append( (num,second) )