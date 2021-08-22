import math
a = float(input("Cạnh a dài bào nhiêu: "))
while a <= 0:
    a = float(input('Cạnh phải lớn hơn 0. Nhập lại cạnh a:'))
b = float(input("Cạnh b dài bào nhiêu: "))
while b <= 0:
    b = float(input('Cạnh phải lớn hơn 0. Nhập lại cạnh b:'))
c = float(input("Cạnh c dài bào nhiêu: "))
while c <= 0:
    c = float(input('Cạnh phải lớn hơn 0. Nhập lại cạnh c:'))


if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Tam giác đều")
    elif (a == b and a < c) or (a == c and a < c) or (b == c and b < c):
        print("Tam giác cân")
