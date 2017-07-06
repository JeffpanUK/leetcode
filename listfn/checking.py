#-*-coding:utf-8-*-

import os
import sys
import time

rootdir = sys.argv[1]
startTime = "2017-06-27 18:00:00"
endTime = "2017-06-27 20:00:00"

startStamp = time.mktime(time.strptime(startTime, "%Y-%m-%d %H:%M:%S"))
endStamp = time.mktime(time.strptime(endTime, "%Y-%m-%d %H:%M:%S"))

fout = open('malware-list.txt','w')
for parent,dirnames,filenames in os.walk(rootdir):
  for filename in filenames:
    fn = os.path.join(parent,filename)
    t = os.path.getmtime(fn)
    if(t>startStamp and t<endStamp):
      fout.write("%s\n"%fn)
      print(fn)
      
    
    