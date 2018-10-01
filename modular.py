
from typing import Tuple, List

def egcd(a: int, b: int) -> Tuple[int, int, int]:
    """ Extended euclidean algorithm, compute gcd(a,b) as well as the bezout's identity (ax+by = gcd(a,b))"""
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a: int, m: int) -> int:
    """ Compute the modular inverse of a number"""
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def gcd(a, b):
    """ compute the greatest common divisor of a and b"""
    return gcd(b % a, a) if a != 0 else b

def gcd2(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    """ Compute the lowest common multiple of a and b"""
    return a * b // gcd(a, b)

def factors(n: int) -> List[int]:
    from functools import reduce
    return sorted(list(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))))
