import random
import hashlib
import requests

# 替换为你的百度翻译 appid
appid = '2022xxxxxx'

# 填写你的百度翻译API密钥
secretKey = '7Bnxxxxxxxx'  

# 要翻译的文本
translate_text = 'Hello World'

# 随机数
salt = random.randint(32768, 65536)

# 签名，拼接成字符串后，再进行md5加密
sign = appid + translate_text + str(salt) + secretKey
sign = hashlib.md5(sign.encode()).hexdigest()

# 百度翻译 API 地址
url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'

# 发送请求
response = requests.get(url, params={
    'q': translate_text,
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