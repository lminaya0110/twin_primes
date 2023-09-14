
def is_prime(candidate):
    for num in range(2, candidate):
       if candidate % num == 0:
            return False
       else:
           return True


def find_twin_primes(upper_bound):
    twin_primes = [ (num, num + 2) for num in range(2, bound) if is_prime(num) and is_prime(num+2)]
    return twin_primes

bound = 1_000
twin_primes = find_twin_primes(bound)

for pair in twin_primes:
    print(f'{pair[0]} and {pair[1]} are twin primes')
    
