import random
y= random.randint(1,10)
for i in range(3):
    x = int(input("Nhập số: "))
    if x == y:
        print("Bạn đã đoán đúng")
        break
    else:
        print("Bạn đoán sai rồi")
else:
    print(f"Game Over. Số đúng là {y}")
