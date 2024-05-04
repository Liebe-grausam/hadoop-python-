---
title: 玩了AI
date: 2024-03-20 21:41:55
tags: groq
---
第一次跑一个ai的实例独立跑通了！之前没跑通是因为环境变量的问题，设置了环境变量就好了！（事实证明不能忽视控制台的警告哇

本地部署完成！（算是？

成就：获得免费API（记得运行的时候要全局翻墙

![API keys](../img/玩了AI/API_keys.png)
![运行示例](../img/玩了AI/运行示例.png)
源码
```python
from groq import Groq

client = Groq(api_key="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")

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "why is the sea blue?",
        }
    ],
    model="gemma-7b-it",
)

print(chat_completion.choices[0].message.content)
```