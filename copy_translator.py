import pyperclip
import random
import hashlib
import requests
from tkinter import Tk, Label, StringVar

# 请替换为您的百度翻译 appid
appid = '2022xxxxxx'

# 填写你的百度翻译API密钥
secretKey = '7Bnxxxxxxxx'  

# 初始化上一次的剪贴板内容
last_clipboard_content = ''

# 创建窗口
root = Tk()
root.title('熊哩翻译器')

# 创建字符串变量
result_str = StringVar()

# 创建标签
label = Label(root, textvariable=result_str, font=("Arial", 14))
# 使用 config() 函数来设置文本框的宽度和高度
label.config(width=30, height=10)
label.pack()

def translate():
    global last_clipboard_content
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

        # 更新字符串变量的值
        result_str.set(result['trans_result'][0]['dst'])
    
    # 延迟一秒后再次执行 translate 函数
    root.after(1000, translate)

# 开始循环
translate()

# 进入消息循环
root.mainloop()