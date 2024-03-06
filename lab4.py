#--------------------------Python date--------------------------

import datetime
# #1
# x = datetime.datetime.now()
# y = x - datetime.timedelta(days=5)
# print(y.strftime("%Y-%m-%d"))

# #2ss
# today = datetime.datetime.now()
# yesterday = today - datetime.timedelta(days=1)
# tomorrow = today + datetime.timedelta(days=1)

# print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
# print("Today:", today.strftime("%Y-%m-%d"))
# print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))

# #3
# date = datetime.datetime.now()
# date_without = date.replace(microsecond=0)
# print(date_without)
# import math
# #4
# x = datetime.datetime(2024, 2, 22, 0, 0, 0)
# y = datetime.datetime(2024, 2, 21, 0, 0, 0)
# xy = (x - y).total_seconds()
# print(math.fabs(xy))

# #--------------------------Python iterators and generators--------------------------
# #1
# def generator(n):
#     for i in range(n):
#         yield i**2
# n = int(input())
# a = generator(n)
# for i in a:
#     print(i)

# #2
# def even_numbers(n):
#     for i in range(n):
#         if i % 2 == 0:
#             yield i
# n = int(input())
# a = even_numbers(n)
# for i in a:
#     print(i,end=",")
# print()
# #3s
# def divisible_numbers(n):
#     for i in range(n):
#         if i % 3 == 0 and i % 4 == 0:
#             yield i
# n = int(input())
# a = divisible_numbers(n)
# for i in a:
#     print(i)

# #4
# def squares(a,b):
#     for i in range(a,b):
#         yield i**2  
# a = int(input())
# b = int(input())
# c = squares(a,b)
# for i in c:
#     print(i)

# #5
# def down(n):
#     while n > 0:
#         yield n
#         n-=1
# n = int(input())
# a = down(n)
# for i in a:
#     print(i)

# # #--------------------------Math--------------------------
# import math
# #1
# deg = int(input())
# print(math.radians(deg))

# #2
# h, a, b = map(int,input().split())
# print((a+b)/2*h)

# #3
# n, s = map(int,input().split())
# print((1/4)*n*s**2*(1/math.tan(math.pi/n)))

# #4
# a, h = map(int,input().split())
# print(a*h)

#--------------------------JSON--------------------------
import json

file = open("sample-data.json")
a = json.load(file)

print('''Interface Status
=========================================================================
DN                                              Description     Speed       MTU
------------------------------------------      -----------     -------     ----''')

print(a["imdata"][0]["l1PhysIf"]["attributes"]["dn"], a["imdata"][0]["l1PhysIf"]["attributes"]["descr"]," "*19, a["imdata"][0]["l1PhysIf"]["attributes"]["speed"]," "*3, a["imdata"][0]["l1PhysIf"]["attributes"]["mtu"])
print(a["imdata"][1]["l1PhysIf"]["attributes"]["dn"], a["imdata"][1]["l1PhysIf"]["attributes"]["descr"]," "*19, a["imdata"][1]["l1PhysIf"]["attributes"]["speed"]," "*3, a["imdata"][1]["l1PhysIf"]["attributes"]["mtu"])
print(a["imdata"][2]["l1PhysIf"]["attributes"]["dn"], a["imdata"][2]["l1PhysIf"]["attributes"]["descr"]," "*19, a["imdata"][2]["l1PhysIf"]["attributes"]["speed"]," "*3, a["imdata"][2]["l1PhysIf"]["attributes"]["mtu"])
