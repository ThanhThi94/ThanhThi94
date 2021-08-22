x = 1
while x < 6:
    print("*"*x)
    x += 1
print("\n")
for i in range(5,0,-1):
    print(i*"*")
print("\n")
for i in range(5,0,-1):
    print(i*" " + "*"*(6-i))
print("\n")
for i in range(1,6):
    print(i*" " + "*"*(6-i))
