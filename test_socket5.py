# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:      test_socks
# Date:      2020/4/14
__Author__ = 'Negoo_wen'
#-------------------------------------------------------------------------------
import socket
import socks
socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 10792)
socket.socket = socks.socksocket


import requests

def main():
    url = 'https://newsapi.org'
    html = requests.get(url).text
    print(html)


if __name__ == '__main__':
    main()

