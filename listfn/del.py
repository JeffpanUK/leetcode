#-*-coding:utf-8-*-

import os
import sys

fn = open("malware-list-1.txt","r")
for f in fn:
  f=f.strip()
  print(f)
  os.remove(f)
