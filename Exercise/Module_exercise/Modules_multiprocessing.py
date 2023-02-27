#coding:utf-8

from multiprocessing import Pool
import time
def ssh (ip):
    print ("login in %s "%ip)
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    time.sleep(10)
if __name__ == '__main__':
    with Pool(50) as p:
        p.map(ssh,["192.168.1."+ str(i) for i in range(100)])

