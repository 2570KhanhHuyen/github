a=float(input('Tieu thu='))
if a<=100:
    T=a*550
elif a<=150:
    T=100*550+(a-100)*750
elif a<=200:
    T=100*550+50*750+(a-150)*950
else:
    T=100*550+50*750+50*950+(a-200)*1350
VAT=0.1
Thanhtien=T+VAT*T
print('Phai tra=',round(Thanhtien,1),sep='')

