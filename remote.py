import socket


class Remote(socket.socket):

    def __init__(self, host: str, port: int, *args, **kwargs):
        super().__init__(socket.AF_INET, socket.SOCK_STREAM, *args, **kwargs)
        self.connect((host, port))

    def recvuntil(self, sentinel: bytes = b'\n', *, buffer_size: int = 1024) -> bytes:
        return recvuntil(self, sentinel, buffer_size=buffer_size)


def recvuntil(s: socket.socket, sentinel: bytes=b'\n', *,  buffer_size: int=1024) -> bytes:

    data = b''
    while sentinel not in data:
        data += s.recv(buffer_size)

    return data