import re
import tkinter as tk
import time
import os
# import requests
import tkinter.messagebox
from tkinter import ttk
from tkinter import *
import tkinter.filedialog
import shutil

def TimeStampToTime(timestamp):
  timeStruct = time.localtime(timestamp)
  return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)
def moveFile(request_path,pathTo,size):# there is a bug 路径下文件夹存在与上一目录文件相同名称则不会复制此文件夹下面文件
    for item in os.listdir(request_path):
        full_path = os.path.join(request_path, item)
        src_FileSize = os.path.getsize(full_path)
        src_FileName = check_file(item,pathTo,src_FileSize)
        fsize = os.path.getsize(full_path)
        fmtime = TimeStampToTime(os.path.getmtime(full_path))

        if os.path.isdir(full_path):
            moveFile(full_path,pathTo,size)
        else:# file_list[1].append({'name':item,'fsize':fsize,'fmtime':fmtime})#'files'

            amendtime = os.stat(full_path).st_mtime
            file_size = os.path.getsize(full_path)/ 1024 / 1024

            # print(TimeStampToTime(amendtime) + '-文件-' + item)
            full_path_new = "" #dir + TimeStampToTime(amendtime) + item
            size =float(size)
            if size != '':
                if file_size >size:
                    print('dir' + TimeStampToTime(time.time()) + ' '+ full_path+ str(file_size))
                    full_path_new = pathTo +"/" + src_FileName #r'D:\迅雷下载\test'  src_FileName
                    print(full_path + '  ' +full_path_new)
                    shutil.copy(full_path, full_path_new)
                    # text_var.set(full_path + full_path_new+ str(file_size) )# modi float to string type
            full_path =""
#demo
# https://stackoverflow.com/questions/18383384/python-copy-files-to-a-new-directory-and-rename-if-file-name-already-exists
def check_file(SrcFileName,target_FilePath,src_FileSize):
    # src_size = os.path.getsize(SrcFileName)
    # targ_size = os.path.getsize(target_FilePath)
    # src_name = os.path.fi
    obj_target = target_FilePath +'/' + SrcFileName
    if not os.path.isdir(target_FilePath):
        print('It is not a FilePath. ')
    if os.path.exists(obj_target):
        ii = 1
        # for base,extension in SrcFileName:
        base, extension = os.path.splitext(SrcFileName)
        while True:
            if os.path.exists(obj_target):
                # ew_name = os.path.join(basedir, base, base + "_" + str(ii) + extension)
                new_File_Name = os.path.join(base + "_" + str(ii) + 'Rename'+ str(src_FileSize)+ extension)
                break
            # else:
            #     continue
            ii += 1
    else:
        new_File_Name = SrcFileName

    return new_File_Name

def show_file(contentVar_input):#选择文件夹
   file_name =tk.filedialog.askdirectory()# choose  dir
   if file_name != '':
      contentVar1_ =file_name
      # contentEntry1.config(textvariable= contentVar1_)#这种方式貌似 不好用
      contentVar_input.set(contentVar1_)
   else:
      contentVar1_='您没有选择任何文件'
      contentVar_input.set(contentVar1_)
root =tk.Tk()
root.geometry('300x270+400+100')
root.resizable(True,True)
root.title('实用小工具--文件筛选器')

list_label =['源目录：','大小：','类型：','目标路径：']
r = 0
for label_row in list_label:
   Label(root, text=label_row, fg='blue', font='Helvetica -12 bold', justify='left').grid(row=r,column =0)
   contentEntry1 = tk.Entry(root, textvariable='').grid(row =r,column =1)
   r = r + 1

contentVar1 =tk.StringVar(root,'')
contentEntry1 =tk.Entry(root,textvariable=contentVar1)#,textvariable=contentVar1
contentEntry1.grid(row=0,column =1)
Button(root, text='...', command=lambda:show_file(contentVar1)).grid(row=0, column=2, sticky=E, pady=4)


contentVar2 =tk.StringVar(root,'0')
contentEntry2 =tk.Entry(root,textvariable=contentVar2)
contentEntry2.grid(row=1,column =1)
Label(root, text='MB', fg='blue', font='Helvetica -12 bold', justify='left').grid(row=1,column =2)

number = tk.StringVar()
numberChosen = ttk.Combobox(root, width=17, textvariable=number)#width=12,
numberChosen['values'] = ('mp3', 'avi', 'rmvb', 'rm', '所有文件类型')     # 设置下拉列表的值
numberChosen.grid(column=1, row=2)      # 设置其在界面中出现的位置  column代表列   row 代表行
numberChosen.current(4)

contentVar3 =tk.StringVar(root,'')
contentEntry3 =tk.Entry(root,textvariable=contentVar3)
contentEntry3.grid(row=3,column =1)

# contentVar4 =tk.StringVar(root,'')
# contentEntry4 =tk.Entry(root,textvariable=contentVar4)
# contentEntry4.grid(row=4,column =1)

Button(root, text='...', command=lambda:show_file(contentVar3)).grid(row=3, column=2, sticky=E, pady=4)#lambda make you  less function definition
Button(root, text='关闭', command = root.destroy).grid(row=5, column=1, sticky=E, pady=4)
Button(root, text='开始', command=lambda :moveFile(contentEntry1.get(),contentEntry3.get(),contentEntry2.get())).grid(row=5, column=0, sticky=E, pady=4)


text_var = tk.StringVar(root)
label_var = tk.Label(root, textvariable=text_var)
label_var.grid(row=4,column =1)
#full_path + full_path_new
root.mainloop()
