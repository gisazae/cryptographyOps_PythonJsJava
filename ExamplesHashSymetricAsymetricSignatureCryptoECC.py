# Examples pyCrypto
# Taken from : https://github.com/dlitz/pycrypto/blob/master/lib/Crypto/PublicKey/DSA.py
# http://www.laurentluce.com/posts/python-and-cryptography-with-pycrypto/
# Different testing Crypto Algorithms
# Modified by G. Isaza Abrl 2016. UCaldas

# Hashing with SHA
from Crypto.Hash import SHA256
SHA256.new('abc').hexdigest()
>>'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'

from Crypto.Hash import SHA256
	def check_password(clear_password, password_hash):
	    return SHA256.new(clear_password).hexdigest() == password_hash

# Symetric DES
	from Crypto.Cipher import DES
	des = DES.new('01234567', DES.MODE_ECB)
	text = 'abcdefgh'
	cipher_text = des.encrypt(text)
	cipher_text
	'\xec\xc2\x9e\xd9] a\xd0'
	des.decrypt(cipher_text)
	'abcdefgh'

# Symetric DES with CFB+IV
from Crypto.Cipher import DES
from Crypto import Random
iv = Random.get_random_bytes(8)
des1 = DES.new('01234567', DES.MODE_CFB, iv)
des2 = DES.new('01234567', DES.MODE_CFB, iv)
text = 'abcdefghijklmnop'
cipher_text = des1.encrypt(text)
cipher_text
"?\\\x8e\x86\xeb\xab\x8b\x97'\xa1W\xde\x89!\xc3d"
des2.decrypt(cipher_text)
'abcdefghijklmnop'

# Stream Cipher Rc4
from Crypto.Cipher import ARC4
obj1 = ARC4.new('01234567')
obj2 = ARC4.new('01234567')
text = 'abcdefghijklmnop'
cipher_text = obj1.encrypt(text)
cipher_text
'\xf0\xb7\x90{#ABXY9\xd06\x9f\xc0\x8c '
obj2.decrypt(cipher_text)
'abcdefghijklmnop'

# Public RSA with 1024 key
from Crypto.PublicKey import RSA
from Crypto import Random
random_generator = Random.new().read
key = RSA.generate(1024, random_generator)
 key
RSAobj @0x7f60cf1b57e8 n(1024),e,d,p,q,u,private>
key.can_encrypt()
True
key.can_sign()
True
key.has_private()
True
public_key = key.publickey()
enc_data = public_key.encrypt('abcdefgh', 32)
enc_data
#('\x11\x86\x8b\xfa\x82\xdf\xe3sN ~@\xdbP\x85
public_key = key.publickey()key.decrypt(enc_data)
'abcdefgh'

# Signature Sign and Verify Long Process
# First HASH with SHA256 then RSA with private key
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
random_generator = Random.new().read
key = RSA.generate(1024, random_generator)
text = 'abcdefgh'
hash = SHA256.new(text).digest()
hash
'\x9cV\xccQ\xb3t\xc3\xba\x18\x92\x10\xd5\xb6\xd4\xbfWy\r5\x1c\x96\xc4|\x02\x19\x0e\xcf\x1eC\x065\xab'
signature = key.sign(hash, '')
text = 'abcdefgh'
hash = SHA256.new(text).digest()
public_key = key.publickey()
public_key.verify(hash, signature)
True


#Crypt and Decrypt File
import os
from Crypto.Cipher import DES3
 
def encrypt_file(in_filename, out_filename, chunk_size, key, iv):
    des3 = DES3.new(key, DES3.MODE_CFB, iv)
	 
    with open(in_filename, 'r') as in_file:
        with open(out_filename, 'w') as out_file:
            while True:
                chunk = in_file.read(chunk_size)
	                if len(chunk) == 0:
	                    break
	                elif len(chunk) % 16 != 0:
	                    chunk += ' ' * (16 - len(chunk) % 16)
	            	out_file.write(des3.encrypt(chunk))
	 
def decrypt_file(in_filename, out_filename, chunk_size, key, iv):
	    des3 = DES3.new(key, DES3.MODE_CFB, iv)
	 
	    with open(in_filename, 'r') as in_file:
	        with open(out_filename, 'w') as out_file:
	            while True:
	                chunk = in_file.read(chunk_size)
	                if len(chunk) == 0:
	                    break
	                out_file.write(des3.decrypt(chunk))

#### DSA
#### Digital Signature Example
from Crypto.Random import random
from Crypto.PublicKey import DSA
from Crypto.Hash import SHA

message = "Hello"
key = DSA.generate(1025)
h = SHA.new(message).digest()
k = random.StrongRandom().randint(1,key.q-1)
sig = key.sign(h,k)
 ...
if key.verify(h,sig):
	print "OK"
else:
print "Incorrect signature" 
