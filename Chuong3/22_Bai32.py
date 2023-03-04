M1=int(input('M1='))
M2=int(input('M2='))
M3=int(input('M3='))
s=int(input('S='))
if s<=100:
    p=s*M1
elif s<=150:
    p=100*M1+(s-100)*M2
else:
    p=100*M1+50*M2+(s-150)*M3
    print('Phai tra=',p,sep='')