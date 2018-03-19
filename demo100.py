#demo1 wait a second
# import time
# print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
# #wait a second
# time.sleep(1)
# print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
#
#demo2   rabbit
# import string
# def f_rabbit( n):
#     if n<= 2:  #n ==1 or n==2:
#         rab_sum = 1
#     else:
#         rab_sum = f_rabbit(n - 1) + f_rabbit(n - 2)
#     # print(rab_sum)
#     return rab_sum
# n=input('input a integer:')
# n= int(n)
#
# for i in range(1,n):
#     rabbit_sum = f_rabbit(i)
#     print(rabbit_sum)

# #demo 3 ball fall rise
# height_total =100.0
# height_total_sum =0
# height_total_sum_total =0.0
# num =input('input a integer:')
# num =int(num)
# for i in range(1,num):
#     height_total_sum=height_total
#     height_total /=2
#     height_total_sum_total +=(height_total_sum*2)
# print(str(i) +'count'+ '  '+str(height_total))
# print(str(i) +'total'+ '  '+str(height_total_sum_total -100))
