__author__ = 'Administrator'
# -*- coding: UTF8 -*-

import time
import datetime
import shutil
import unicodedata
import os
import filecmp
#get file addr
dir = os.getcwd()
request_path =r"C:\Users\Administrator\Pictures\testpic"
file_list_name =os.listdir(request_path)
file_list =[]
print(file_list_name)
#get alter datetime

#alter file name

def TimeStampToTime(timestamp):
  timeStruct = time.localtime(timestamp)
  return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)

# def get_FileModifyTime(filePath):
#   filePath = unicode(filePath,'utf8')
#   t = os.path.getmtime(filePath)
#   return TimeStampToTime(t)
for item in os.listdir(request_path):
    full_path = os.path.join(request_path,item)
    fsize = os.path.getsize(full_path)
    fmtime = TimeStampToTime(os.path.getmtime(full_path))
    full_path_new = r'C:\Users\Administrator\Pictures\testpic\test'
    if os.path.isdir(full_path):
        # file_list[0].append({'name':item,'fsize':str(fsize)+'KB','fmtime':fmtime})#'dirs'
        amendtime = os.stat(full_path).st_mtime
        print(TimeStampToTime(amendtime)+'-文件夹-'+item)
        # shutil.copy(full_path, 'C:\\Users\\Administrator\\Pictures\\testpic\\test\\'+TimeStampToTime(amendtime)+'-文件夹-'+item)
        # print('file'+TimeStampToTime(time.time()))
    else:
        # file_list[1].append({'name':item,'fsize':fsize,'fmtime':fmtime})#'files'
        amendtime = os.stat(full_path).st_mtime
        print(TimeStampToTime(amendtime)+'-文件-'+item)
        full_path_new =dir + TimeStampToTime(amendtime)+item
        shutil.copy(full_path,full_path_new)
        # print('dir'+TimeStampToTime(time.time()))