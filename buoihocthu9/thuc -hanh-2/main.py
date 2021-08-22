a = int(input("Nhập giá trị đầu:"))
b = int(input("Nhập giá trị cuối:"))

for x in range(a, b+1):
    if x % 15 ==0:
        print(f"Số {x} là FizzBuzz")
    elif x % 3 ==0:
        print("Số " + str(x) + " là Fizz")
    elif x % 5 ==0:
        print("Số",x,"Buzz")
else:
    print("Kết thúc")
