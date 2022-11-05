#
#
#

import os
from hashlib import scrypt

SCRYPT_N = 16384
SCRYPT_R = 8
SCRYPT_P = 1

#
#
#
def check_password(password, value):
    buffer = password.split(b'$')
    temp = scrypt(
        value.encode('utf-8'),
        salt=bytes.fromhex(buffer[0].decode()),
        n=SCRYPT_N,
        r=SCRYPT_R,
        p=SCRYPT_P
    ).hex().encode('utf-8')
    return (temp == buffer[1])

#
#
#
def generate_password(value):
    salt = os.urandom(32)
    temp = scrypt(
        value.encode('utf-8'),
        salt=salt,
        n=SCRYPT_N,
        r=SCRYPT_R,
        p=SCRYPT_P
    )
    return (salt.hex().encode('utf-8') + b'$' + temp.hex().encode('utf-8'))
