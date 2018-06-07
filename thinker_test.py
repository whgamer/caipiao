import re
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from tkinter import *
import tkinter.filedialog


def moveFile():
   pass
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
r =0
for label_row in list_label:
   Label(root, text=label_row, fg='blue', font='Helvetica -12 bold', justify='left').grid(row=r,column =0)
   contentEntry1 = tk.Entry(root, textvariable='').grid(row =r,column =1)
   r = r + 1

contentVar1 =tk.StringVar(root,'')
contentEntry1 =tk.Entry(root,textvariable=contentVar1)#,textvariable=contentVar1
contentEntry1.grid(row=0,column =1)
Button(root, text='...', command=lambda:show_file(contentVar1)).grid(row=0, column=2, sticky=E, pady=4)

contentVar2 =tk.StringVar(root,'')
contentEntry2 =tk.Entry(root,textvariable=contentVar2)
contentEntry2.grid(row=1,column =1)

number = tk.StringVar()
numberChosen = ttk.Combobox(root, width=17, textvariable=number)#width=12,
numberChosen['values'] = ('mp3', 'avi', 'rmvb', 'rm', 'other')     # 设置下拉列表的值
numberChosen.grid(column=1, row=2)      # 设置其在界面中出现的位置  column代表列   row 代表行
numberChosen.current(0)

contentVar3 =tk.StringVar(root,'')
contentEntry3 =tk.Entry(root,textvariable=contentVar3)
contentEntry3.grid(row=3,column =1)

# contentVar4 =tk.StringVar(root,'')
# contentEntry4 =tk.Entry(root,textvariable=contentVar4)
# contentEntry4.grid(row=4,column =1)

Button(root, text='...', command=lambda:show_file(contentVar3)).grid(row=3, column=2, sticky=E, pady=4)#lambda make you  less function definition

Button(root, text='Quit', command=root.quit).grid(row=4, column=1, sticky=E, pady=4)
Button(root, text='Show', command=moveFile).grid(row=4, column=0, sticky=E, pady=4)



root.mainloop()
