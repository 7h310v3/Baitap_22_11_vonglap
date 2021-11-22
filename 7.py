num = int(input("Nhập số cần tính: "))

while (num < 0):
  print("Nhập sai, xin nhập lại !(> 0)")
  num = int(input("Nhập giới hạn: "))

sum = 0
count = 0
tmp = ""

while (num > 0):
    sum += num % 10
    if (num > 10):
        tmp += str(num % 10) + "+"
    else:
        tmp += str(num % 10)
    num = num // 10

tmp = tmp[::-1]

print("Tổng các chữ số là:", tmp , "=", sum)