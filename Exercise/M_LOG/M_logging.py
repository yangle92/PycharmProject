import logging

'''
1)输出者
2）输出位置 handles （句柄）
3）输出者与位置的绑定 formater
4)级别控制：打印者规定打印机级别，输出位置（句柄）再可以二次限定，级别>=打印者级别
'''

# logging.critical("critical msg ....")

#outer
log1 = logging.getLogger("Tony")
log1.setLevel(level = logging.INFO)

log2 = logging.getLogger("Sunny")
log2.setLevel(level = logging.DEBUG)

#handles
ha_a = logging.FileHandler('./log/a.log',encoding='utf-8')
ha_b = logging.FileHandler('./log/b.log',encoding='utf-8')
ha_cmd = logging.StreamHandler()

log1.addHandler(ha_a)
log2.addHandler(ha_b)
log2.addHandler(ha_cmd)
#formater
fmt1 = logging.Formatter ('%(asctime)s - %(name)s - %(msg)s')
fmt2 = logging.Formatter ('%(asctime)s - %(name)s - %(msg)s')

ha_a.setFormatter(fmt1)
ha_b.setFormatter(fmt1)
ha_cmd.setFormatter(fmt2)
# out
log1.critical("log1 critical outer  a  .......")
log2.critical("log1 critical outer b  .......")
log2.critical("log2 critical outer .......")
log2.debug("debug.....")
