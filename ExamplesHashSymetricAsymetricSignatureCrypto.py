# Examples pyCrypto
# Taken from : https://github.com/dlitz/pycrypto/blob/master/lib/Crypto/PublicKey/DSA.py
# http://www.laurentluce.com/posts/python-and-cryptography-with-pycrypto/
# Different testing Crypto Algorithms
# Modified by G. Isaza Abrl 2016. UCaldas

# Hashing with SHA
>>> from Crypto.Hash import SHA256
>>> SHA256.new('abc').hexdigest()
'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'

1	from Crypto.Hash import SHA256
2	def check_password(clear_password, password_hash):
3	    return SHA256.new(clear_password).hexdigest() == password_hash

# Symetric DES
1	>>> from Crypto.Cipher import DES
2	>>> des = DES.new('01234567', DES.MODE_ECB)
3	>>> text = 'abcdefgh'
4	>>> cipher_text = des.encrypt(text)
5	>>> cipher_text
6	'\xec\xc2\x9e\xd9] a\xd0'
7	>>> des.decrypt(cipher_text)
8	'abcdefgh'

# Symetric DES with CFB+IV
01	>>> from Crypto.Cipher import DES
02	>>> from Crypto import Random
03	>>> iv = Random.get_random_bytes(8)
04	>>> des1 = DES.new('01234567', DES.MODE_CFB, iv)
05	>>> des2 = DES.new('01234567', DES.MODE_CFB, iv)
06	>>> text = 'abcdefghijklmnop'
07	>>> cipher_text = des1.encrypt(text)
08	>>> cipher_text
09	"?\\\x8e\x86\xeb\xab\x8b\x97'\xa1W\xde\x89!\xc3d"
10	>>> des2.decrypt(cipher_text)
11	'abcdefghijklmnop'

# Stream Cipher Rc4
1	>>> from Crypto.Cipher import ARC4
2	>>> obj1 = ARC4.new('01234567')
3	>>> obj2 = ARC4.new('01234567')
4	>>> text = 'abcdefghijklmnop'
5	>>> cipher_text = obj1.encrypt(text)
6	>>> cipher_text
7	'\xf0\xb7\x90{#ABXY9\xd06\x9f\xc0\x8c '
8	>>> obj2.decrypt(cipher_text)
9	'abcdefghijklmnop'

# Public RSA with 1024 key
1	>>> from Crypto.PublicKey import RSA
2	>>> from Crypto import Random
3	>>> random_generator = Random.new().read
4	>>> key = RSA.generate(1024, random_generator)
5	>>> key
6	<_RSAobj @0x7f60cf1b57e8 n(1024),e,d,p,q,u,private>
1	>>> key.can_encrypt()
2	True
3	>>> key.can_sign()
4	True
5	>>> key.has_private()
6	True
1	>>> public_key = key.publickey()
2	>>> enc_data = public_key.encrypt('abcdefgh', 32)
3	>>> enc_data
4	#('\x11\x86\x8b\xfa\x82\xdf\xe3sN ~@\xdbP\x85
1	>>> 2   >>>> public_key = key.publickey()key.decrypt(enc_data)
2	'abcdefgh'

# Signature Sign and Verify Long Process
# First HASH with SHA256 then RSA with private key
1	>>> from Crypto.Hash import SHA256
2	>>> from Crypto.PublicKey import RSA
3	>>> from Crypto import Random
3   >>> random_generator = Random.new().read
4	>>> key = RSA.generate(1024, random_generator)
5	>>> text = 'abcdefgh'
6	>>> hash = SHA256.new(text).digest()
7	>>> hash
8	'\x9cV\xccQ\xb3t\xc3\xba\x18\x92\x10\xd5\xb6\xd4\xbfWy\r5\x1c\x96\xc4|\x02\x19\x0e\xcf\x1eC\x065\xab'
9	>>> signature = key.sign(hash, '')
1	>>> text = 'abcdefgh'
2	>>> hash = SHA256.new(text).digest()
2   >>>> public_key = key.publickey()
3	>>> public_key.verify(hash, signature)
4	True


#Crypt and Decrypt File
01	import os
02	from Crypto.Cipher import DES3
03	 
04	def encrypt_file(in_filename, out_filename, chunk_size, key, iv):
05	    des3 = DES3.new(key, DES3.MODE_CFB, iv)
06	 
07	    with open(in_filename, 'r') as in_file:
08	        with open(out_filename, 'w') as out_file:
09	            while True:
10	                chunk = in_file.read(chunk_size)
11	                if len(chunk) == 0:
12	                    break
13	                elif len(chunk) % 16 != 0:
14	                    chunk += ' ' * (16 - len(chunk) % 16)
15	                out_file.write(des3.encrypt(chunk))
16	 
17	def decrypt_file(in_filename, out_filename, chunk_size, key, iv):
18	    des3 = DES3.new(key, DES3.MODE_CFB, iv)
19	 
20	    with open(in_filename, 'r') as in_file:
21	        with open(out_filename, 'w') as out_file:
22	            while True:
23	                chunk = in_file.read(chunk_size)
24	                if len(chunk) == 0:
25	                    break
26	                out_file.write(des3.decrypt(chunk))

#### DSA
#### Digital Signature Example
>>> from Crypto.Random import random
>>> from Crypto.PublicKey import DSA
>>> from Crypto.Hash import SHA
>>>
>>> message = "Hello"
>>> key = DSA.generate(1025)
>>> h = SHA.new(message).digest()
>>> k = random.StrongRandom().randint(1,key.q-1)
>>> sig = key.sign(h,k)
>>> ...
>>> if key.verify(h,sig):
>>> print "OK"
>>> else:
>>> print "Incorrect signature" 
