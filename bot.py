# save this as app.py
import os
import json
from my_crypt import decrypt_message, encrypt_message
from api_openai import *
from flask import Flask, make_response, render_template, request, url_for, jsonify
from markupsafe import escape
import logging
import asyncio

MY_PROXY_AES_KEY = Globals.MY_PROXY_AES_KEY
loop = asyncio.get_event_loop()
asyncio.set_event_loop(loop)




# 创建一个 logger
logger = logging.getLogger('myapp')
logger.setLevel(logging.DEBUG)

# 创建一个控制台日志处理器 StreamHandler 并设置其日志级别
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

# 创建一个文件日志处理器 FileHandler 并设置其日志级别
file_handler = logging.FileHandler('myapp.log')
file_handler.setLevel(logging.DEBUG)

# 创建日志格式化器
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 为控制台日志处理器和文件日志处理器分别设置格式化器
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# 为 logger 添加控制台日志处理器和文件日志处理器
logger.addHandler(console_handler)
logger.addHandler(file_handler)


app = Flask(__name__)


@app.route('/YXnkJqAD14DPG4', methods=['GET', 'POST'])
def getpay():
    encrypted_message = request.form.get('message')
    if encrypted_message:
        decrypted_message = decrypt_message(encrypted_message, MY_PROXY_AES_KEY)
        if decrypted_message:
            result =  asyncio.run(get_response(decrypted_message))
            message = json.dumps(result)
            encrypted_message = encrypt_message(message,MY_PROXY_AES_KEY)    
            logger.debug(f"encrypted_message: {encrypted_message}")        
            return jsonify({'code': 200, 'message': encrypted_message})

    print(f"bad pay info")
    logger.warning(f"bad pay info")
    return make_response("", 400)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return jsonify({"error": "Not Found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)