Hoten=input('Ho ten:')
Songaycong=int(input('So ngay cong:'))
Dongiangaycong=int(input('Don gia ngay cong:'))
Hesophucap=float(input('He so phu cap:'))
Tamung=float(input('Tam ung:'))
Luong=Dongiangaycong*Songaycong*Hesophucap
Thuclinh=Luong-Tamung
print('Nhan vien',Hoten,end=',',)
print('Co tien luong=',Luong,end=',',sep='')
print('Tam ung=',Tamung,end=' va ',sep='')
print('Thuc Linh=',Thuclinh,sep='')
