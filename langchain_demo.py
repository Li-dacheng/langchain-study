import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# 加载 .env 文件中的环境变量
load_dotenv()

model = ChatOpenAI(
    base_url="https://ark-cn-beijing.bytedance.net/api/v3",
    api_key=os.environ.get("ARK_API_KEY"),
    model="ep-20250904195315-brszv",
)

messages = "解释人工智能"
res = model.invoke(messages)

print(res)


# 如果希望接入提示词的能力，可以message入参做一些修改，SystemMessage就是系统提示词
from langchain_core.messages import HumanMessage, SystemMessage
messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="解释人工智能"),
]