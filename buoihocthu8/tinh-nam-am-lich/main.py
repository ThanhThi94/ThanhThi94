n = int(input('Nhập năm: '))
can = ['Canh', 'Tân', 'Nhâm', 'Quý', 'Giáp', 'Ất', 'Bính', 'Đinh','Mậu','Kỷ']
chi = ['Thân', 'Dậu', 'Tuất', 'Hợi','Tí','Sửu','Dần', 'Mão', 'Thìn', 'Tị', 'Ngọ', 'Mùi']

if n % 10 == 0:
    print('Canh')
elif n % 10 == 1:
    print('Tân')
elif n % 10 == 2:
    print('Nhâm')
elif n % 10 == 3:
    print('Quý')
elif n % 10 == 4:
    print('Giáp')
elif n % 10 == 5:
    print('Ất')
elif n % 10 == 6:
    print('Bính')
elif n % 10 == 7:
    print('Đinh')
elif n % 10 == 8:
    print('Mậu')
elif n % 10 == 9:
    print('Kỷ')

if n % 12 == 1:
    print('Thân')
elif n % 10 == 2:
    print('Dậu')
elif n % 10 == 3:
    print('Tuất')
elif n % 10 == 4:
    print('Hợi')
elif n % 10 == 5:
    print('Tí')
elif n % 10 == 6:
    print('Sửu')
elif n % 10 == 7:
    print('Dần')
elif n % 10 == 8:
    print('Mão')
elif n % 10 == 9:
    print('Thìn')
elif n % 10 == 10:
    print('Tị')
elif n % 10 == 11:
    print('Ngọ')
elif n % 10 == 12:
    print('Mùi')