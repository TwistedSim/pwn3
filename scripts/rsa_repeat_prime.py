
from encode import decode_rsa
from modular import gcd
from conversion import Integer

exponent = 65537
m1 = Integer.from_b64(b'A6PkKi8WkabY8Uk3qYZH0C4CAXHNnJldZnT68taohRQHJVi6zsZRFzI29hB1mAKMztFyg0eHwkhiFkqiyKKAlQs=')
m2 = Integer.from_b64(b'Ay8N/PIIWYqGETA3JY9/kZG5+hctifI9z09zfJC9NtocsCNUDGnW9YPd6746zohnX3lg1mvWl0eldN01CgrJ7A8=')
cipher_text = Integer.from_b64(b'2LaTAyHDqznnLYr7b01onsM9O1D9Xh4KA9qkHj+Plujg0ArIuHgsaEjIGtuLEwfA37VaVdFbEbXQY5OlE0tC4g==')

p = gcd(m1, m2)
q1, q2 = m1 // p, m2 // p

print(Integer(decode_rsa(cipher_text, p, q1, exponent)))
