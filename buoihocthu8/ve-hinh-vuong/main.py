dai = int(input("Chiều dài: "))
rong = int(input("Chiều rộng: "))

print(str(dai * "*"))
for i in range(rong):
    print("*"+ str((dai-2)*" ")+"*")
print(str(dai * "*"))




