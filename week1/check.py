from math import sqrt                                                    
def is_prime(n):
    if (n < 2):
        return 0
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i == 0):
            return 0 # Không là số nguyên tố
    return 1 # Là số nguyên tố