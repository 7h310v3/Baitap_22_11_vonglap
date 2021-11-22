lim = int(input("Nhập số cần tính giai thừa : "))

while (lim <= 0):
  print("Nhập sai, xin nhập lại (> 0)")
  lim = int(input("Nhập số cần tính : "))

count = 1
fac = 1
tmp = ""

while (count <= lim):
  if(count < lim):
    tmp += str(count) + "*"
  else:
    tmp += str(count)
  fac *= count
  count += 1

print("Giai thừa của", lim, "là: ", tmp, "=",fac)
