# Adapted from https://pypi.python.org/pypi/fastecdsa/
# Criptosistema Híbrido para Firma Digital usando cálculo de claves
# por curvas elípticas (parámetros Curve P256, P224) y hashing vía SHA2 y SHA3
# Modified: GIsaza (UCALDAS)

from fastecdsa import curve, ecdsa, keys
from hashlib import sha384

m = "Test Message"  
# formato de curva y de algoritmo de hashing (P256 and SHA256)
private_key = keys.gen_private_key(curve.P256)
public_key = keys.get_public_key(private_key, curve.P256)
r, s = ecdsa.sign(m, private_key)
# Debe retornar TRUE 
valid = ecdsa.verify((r, s), m, public_key)
print(valid)
##'Aumentar Sec con sha384 ECDSA '''
r, s = ecdsa.sign(m, private_key, hashfunc=sha384)
valid = ecdsa.verify((r, s), m, public_key, hashfunc=sha384)
print(valid)
##''' Otra Curva ECDSA '''
private_key = keys.gen_private_key(curve.P224)
public_key = keys.get_public_key(private_key, curve.P224)
r, s = ecdsa.sign(m, private_key, curve=curve.P224)
valid = ecdsa.verify((r, s), m, public_key, curve=curve.P224)
print(valid)
## Otra curva y sha3 ''' using SHA3 via pysha3>=1.0b1 package '''
import sha3  # pip install [--user] pysha3==1.0b1
from hashlib import sha3_256
private_key, public_key = keys.gen_keypair(curve.P256)
r, s = ecdsa.sign(m, private_key, hashfunc=sha3_256)
valid = ecdsa.verify((r, s), m, public_key, hashfunc=sha3_256)
print(valid)