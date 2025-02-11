import datetime
import json
import requests
from utils.load_conf import load_conf

conf = load_conf()
url = f'https://api.itapi.cn/api/hotnews/xiaohongshu?key={conf['key']}'

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

# 获取当前时间，格式为 YYYYMMDDHHMMSS
current_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

# 构建文件名
filename = f'./results/xiaohongshu_{current_time}.json'

# 将数据写入文件
with open(filename, 'w', encoding='utf-8') as file:
    json.dump(response.json(), file, ensure_ascii=False, indent=4)

print(f"数据已存入文件：{filename}")