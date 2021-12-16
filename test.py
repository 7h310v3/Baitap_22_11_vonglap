import math

list1 = []

lim = int(input("Nhập bao nhiêu số nguyên tố cần in ra: "))

while (lim < 0):
  print("Nhập sai, xin nhập lại !(> 0)")
  lim = int(input("Nhập bao nhiêu số nguyên tố cần in ra: "))

num = 1
count = 0

while (count < lim):
    tmp = 2
    flag = 0
    for tmp in range(2, math.sqrt(num)):
        if ((num % tmp) == 0):
            flag = 1
        tmp = tmp + 1
    if (flag == 0 and num != 1):
        list1.append(num)
        count += 1
    num += 1

if(count > 0):
    print("Các số nguyên tố là: ", list1)
else:
    print("Không có số nguyên tố nào cả!")
