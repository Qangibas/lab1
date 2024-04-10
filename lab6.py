#----------------------------------------------Python builtin function----------------------------------------------
#1
def multiple(n, arr):
    n = int(input())
    for i in arr:
        i*n
    return arr

arr = [4,2,5,8,35,84,34,23]
n = int(input())
print(multiple(n,arr))

#2
def func(str):
    a = 0
    b = 0
    for i in range(len(str)):
        if str[i].isupper():
            a+=1
        elif str[i].islower():
            b+=1
    return a, b
str = input()
print(func(str))

#3
def pal():
    if str[::-1] == str:
        return "its palendrom"  
str = input()
print(pal(str))


#4
def square_root(number, milliseconds):
    start_time = sum(iter(range(1000000)))
    while (sum(iter(range(1000000))) - start_time) * 1000 < milliseconds:
        pass
    return number ** 0.5

number = 25100
millisec = 2123

print(square_root(number, millisec))

#5
def check(arr):
    b = 0
    for i in arr:
        if i == False:
            b+=1
    if b == 0:
        return True
arr = (True,3,7,3,74,4,0)
print(check(arr))


#-------------------------------------------Python Directories and Files exercises---------------------------------------
#1
import os
path = 'example.txt'
directories = []
files = []
all = []

all = os.listdir(path)

for item in all:
    if os.path.isdir(os.path.join(path, item)):
        directories.append(item)
    else:
        files.append(item)
print(directories,"\n", files, "\n", all)

#2
if os.access(path, os.R_OK):
    print("есть доступ к чтению")
if os.access(path, os.W_OK):
    print("записывается")
if os.access(path, os.X_OK):
    print("доступен для исполнения")

#3
if not os.path.exists(path):
    print("существует")
    print(os.path.dirname(path), os.path.basename(path))

#4
with open(path, 'r') as file:
    lines = sum(1 for i in file)
    print(lines)

#5
list = [1,2,3,4,5]
with open(path, 'w') as file:
    for item in list:
        file.write(str(item) + '\n')

#6
import string
let = string.ascii_uppercase
for i in let:
    file = f"{i}.txt"
    with open(file, 'w') as file:
        file.write(file)

#7
copy = 'one_more_example.txt'
with open(path, 'r') as sour:
    cont = sour.read
with open(copy, 'w') as dest:
    dest.write(cont)

#8
if not os.path.exists(path):
    print("существует")
if os.access(path, os.W_OK):
    print("доступ есть")
os.remove(path)
