# 自用

import requests, os, argparse

headers = {
    "Cache-Control": "max-age=0",
    "Sec-Ch-Ua": "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Microsoft Edge\";v=\"116\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "If-Modified-Since": "Thu, 07 Sep 2023 06:31:39 GMT"
}

urls = []

def dingding(url, i):
    r = requests.Session()
    url = "https://dtliving-bj.dingtalk.com/live_hp/" + str(url)

    file = r.get(url=url, headers=headers).content
    with open("./08网警大比武/" + str(i+1) + ".ts", 'wb') as f:
        f.write(file)

text = ""
with open('video.txt', 'rb') as f:
    text = f.read()

text = text.decode('utf-8').split('\r\n')
for url in range(5, len(text), 2):
    urls.append(str(text[url]))

for i in range(len(urls)):
    dingding(urls[i], (i))

# \?auth_key=(.*)

# ffmpeg -i video.txt -vcodec copy -acodec copy -absf aac_adtstoasc output.mp4

# copy /b *.ts example.mp4