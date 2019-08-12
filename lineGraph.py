#utf-8
import numpy as np
import matplotlib.pyplot as plt
import xlrd
# import xlwt

from datetime import date,datetime

def read_excel():

#文件位置
 ExcelFile = xlrd.open_workbook(r'D:\1011.xls')

#获取目标EXCEL文件sheet名
 sheet1 =ExcelFile.sheet_by_index(0)#获取第一个表格
 cols_mzcount= sheet1.col_values(1)
 cols_mzrq = sheet1.col_values(0)
 cols_total = sheet1.col_values(4)
 return (cols_mzrq[1:],cols_mzcount[1:],cols_total[1:])#column data

#------------------------------------

#若有多个sheet，则需要指定读取目标sheet例如读取sheet2

#sheet2_name=ExcelFile.sheet_names()[1]
 sheet2_name=ExcelFile.sheet_names()[0]

#------------------------------------

#获取sheet内容【1.根据sheet索引2.根据sheet名称】

 sheet=ExcelFile.sheet_by_index(0)


cols_mzrq,clinic_num,cols_total = read_excel()

# x = np.linspace(0, 2 * np.pi, 100)
# names = ['1', '2', '3', '4', '5','6', '7', '8', '9', '10',]
names1 = [[i] for i in range(44)]
print(names1)
# x = range(len(cols_mzrq))
# x = range(len(cols_mzrq))
x = cols_mzrq
# x= len(clinic_num)
# y1, y2 = np.sin(x), np.cos(x)
y3 = clinic_num
y2 = cols_total
fig = plt.figure()

num1 =fig.add_subplot(111)
num1.plot(x,y3)
num1.set_ylabel('clinic count 门诊量')
num1.set_title("clinic ")

num2 =num1.twinx()
num2.plot(x,y2,'r')
num2.set_ylabel('clinic income')
# plt.plot(x, y3, label='clinic')
# plt.plot(x, y2, label='inhospital')
plt.legend()

plt.title('clinic ')
plt.xlabel('x')
plt.ylabel('y')

plt.show()