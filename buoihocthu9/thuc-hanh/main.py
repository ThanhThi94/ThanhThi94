a = int(input("Nhập giá trị a:"))
b = int(input("Nhập giá trị b:"))
y = 0
for x in range(a, b+1):
    y += x
    print(f"Vòng lặp {x}. y = {y}")

print(f"Tổng là: {y}")

