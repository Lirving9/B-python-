fp=open('test.txt','w')  #w为检测到已经写入，则清楚后再次写入
print('青岛！',file=fp)  #将青岛欢迎你写入test文件中
fp.close()

fp=open('test.txt','a')  #a为检测到已经写入，则追加写入
print('青岛！',file=fp)  #将青岛欢迎你写入test文件中
fp.close()

