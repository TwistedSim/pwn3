

def int2str(integer: int) -> str:
    """return an ascii string"""
    return hex2str(int2hex(integer))

def str2hex(string: str) -> str:
    return ''.join(hex(ord(char))[2:] for char in string)

def hex2str(hex_string: str) -> str:
    """Only works with ascii (2 bytes) strings."""
    bytes_pairs = zip(*[iter(hex_string)] * 2)
    return ''.join(chr(hex2int(byte1 + byte2)) for byte1, byte2 in bytes_pairs)

def str2int(string: str) -> int:
    return int(str2hex(string), base=16)

def hex2int(hex_string: str) -> int:
    return int(hex_string, base=16)

def int2hex(integer: int) -> str:
    return bytes2hex(int2bytes(integer))

def int2bytes(integer: int, byteorder: str='big') -> bytes:
    n_bytes = (integer.bit_length()+7) // 8
    return integer.to_bytes(n_bytes, byteorder=byteorder)

def bytes2int(bytes_str: bytes, byteorder: str='big') -> int:
    return int.from_bytes(bytes_str, byteorder=byteorder)

def bytes2hex(bytes_str: bytes) -> str:
    return bytes_str.hex()

def hex2bytes(hex_string: str) -> bytes:
    return bytes.fromhex(hex_string)

def bytes2str(bytes_str: bytes, encoding: str='utf-8', errors: str='strict') -> str:
    return bytes_str.decode(encoding=encoding, errors=errors)

def str2bytes(string: str, encoding: str='utf-8') -> bytes:
    return bytes(string, encoding=encoding)
