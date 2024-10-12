__author__ = 'Administrator'
# -*- coding: UTF8 -*-

import time
import datetime
import shutil
import unicodedata
import os
import filecmp
#get file addr


def TimeStampToTime(timestamp):
  timeStruct = time.localtime(timestamp)
  return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)

# def get_FileModifyTime(filePath):
#   filePath = unicode(filePath,'utf8')
#   t = os.path.getmtime(filePath)
#   return TimeStampToTime(t)
def getFile1(request_path):
    for item in os.listdir(request_path):
        full_path = os.path.join(request_path, item)
        fsize = os.path.getsize(full_path)
        fmtime = TimeStampToTime(os.path.getmtime(full_path))

        if os.path.isdir(full_path):
            getFile1(full_path)
        else:# file_list[1].append({'name':item,'fsize':fsize,'fmtime':fmtime})#'files'

            amendtime = os.stat(full_path).st_mtime
            file_size = os.path.getsize(full_path)/ 1024 / 1024

            # print(TimeStampToTime(amendtime) + '-文件-' + item)
            full_path_new = dir + TimeStampToTime(amendtime) + item

            if file_size >100:
                print('dir' + TimeStampToTime(time.time()) + ' '+ full_path+ str(file_size))
                full_path_new = r'D:\test'
                print(full_path + '  ' +full_path_new)
                shutil.copy(full_path, full_path_new)
            full_path =""


dir = os.getcwd()
request_path =r"D:\download-movie"
file_list_name =os.listdir(request_path)
file_list =[]
# print(file_list_name)
getFile1(request_path)
#get alter datetime

#alter file name



