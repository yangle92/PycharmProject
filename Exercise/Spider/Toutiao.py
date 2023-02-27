#!/usr/bin/env python
import re
import requests
import time
import os
import sys
#from lxml import etree
count=0
while True:
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"
    }
    # 传递的非单个博客地址，而是博客列表

    art_url=[
        "https://www.toutiao.com/i6519813373746479624/",
        "https://www.toutiao.com/i6519455882323952131/",
        "https://www.toutiao.com/i6518637989927584259/",
        "https://www.toutiao.com/i6518600764204515844/",
        "https://www.toutiao.com/i6518250648989860356/"
    ]
    print(art_url)
    for i in art_url:
        print(i)
        html = requests.get(i, headers=headers).text
        time.sleep(3)
        print (html)
    count+=1
    print("#############第 %s 轮循环完毕##################"% (count))
    


