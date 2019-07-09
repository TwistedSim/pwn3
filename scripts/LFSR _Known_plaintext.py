

"""

Plain Text: 

89 50 4E 47 0D 0A 1A 0A 00 00 00 0D

bits stream: 

10001001 01010000
01001110 01000111
00001101 00001010
00011010 00001010
00000000 00000000
00000000 00001101

Cipher Text:

43 AE 21 2C 40 33 63 C0 00 E4 FD 68

01000011 10101110
00100001 00101100
01000000 00110011
01100011 11000000
00000000 11100100
11111101 01101000

LFSR output:

1100101 011111110
0110111 101101011
0100110 100111001
0111100 111001010
0000000 011100100
1111110 101100101


LSFR output = 110010101111111001101111011010110100110100111001011110011100101000000000111001001111110101100101
plaintext   = 100010010101000001001110010001110000110100001010000110100000101000000000000000000000000000001101
ciphertext  = 010000111010111000100001001011000100000000110011011000111100000000000000111001001111110101101000


"""

def lfsr(seed, taps, n):
    sr, xor = seed, 0
    bits = ''

    for _ in range(n):        
    
        xor = sum(int(sr[t-1]) for t in taps) % 2

        out = sr[-1]
        sr = str(xor) + sr[:-1]
        xor = 0

        bits += out

    return bits

def lfsr_gen(seed, taps):
    sr, xor = seed, 0

    while True:          
        xor = sum(int(sr[t-1]) for t in taps) % 2
        out = sr[-1]
        sr = str(xor) + sr[:-1]
        xor = 0

        yield out



# Brute force the taps (assume 16 bits LFSR), taps = [1,3,11,16]

seed = '0111111101010011'
known_output = '110010101111111001101111011010110100110100111001011110011100101000000000111001001111110101100101'
for i in range(1, 2**16):
    taps = '{:0>16b}'.format(i)
    taps = [idx+1 for idx,t in enumerate(taps) if t is '1']
    out = lfsr(seed, taps, 96)
    if out.startswith(known_output):
        print('Found:', taps)
        break
 

with open('/home/simon/Desktop/challenge.png.encrypt', 'rb') as f:
	cipher = f.read()	
	cipher = '0' + bin(int(cipher.hex(),16))[2:]			
	data = ''.join(str(int(c, 2) ^ int(x, 2)) for c, x in zip(cipher, lfsr_gen(seed, taps)))	
	data = int(data, 2).to_bytes(length=len(cipher)//8, byteorder='big')
	open('/home/simon/Desktop/challenge.png', 'wb').write(data)


