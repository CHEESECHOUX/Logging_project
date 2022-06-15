import requests
from random import random
from concurrent.futures import ThreadPoolExecutor

def post_url(args):
    return requests.post(args[0], data=args[1])

for i in range(10):
    form_data = {"ikria":random()}
    list_of_urls = [("https://ghcrol2iwf.execute-api.ap-northeast-2.amazonaws.com/default/logs-3",form_data)]*1000

    with ThreadPoolExecutor(max_workers=20) as pool:
        response_list = list(pool.map(post_url,list_of_urls))

    for response in response_list:
        print(response)

    print(f"{(i+1)*1000}번 성공")
