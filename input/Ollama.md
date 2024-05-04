---
title: Ollama
date: 2024-03-21 15:52:24
tags: Ollama
---
昨天加入了环境变量，之前困扰的ollama报错问题也解决了。
![运行环境](../img/ollama/运行环境.png)
![以流的形式运行实例](../img/ollama/以流的形式运行实例.png)
```python
import ollama
stream = ollama.chat(
    model='MyModel',
    messages=[{'role': 'user', 'content': 'Why is the sky blue?'}],
    stream=True,
)
for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)
```