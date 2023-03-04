x=float(input('x='))
y=float(input('y='))
ch=input('Phep toan:')
if ch=='+'or ch=='-'or ch=='*'or ch=='/':
    if ch=='+':
     print(x,'+',y,'=',x+y,sep='')
elif ch=='-':
    print(x,'-',y,'=',x-y,sep='')
elif ch=='*':
    print(x,'*',y,'=',x*y,sep='')
elif ch=='/':
    print(x,'/',y,'=',x/y,sep='')
else:
    print('Khong hop le')
if ch=='/'and y==0:
    print('Khong hop le')
