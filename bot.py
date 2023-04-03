# save this as app.py
import os
import json
from my_crypt import decrypt_message, encrypt_message
from api_openai import *
from flask import Flask, make_response, render_template, request, url_for, jsonify
from markupsafe import escape
from dotenv import load_dotenv


load_dotenv()
MY_PROXY_AES_KEY = os.getenv("MY_PROXY_AES_KEY")

app = Flask(__name__)


@app.route('/YXnkJqAD14DPG4', methods=['GET', 'POST'])
async def getpay():
    encrypted_message = request.form.get('message')
    if encrypted_message:
        decrypted_message = decrypt_message(encrypted_message, MY_PROXY_AES_KEY)
        if decrypted_message:
            dic = json.loads(decrypted_message)
            result =  await get_response(dic)
            
            return make_response("", 200)

    print(f"bad pay info")
    return make_response("", 400)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return jsonify({"error": "Not Found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)