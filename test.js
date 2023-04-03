const axios = require("axios");
const crypto = require("crypto");
const { encrypt, decrypt } = require("./my_crypt"); // Import your custom encrypt and decrypt functions from 'my_crypt'

const Globals = {
  url: "YOUR_SERVER_URL", // Replace with your server URL and port number
  m_url: "YOUR_SERVER_M_URL", // Replace with your m_server URL and port number
  MY_PROXY_AES_KEY: "YOUR_AES_KEY", // Replace with your AES key
};

const params = {
  model: "gpt-3.5-turbo",
  presence_penalty: 0,
  top_p: 0.2,
  temperature: 0.5,
  frequency_penalty: 0.5,
  messages: [
    { role: "system", content: "you are a translator." },
    { role: "user", content: "Please translate the content I send you into English." },
    { role: "assistant", content: "yes" },
    { role: "user", content: "Translate the following Chinese text to English: " },
  ],
};

const params_m = { input: "需要被审核的内容" };

const messageData = encrypt(JSON.stringify(params), Globals.MY_PROXY_AES_KEY);
const data = { message: messageData };

const messageData_m = encrypt(JSON.stringify(params_m), Globals.MY_PROXY_AES_KEY);
const data_m = { message: messageData_m };

const headers = { "Content-Type": "application/x-www-form-urlencoded" };

async function getResponseChat() {
  try {
    const response = await axios.post(Globals.url, data, { headers });
    if (response.status === 200) {
      const jsonResponse = response.data;
      const encryptedMessage = jsonResponse.message;
      const result = decrypt(encryptedMessage, Globals.MY_PROXY_AES_KEY);
      console.log("Decrypted message:", result);
    } else {
      console.log(`Request failed, status code: ${response.status}`);
    }
  } catch (error) {
    console.error(`Error: ${error.message}`);
  }
}

async function getResponseM() {
  try {
    const response = await axios.post(Globals.m_url, data_m, { headers });
    if (response.status === 200) {
      const jsonResponse = response.data;
      const encryptedMessage = jsonResponse.message;
      const result = decrypt(encryptedMessage, Globals.MY_PROXY_AES_KEY);
      console.log("Decrypted message:", result);
    } else {
      console.log(`Request failed, status code: ${response.status}`);
    }
  } catch (error) {
    console.error(`Error: ${error.message}`);
  }
}

(async () => {
  await getResponseChat();
  await getResponseM();
})();
