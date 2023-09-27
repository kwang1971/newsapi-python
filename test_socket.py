#!/usr/bin/python
# -*- coding: UTF-8 -*-



import time
import socket
import socks

starttime = time.time()

SOCKS5_PROXY_HOST = '127.0.0.1'		 # socks 代理IP地址
SOCKS5_PROXY_PORT = 10792          # socks 代理本地端口
default_socket = socket.socket
socks.set_default_proxy(socks.SOCKS5, SOCKS5_PROXY_HOST, SOCKS5_PROXY_PORT)
socket.socket = socks.socksocket

import requests


head1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) Gecko/20100101 Firefox/62.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2"
}

session = requests.session()
session.keep_alive = False

resp=session.get("https://newsapi_org",headers=head1,timeout=5)
#resp.encoding = 'gb2312'
html_source=resp.text
resp.close()

# if html_source: 
#     with open('ssssss.htm', mode='a+', encoding='gb2312') as file:
#         file.write(html_source)
#     print('ok')
# else: 
#     print('fail')


endtime = time.time()
print(endtime-starttime)




