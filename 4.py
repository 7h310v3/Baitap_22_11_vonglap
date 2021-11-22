import math

list1 = []

lim = int(input("Nhập giới hạn: "))
num = 1

while (lim < 0):
  print("Nhập sai, xin nhập lại !(> 0)")
  lim = int(input("Nhập giới hạn: "))

count = 0

while (num < lim):
    flag = 0
    tmp = 2
    while (tmp <= math.sqrt(num)):
        if ((num % tmp) == 0):
            flag = 1
        tmp = tmp + 1
    if (flag == 0 and num != 1):
        count += 1
        list1.append(num)
    num += 1

if(count > 0):
    print("Các số nguyên tố bé hơn ", lim, "là: ", list1)
else:
    print("Không có số nguyên tố nào bé hơn", lim)