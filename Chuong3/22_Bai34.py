Toan=float(input(''))
Ly=float(input(''))
Hoa=float(input(''))
dtb=(Toan*2+Ly*3+Hoa)/6
if dtb<3:
    print('Kem')
elif dtb<5:
    print('Yeu')
elif dtb<6:
    print('Trung binh')
elif dtb<7:
    print('Trung binh kha')
elif dtb<8:
    print('Kha')
elif dtb<9:
    print('Gioi')
else:
    print('Xuat sac')