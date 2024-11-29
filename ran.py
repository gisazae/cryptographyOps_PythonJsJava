from cryptography.fernet import Fernet
import os

def generate_key():
    """Genera y guarda una clave en un archivo."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    """Carga la clave desde el archivo."""
    return open("secret.key", "rb").read()

def encrypt_file(file_path):
    """Cifra el contenido de un archivo."""
    key = load_key()
    fernet = Fernet(key)

    with open(file_path, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(file_path + ".encrypted", "wb") as encrypted_file:
        encrypted_file.write(encrypted)

    print(f"Archivo cifrado como: {file_path}.encrypted")

def decrypt_file(encrypted_file_path):
    """Descifra el contenido de un archivo cifrado."""
    key = load_key()
    fernet = Fernet(key)

    with open(encrypted_file_path, "rb") as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(encrypted_file_path.replace(".encrypted", ".decrypted"), "wb") as decrypted_file:
        decrypted_file.write(decrypted)

    print(f"Archivo descifrado como: {encrypted_file_path.replace('.encrypted', '.decrypted')}")

def main():
    choice = input("¿Deseas (e)ncriptar o (d)esencriptar un archivo? (e/d): ")
    if choice.lower() == 'e':
        file_path = input("Introduce la ruta del archivo a cifrar: ")
        if os.path.isfile(file_path):
            if not os.path.exists("secret.key"):
                generate_key()
            encrypt_file(file_path)
        else:
            print("El archivo no existe. Por favor, verifica la ruta.")
    elif choice.lower() == 'd':
        encrypted_file_path = input("Introduce la ruta del archivo cifrado: ")
        if os.path.isfile(encrypted_file_path):
            decrypt_file(encrypted_file_path)
        else:
            print("El archivo cifrado no existe. Por favor, verifica la ruta.")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
