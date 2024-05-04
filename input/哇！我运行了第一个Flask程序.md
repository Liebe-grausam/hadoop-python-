---
title: 哇！我运行了第一个Flask程序
date: 2024-04-25 16:37:42
tags: dialect
---
python的程序已经差不多搭建完成了！（今天录入了全部的音素 方言词典开发计划进入下一阶段，即在web网页中嵌入python代码

发现了flask这个宝藏应用程序
```python
# Filename : example.py
# Copyright : 2020 By Nhooo
# Author by : www.cainiaojc.com
# Date : 2020-08-08
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World'
if __name__ == '__main__':
    app.run()
```
只要把这个代码保存到hello.py中并在终端中运行命令
```bash
python hello.py
```
就可以在弹出的本地端口中发现网页上已经展示了一行“helloworld”~