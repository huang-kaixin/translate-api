import random
import hashlib
import requests
import tkinter as tk

# 创建窗口
root = tk.Tk()
root.title('翻译结果')

# 创建文本输入框，用于输入要翻译的英文
text_input = tk.Entry(root, width=60)
text_input.pack()

# 创建按钮，点击按钮时调用百度翻译 API 进行翻译
def translate():
  # 读取文本输入框中的文本
  translate_text = text_input.get()

  # 调用百度翻译 API 进行翻译
  # 替换为你的百度翻译 appid
  appid = '2022xxxxx'

  # 填写你的百度翻译API密钥
  secretKey = '7Bxxxxxxx'  

  # 随机数
  salt = random.randint(32768, 65536)

  # 签名
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

  # 将翻译结果显示在文本框中
  text_output.delete(0.0, tk.END)
  text_output.insert(tk.END, result['trans_result'][0]['dst'])

button = tk.Button(root, text='翻译', command=translate)
button.pack()

# 创建文本框，用于显示翻译结果
text_output = tk.Text(root)
text_output.pack()

# 运行主循环
root.mainloop()