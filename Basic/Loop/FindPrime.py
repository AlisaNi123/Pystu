#!/usr/bin/env python
#coding=utf-8

# signal = 0
# for i in range(2, 101):
#     if i == 2 or i == 3:
#         print i
#     for j in range(2, i/2+1):
#         if i % j == 0:
#             signal = 0
#             break
#         else:
#             signal = 1
#     if signal == 1:
#         print i

for i in range(2, 101):
    j =2
    while(i%j !=0):
        j+=1
    if j==i:
        print i
