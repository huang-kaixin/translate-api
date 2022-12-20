import pyperclip
import random
import hashlib
import requests
import time

# 请替换为你的百度翻译 appid
appid = '2022xxxxxxxx'

# 填写你的百度翻译API密钥
secretKey = '7Bnxxxxxxx'  

# 初始化上一次的剪贴板内容
last_clipboard_content = ''

while True:
    # 获取当前剪贴板内容
    clipboard_content = pyperclip.paste()
    
    # 如果剪贴板内容发生了变化
    if clipboard_content != last_clipboard_content:
        # 更新上一次的剪贴板内容
        last_clipboard_content = clipboard_content
        
        # 随机数
        salt = random.randint(32768, 65536)

        # 签名
        sign = appid + clipboard_content + str(salt) + secretKey
        sign = hashlib.md5(sign.encode()).hexdigest()

        # 百度翻译 API 地址
        url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'

        try:
            # 发送请求
            response = requests.get(url, params={
                'q': clipboard_content,
                'from': 'en', # auto
                'to': 'zh',
                'appid': appid,
                'salt': salt,
                'sign': sign
            })

            # 解析响应
            result = response.json()    
            # 输出翻译结果
            print(result['trans_result'][0]['dst'])
        except:
            print('发生了错误，无法获取翻译结果')
    # 休眠 1 秒
    time.sleep(1)