import os
import sys
import subprocess
import time         #时间模块

os.chdir(sys.path[0])

subprocess.getoutput("./speedtest.py --list > ./list.txt")  #获取服务器代码列表
f = open("list.txt", "r")
list_txt = []
for i in f:
    list_txt.append(i[:5].strip())      #读取一行将前5个字符提取并去掉前后空格 str.strip() 默认去掉前后空格
del list_txt[0]                         #删除列表中的第一个元素，因为服务器代码列表文件中第一行是独白
f.close()                               #关闭文件

speedtestshell = "python3 ./speedtest.py --server "     #命令行参数


subprocess.getoutput("echo '' > log.txt")               #清空log.txt中的日志，没有顺便创建该文件
number = len(list_txt)
#默认只执行一周期。（将下一行 “while number” 替换成 “while True” 将无限循环。注：建议将末尾行的代码一并注释掉）
while number:
#while True:
    for i in list_txt:
        if i == '':     #判断取到是否为空
            #print(subprocess.getoutput("python3 ./speedtest.py"))
            stu = subprocess.getoutput("python3 ./speedtest.py")
        else:
            shellall = speedtestshell+i
            #print(subprocess.getoutput(shellall))
            #print("---------------------------------------------------------------"+"\n")
            stu = subprocess.getoutput(shellall)
        time_new = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        subprocess.getoutput('echo "%s\n服务器代码：%s\n测试时间：%s\n" >> log.txt' % (stu,i,time_new))
        number -= 1        #每完成一个就减一，当number=0时完成一个周期，此时因number=0不会再次进入循环，脚本结束。
