import hashlib

def hash_password(password: str) -> str:
    """
    Genera un hash SHA-256 para la contraseña dada.
    """
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def validate_password(stored_hash: str, input_password: str) -> bool:
    """
    Valida una contraseña ingresada comparando su hash con el hash almacenado.
    
    Args:
    - stored_hash: Hash previamente almacenado de la contraseña.
    - input_password: Contraseña ingresada por el usuario.
    
    Returns:
    - True si las contraseñas coinciden, False en caso contrario.
    """
    input_hash = hash_password(input_password)
    return input_hash == stored_hash

# Ejemplo de uso:
if __name__ == "__main__":
    # Contraseña original
    original_password = "Testing1234"
    # Generar y almacenar el hash
    stored_hash = hash_password(original_password)
    print("Hash almacenado:", stored_hash)

    # Validar una contraseña ingresada
    input_password = input("Ingresa tu contraseña: ")
    if validate_password(stored_hash, input_password):
        print("Contraseña válida.")
    else:
        print("Contraseña incorrecta.")
