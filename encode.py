
import warnings

from modular import lcm, modinv
import base64
from string import ascii_lowercase
from queue import deque
from itertools import cycle


def xor_bytes(msg: bytes, key: bytes) -> bytes:
    return bytes(m ^ k for m, k in zip(msg, cycle(key)))

def encode_rsa(plain_text: int, modulus: int, exponent: int) -> int:
    if plain_text > modulus: warnings.warn('Integer to encode is bigger than the modulus.', stacklevel=2)
    return pow(plain_text, exponent, modulus)

def decode_rsa(cipher: int, p: int, q: int, exponent: int) -> int:
    modulus = p * q
    if cipher > modulus: warnings.warn('Integer to encode is bigger than the modulus.', stacklevel=2)
    t = lcm(p - 1, q - 1)
    d = modinv(exponent, t)
    return pow(cipher, d, modulus)

def b64_encode(bytes_str: bytes) -> bytes:
    return base64.b64encode(bytes_str)

def b64_decode(bytes_str: bytes) -> bytes:
    return base64.b64decode(bytes_str)

def caesar_encode(msg: bytes, shift: int, *, alphabet: str=bytes(ascii_lowercase, 'utf-8'), case_sensitive: bool=False):

    if not case_sensitive: msg = msg.lower()

    shifted_alphabet = deque(alphabet)
    shifted_alphabet.rotate(-shift)

    mapping = dict(zip(alphabet, shifted_alphabet))
    mapping.update({excluded_char:excluded_char for excluded_char in msg if excluded_char not in alphabet})

    return bytes(mapping[byte] for byte in msg if byte)

def caesar_decode(msg: bytes, shift: int, **kwargs):
    return caesar_decode(msg, -shift, **kwargs)

def rot13(msg: bytes):
    return caesar_encode(msg, 13, case_sensitive=False)
