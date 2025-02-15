import datetime
import json
import requests
from utils.load_conf import load_conf

conf = load_conf()
source_platform = conf['source_platform']
for target_platform in source_platform:
    print(f"target_platform: {target_platform}")
    url = f'https://api.itapi.cn/api/hotnews/{target_platform}?key={conf['key']}'
    response = requests.request("GET", url)
    # 获取当前时间，格式为 YYYYMMDDHHMMSS
    current_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    # 构建文件名
    filename = f'./results/{target_platform}_{current_time}.json'
    # 将数据写入文件
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(response.json(), file, ensure_ascii=False, indent=4)
    print(f"[{current_time}] [{target_platform}] 热点数据已存入文件：{filename}")