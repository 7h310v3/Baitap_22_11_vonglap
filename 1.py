list1 = []

count = 10

while (count <= 200):
  if ((count % 7) == 0) and ((count % 5) != 0):
    list1.append(count)
  count += 1

if(len(list1) == 0):
    print("Không có số nào chia hết cho 7 nhưng không là bội của 5 trong khoảng 10 đến 200!")
else:
    print("Các số chia hết cho 7 nhưng không là bội của 5 trong khoảng 10 đến 200 là: ")
    print(list1)