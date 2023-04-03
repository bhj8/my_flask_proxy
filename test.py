from my_crypt import decrypt_message, encrypt_message
import requests
import Globals
import json

# 请替换为您的服务器地址和端口号
# http://localhost:端口号/YXnkJqAD14DPG4
url = Globals.url #聊天接口
m_url = Globals.m_url #审核接口
# 这是gptapi的参数示例，您可以根据需要修改参数,自行构造参数
params = {
    "model": "gpt-3.5-turbo",
    "presence_penalty": 0,
    "top_p": 0.2, 
    "temperature": 0.5,
    "frequency_penalty": 0.5,
    "messages": [
        {"role": "system", "content": "you are a translator."},
        {"role": "user", "content": "Please translate the content I send you into English."},
        {"role": "assistant", "content": "yes"},
        {"role": "user", "content": "Translate the following Chinese text to English: "},
    ]
}
params_m = {"input":"需要被审核的内容"}



# 这是你发给我中转服务器的data，我们之间所有的通信都是对称加密的
message_data = encrypt_message(json.dumps(params),Globals.MY_PROXY_AES_KEY)
data = {
    "message":message_data 
}
message_data_m = encrypt_message(json.dumps(params_m),Globals.MY_PROXY_AES_KEY)
data_m = {"message":message_data_m}




headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

def get_response_chat():
    response = requests.post(url, data=data, headers=headers)

    if response.status_code == 200:
        json_response = json.loads(response.text)
        encrypted_message = json_response['message']
        reslut = decrypt_message(encrypted_message, Globals.MY_PROXY_AES_KEY)#解密后已经是一个字典了
        #我会把调取openai的结果，原样返回给你。你需要自行从包中提取自己需要的东西（触发异常时，则是意外信息）
        
        #假如你只要返回的聊天文本
        #reslut = reslut.choices[0].message.content.strip()
        print("解密后的消息：", reslut)
    else:
        print(f"请求失败，状态码：{response.status_code}")

def get_response_m():
    response = requests.post(m_url, data=data_m, headers=headers)

    if response.status_code == 200:
        json_response = json.loads(response.text)
        encrypted_message = json_response['message']
        reslut = decrypt_message(encrypted_message, Globals.MY_PROXY_AES_KEY)#解密后已经是一个字典了
        #我会把调取openai的结果，原样返回给你。你需要自行从包中提取自己需要的东西（触发异常时，则是意外信息）
        
        #假如你只要返回的聊天文本
        #reslut = reslut.choices[0].message.content.strip()
        print("解密后的消息：", reslut)
    else:
        print(f"请求失败，状态码：{response.status_code}")
    
        
    
if __name__ == "__main__":
    get_response_chat()
    get_response_m()


