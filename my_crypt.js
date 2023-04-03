const crypto = require('crypto');
const base64 = require('base64-js');

function encryptMessage(messageJson, key) {
  const keyBytes = base64.toByteArray(key);
  const cipher = crypto.createCipheriv('aes-256-ecb', keyBytes, null);
  const messageBuffer = Buffer.from(messageJson, 'utf-8');
  const encrypted = Buffer.concat([cipher.update(messageBuffer), cipher.final()]);
  return base64.fromByteArray(encrypted);
}

function decryptMessage(encryptedMessageBase64, key) {
  const keyBytes = base64.toByteArray(key);
  const encryptedMessageBytes = base64.toByteArray(encryptedMessageBase64);
  try {
    const decipher = crypto.createDecipheriv('aes-256-ecb', keyBytes, null);
    const decrypted = Buffer.concat([decipher.update(encryptedMessageBytes), decipher.final()]);
    return JSON.parse(decrypted.toString('utf-8'));
  } catch (e) {
    console.debug(`Decryption failed, error: ${e}`);
    return null;
  }
}

function generateKey() {
  const keyBytes = crypto.randomBytes(32);
  return base64.fromByteArray(keyBytes);
}
