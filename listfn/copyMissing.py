#-*-coding:utf-8-*-
import os
import shutil

root=r"test"

dest=r"fromWenlu"
curDir=os.getcwd()
destf = os.path.join(curDir, dest)
if not os.path.exists(destf):
  os.mkdir(destf)
fn = open("missing-list.txt","r")
for line in fn:
	line = line.strip()
	f = os.path.join(root, line)
	shutil.copy(f, os.path.join(destf, line))
	