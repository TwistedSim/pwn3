
import itertools
from remote import Remote


with Remote('ctf.cfiul.ca', 24003) as r:

    # Received data
    data = r.recvuntil(b'\n\n')

    # Parse data
    data = data.decode().split('\n')[3]
    equation, result = data.split(' => ')

    # Format data
    result = int(result)
    n_operators = equation.count('?')
    equation = equation.replace('?', '{}')

    # Compute answer
    answer = None
    for operators in itertools.product('+-*/', repeat=n_operators):
        answer = equation.format(*operators)

        try:
            if eval(answer.replace('/', '//')) == result:
                break
        except ZeroDivisionError:
            continue

    # Send answer
    r.sendall(answer.encode())
    r.sendall(b'\n')

    print('received:', r.recvuntil(b'\n').decode())