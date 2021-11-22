lim = int(input("Nhập giới hạn: "))
fi, se = 0, 1

while (lim <= 0):
  if (lim <= 0):
    print("Nhập sai, xin nhập lại!(> 0)")
    lim = int(input("Nhập giới hạn: "))

print(lim, "số Fibonacci đầu tiên là: ", end = "")
count = 0
while (count < lim):
  if(count <= 1):
    th = count
  else:
    th = fi + se
    fi = se
    se = th
  print(th, end = " ")
  count += 1
