#coding:utf-8
import requests

with open("link.txt", "r") as f:
    count = 1
    for line in f.readlines():
        imgUrl = line.strip('\n')  #去掉列表中每一个元素的换行符
        #imgUrl = 'https://res.qxueyou.com/img/2020/09/02/'+line
        image_name = str(count) + '.PNG'
        print(image_name,imgUrl)
        count+=1

        imgresponse = requests.get(imgUrl, stream=True)   #以流的方式打开
        image = imgresponse.content
        address="C:\\Users\Administrator\Desktop\PMP"+"\\"
        try:
            with open(address+image_name ,"wb") as jpg:
                jpg.write(image)
        except IOError:
            print("IO Error\n")
        finally:
            jpg.close


