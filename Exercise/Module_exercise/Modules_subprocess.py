# -*- coding:UTF-8 -*-
import subprocess
cmd='ipconfig'
p = subprocess.Popen(cmd, stdout=subprocess.PIPE,shell=True)
r1=p.stdout.readlines()
r2=[i.strip().decode('gb2312') for i in r1 if i != b'\r\n' ]
print(r2)
