import logging
import os
import sys

import dotenv

logger = logging.getLogger('myapp')
dotenv.load_dotenv()

def get_env_variable(var_name):
    value = os.getenv(var_name)
    if not value or value == "":
        logger.error("错误：又尼玛的狗日的没设置环境变量是不是？？？？   %r",var_name)
        exit()
    return value

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MY_PROXY_AES_KEY = os.getenv("MY_PROXY_AES_KEY")
url = os.getenv("url")
m_url= os.getenv("m_url")
