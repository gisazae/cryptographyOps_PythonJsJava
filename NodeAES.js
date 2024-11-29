const crypto = require('crypto');

// Función para cifrar
function encrypt(text, key, iv) {
  const cipher = crypto.createCipheriv('aes-256-cbc', Buffer.from(key), iv);
  let encrypted = cipher.update(text);
  encrypted = Buffer.concat([encrypted, cipher.final()]);
  return encrypted.toString('hex'); // Retorna el texto cifrado en formato hexadecimal
}

// Función para descifrar
function decrypt(encryptedText, key, iv) {
  const encryptedBuffer = Buffer.from(encryptedText, 'hex');
  const decipher = crypto.createDecipheriv('aes-256-cbc', Buffer.from(key), iv);
  let decrypted = decipher.update(encryptedBuffer);
  decrypted = Buffer.concat([decrypted, decipher.final()]);
  return decrypted.toString(); // Retorna el texto original
}

// Ejemplo de uso
(function main() {
  const secretKey = crypto.randomBytes(32); // Clave de 32 bytes (256 bits)
  const iv = crypto.randomBytes(16); // Vector de inicialización de 16 bytes

  console.log('Clave (key):', secretKey.toString('hex'));
  console.log('Vector de inicialización (iv):', iv.toString('hex'));

  const message = "Este es un mensaje secreto";
  console.log('Mensaje original:', message);

  // Cifrar el mensaje
  const encryptedMessage = encrypt(message, secretKey, iv);
  console.log('Mensaje cifrado:', encryptedMessage);

  // Descifrar el mensaje
  const decryptedMessage = decrypt(encryptedMessage, secretKey, iv);
  console.log('Mensaje descifrado:', decryptedMessage);
})();
