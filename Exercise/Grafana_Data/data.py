import random
import time
from multiprocessing import Pool

from Exercise.Grafana_Data.Mysql import Mysql_handle

if __name__ == '__main__':
    Data_list = []
    while True:
        hosts = ['host1', 'host2', 'host3']
        value = random.randrange(0, 100)
        metric = random.choice(hosts)
        Data_list.append([(value,metric)])
        if len(Data_list)== 10:
            break
    print( Data_list)
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    with Pool(2) as p:
        p.map(Mysql_handle,Data_list)

