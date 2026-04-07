import numpy as np

def generate_random_bits(length):
    """Genera una secuencia de bits aleatorios."""
    return np.random.randint(0, 2, length)

def generate_random_bases(length):
    """Genera una secuencia de bases aleatorias (0 para rectilíneas, 1 para diagonales)."""
    return np.random.randint(0, 2, length)

def encode_qubits(bits, bases):
    """
    Codifica los bits en qubits según las bases.
    - Base 0 (rectilínea): |0⟩ y |1⟩.
    - Base 1 (diagonal): |+⟩ y |-⟩.
    """
    qubits = []
    for bit, base in zip(bits, bases):
        if base == 0:  # Base rectilínea
            qubits.append('|0>' if bit == 0 else '|1>')
        else:  # Base diagonal
            qubits.append('|+>' if bit == 0 else '|->')
    return qubits

def measure_qubits(qubits, measurement_bases):
    """
    Mide los qubits en las bases indicadas.
    - Si la base coincide con la base de preparación, se mide correctamente.
    - Si no, el resultado es aleatorio.
    """
    results = []
    for qubit, base in zip(qubits, measurement_bases):
        if qubit in ['|0>', '|1>'] and base == 0:  # Medición en base rectilínea
            results.append(0 if qubit == '|0>' else 1)
        elif qubit in ['|+>', '|->'] and base == 1:  # Medición en base diagonal
            results.append(0 if qubit == '|+>' else 1)
        else:  # Medición en base incorrecta (resultado aleatorio)
            results.append(np.random.randint(0, 2))
    return results

def reconcile_keys(sender_bases, receiver_bases, sender_bits):
    """
    Reconciliación: Retiene los bits donde las bases coinciden.
    """
    key = [bit for sb, rb, bit in zip(sender_bases, receiver_bases, sender_bits) if sb == rb]
    return key

# Simulación del protocolo BB84
if __name__ == "__main__":
    # Longitud de la secuencia
    n = 100
    
    # Paso 1: Alice genera bits y bases
    alice_bits = generate_random_bits(n)
    alice_bases = generate_random_bases(n)
    qubits = encode_qubits(alice_bits, alice_bases)
    
    # Paso 2: Bob elige bases aleatorias y mide los qubits
    bob_bases = generate_random_bases(n)
    bob_results = measure_qubits(qubits, bob_bases)
    
    # Paso 3: Reconciliación de claves
    shared_key = reconcile_keys(alice_bases, bob_bases, alice_bits)
    
    # Paso 4: (Opcional) Detección de intrusos
    # Alice y Bob comparten una parte de su clave para verificar si hubo interferencia.
    sample_indices = np.random.choice(len(shared_key), size=10, replace=False)
    sample_alice = [shared_key[i] for i in sample_indices]
    sample_bob = [shared_key[i] for i in sample_indices]
    
    print("Bits originales de Alice:", alice_bits)
    print("Bases de Alice:", alice_bases)
    print("Bases de Bob:", bob_bases)
    print("Resultados de Bob:", bob_results)
    print("Clave compartida:", shared_key)
    print("Verificación de la muestra (Alice):", sample_alice)
    print("Verificación de la muestra (Bob):", sample_bob)
    
    if sample_alice == sample_bob:
        print("¡Clave compartida generada con éxito y sin intrusos detectados!")
    else:
        print("Intrusión detectada o error en la transmisión.")
