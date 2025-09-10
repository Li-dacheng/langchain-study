import os
from openai import OpenAI


client = OpenAI(

    base_url="https://ark-cn-beijing.bytedance.net/api/v3",

    api_key=os.environ.get("ARK_API_KEY"),
)

print("----- standard request -----")
completion = client.chat.completions.create(

    model="ep-20250904195315-brszv",
    messages=[
        {"role": "system", "content": "你是人工智能助手"},
        {"role": "user", "content": "你好"},
    ],
)
print(completion.choices[0].message.content)

print("----- streaming request -----")
stream = client.chat.completions.create(

    model="ep-20250904195315-brszv",
    messages=[
        {"role": "system", "content": "你是人工智能助手"},
        {"role": "user", "content": "你好"},
    ],

    stream=True,
)
for chunk in stream:
    if not chunk.choices:
        continue
    print(chunk.choices[0].delta.content, end="")
print()