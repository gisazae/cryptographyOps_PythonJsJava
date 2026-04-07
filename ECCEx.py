from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

# Generar claves privadas de curvas elípticas para dos partes (simulación)
private_key_A = ec.generate_private_key(ec.SECP256R1())
private_key_B = ec.generate_private_key(ec.SECP256R1())

# Obtener claves públicas
public_key_A = private_key_A.public_key()
public_key_B = private_key_B.public_key()

# Derivar una clave compartida utilizando ECDH
shared_key_A = private_key_A.exchange(ec.ECDH(), public_key_B)
shared_key_B = private_key_B.exchange(ec.ECDH(), public_key_A)

# Verificar que ambas claves compartidas son iguales
assert shared_key_A == shared_key_B

# Derivar una clave simétrica a partir de la clave compartida
derived_key = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=None,
    info=b'handshake data'
).derive(shared_key_A)

print(f"Clave derivada: {derived_key.hex()}")

# Mensaje a cifrar
message = b"Este es un mensaje secreto con ECC."

# Generar un IV (vector de inicialización) para AES en modo CBC
iv = os.urandom(16)

# Cifrar el mensaje usando AES con la clave derivada
cipher = Cipher(algorithms.AES(derived_key), modes.CBC(iv))
encryptor = cipher.encryptor()
# El mensaje debe tener un tamaño múltiplo de 16, por lo que lo rellenamos
padded_message = message + b' ' * (16 - len(message) % 16)
ciphertext = encryptor.update(padded_message) + encryptor.finalize()

print(f"\nMensaje cifrado: {ciphertext.hex()}")

# Descifrar el mensaje usando la misma clave derivada
decryptor = cipher.decryptor()
decrypted_padded_message = decryptor.update(ciphertext) + decryptor.finalize()

# Eliminar el relleno
decrypted_message = decrypted_padded_message.rstrip(b' ')

print(f"\nMensaje descifrado: {decrypted_message.decode()}")
