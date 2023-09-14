
def is_prime(candidate):
    for num in range(2, candidate):
       if candidate % num == 0:
            return False
       else:
           return True
       
       
    