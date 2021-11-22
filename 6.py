import math

list1 = []

num = 10001

while (num < 100000):
    flag = 0
    tmp = 2
    while (tmp <= math.sqrt(num)):
        if ((num % tmp) == 0):
            flag = 1
        tmp = tmp + 1
    if (flag == 0 and num != 1):
        list1.append(num)
    num += 1

print("Các số nguyên tố có 5 chữ số là :", list1)