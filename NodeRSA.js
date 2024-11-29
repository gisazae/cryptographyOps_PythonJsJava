const crypto = require('crypto');

// Generar par de claves RSA
function generateKeyPair() {
  const { publicKey, privateKey } = crypto.generateKeyPairSync('rsa', {
    modulusLength: 2048, // Longitud de la clave (en bits)
    publicKeyEncoding: {
      type: 'spki', // Formato de clave pública
      format: 'pem', // Codificación PEM
    },
    privateKeyEncoding: {
      type: 'pkcs8', // Formato de clave privada
      format: 'pem', // Codificación PEM
    },
  });

  return { publicKey, privateKey };
}

// Función para cifrar un mensaje con la clave pública
function encryptWithPublicKey(publicKey, message) {
  const encrypted = crypto.publicEncrypt(
    {
      key: publicKey,
      padding: crypto.constants.RSA_PKCS1_OAEP_PADDING,
      oaepHash: 'sha256',
    },
    Buffer.from(message)
  );

  return encrypted.toString('base64'); // Devuelve el texto cifrado en base64
}

// Función para descifrar un mensaje con la clave privada
function decryptWithPrivateKey(privateKey, encryptedMessage) {
  const decrypted = crypto.privateDecrypt(
    {
      key: privateKey,
      padding: crypto.constants.RSA_PKCS1_OAEP_PADDING,
      oaepHash: 'sha256',
    },
    Buffer.from(encryptedMessage, 'base64')
  );

  return decrypted.toString(); // Devuelve el mensaje descifrado
}

// Ejemplo de uso
(function main() {
  // Generar las claves
  const { publicKey, privateKey } = generateKeyPair();

  console.log('Clave pública:\n', publicKey);
  console.log('Clave privada:\n', privateKey);

  // Mensaje a cifrar
  const message = "Este es un mensaje secreto con RSA";
  console.log('Mensaje original:', message);

  // Cifrar el mensaje con la clave pública
  const encryptedMessage = encryptWithPublicKey(publicKey, message);
  console.log('Mensaje cifrado:', encryptedMessage);

  // Descifrar el mensaje con la clave privada
  const decryptedMessage = decryptWithPrivateKey(privateKey, encryptedMessage);
  console.log('Mensaje descifrado:', decryptedMessage);
})();

