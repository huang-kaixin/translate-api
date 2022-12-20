# 1 获取百度翻译 API
首先，我们需要使用百度翻译 API 进行翻译需要注册百度翻译开放平台账号并获取 API 密钥，可以在此网站中注册并获取 API 密钥：https://api.fanyi.baidu.com/
[百度翻译API申请教程](https://blog.csdn.net/qq_42964728/article/details/125995316?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522167120247816782425159601%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=167120247816782425159601&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~pc_rank_34-1-125995316-null-null.142^v68^pc_new_rank,201^v4^add_ask,213^v2^t3_control2&utm_term=%E4%BD%BF%E7%94%A8%20Python%20%E7%9A%84%20requests%20%E5%BA%93%E6%9D%A5%E8%B0%83%E7%94%A8%E7%99%BE%E5%BA%A6%E7%BF%BB%E8%AF%91%20API&spm=1018.2226.3001.4187)
在获取了 API 密钥之后，我们可以使用 Python 的 requests 库来调用百度翻译 API：
```bash
pip install requests
```
# 2 先简单实现调用百度翻译并打印翻译结果
在调用百度翻译 API 时，我们需要提供以下参数：
- q：要翻译的文本
- from：需要翻译的源语言，例如：en（英文），zh（中文），auto（自动）
- to：需要转换成的语言
- appid：申请成为开发者后生成的appid，在在控制台中查看
- salt：随机数
- sign：生成的签名（appid+q+salt+密钥 的MD5值）

其中，salt 和 sign 是用来防止 API 被滥用的参数。示例代码：[translate.py](translate.py)

运行效果：
![](https://img-blog.csdnimg.cn/122b47c1ba484e109110290f1a281e0b.png#pic_center)

# 3 实现复制即翻译功能
## 3.1 翻译剪贴板内容并在终端输出
这一小节实现的功能：当发生复制待翻译文本的操作后，调用API进行翻译，将翻译结果显示在终端

示例代码：[copy_translate.py](copy_translate.py)

注意：上面代码要在终端运行，结果如下：
![](https://img-blog.csdnimg.cn/7e7599687c6c40a0ae743d4b3aaaa3d9.png#pic_center)

## 3.2 翻译剪贴板内容并在屏幕输出
这一小节我们调用百度翻译API实现以下功能：
1. 当发生复制操作时，获取剪贴板的待翻译文本，翻译为中文并将翻译结果显示在屏幕上；
2. 只有当再次发生复制操作，即剪贴板内容发生变化时，再次触发第一步的翻译并显示
3. 当剪贴板内容没有发生变化时，不执行翻译和显示操作，继续监视剪贴板内容是否发生改变，等待下一次复制操作

示例代码：[copy_translator.py](copy_translator.py)

![在这里插入图片描述](https://img-blog.csdnimg.cn/d970e74ad75040c0a099ff0e6fb163cf.png#pic_center)

- 这里发现了一个问题，复制的待翻译文本必须没有换行，否则翻译结果总是只能翻译一行，不知道是百度翻译API的问题还是我的代码问题，希望有大佬帮我解惑！

# 4 设计一个简单的翻译器
1. 在 Tkinter 窗口中添加一个文本输入框，用于输入要翻译的英文。
2. 在 Tkinter 窗口中添加一个按钮，点击按钮时调用百度翻译 API 进行翻译。
3. 在 Tkinter 窗口中添加一个文本框，用于显示翻译结果。 

在下面代码中，我们在 Tkinter 窗口中添加了一个文本输入框，一个按钮和一个文本框。点击按钮时，会调用百度翻译 API 进行翻译，并将翻译结果显示在文本框中。用户可以多次输入要翻译的英文，并点击按钮进行翻译，翻译结果会不断更新。

示例代码：[translator.py](translator.py)

运行结果如下：
![在这里插入图片描述](https://img-blog.csdnimg.cn/cabb07dbab204439af5cc54df04b2387.png#pic_center)

欢迎star :star:, 感谢支持！
