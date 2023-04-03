import asyncio
import os

import openai
from dotenv import load_dotenv


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

async def get_moderation(imessage: str):#True 有不当内容
  moderation = await openai.Moderation.acreate(
  input=imessage,
  )
  return moderation.results[0].flagged


async def get_response(dic:dict):
    try :
        completions = await openai.ChatCompletion.acreate(
            **dic
        )
        return completions
    except Exception as e:
        print(e)
        return str(e)
    
#   return completions.choices[0].message.content.strip()


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


if __name__ == "__main__":
  openai.proxy=  {
  "http": "http://127.0.0.1:7890",
  "https": "http://127.0.0.1:7890",
}
  # print(asyncio.run(get_translation(["一个美少女,jk,金色头发,带着眼镜"])))
  print(asyncio.run(get_response(params)))
  # print(asyncio.run(get_moderation(["审核能力测试"])))
# 处理生成的文本输出
#print(message)


