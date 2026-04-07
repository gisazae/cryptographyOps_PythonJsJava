var CryptoJS = require("crypto-js");
 
// Encrypt
var ciphertext = CryptoJS.AES.encrypt('Prueba de Mensaje', 'secret key 123').toString();
 
// Decrypt
var bytes  = CryptoJS.AES.decrypt(ciphertext, 'secret key 123');
var originalText = bytes.toString(CryptoJS.enc.Utf8);
 
console.log(originalText);
