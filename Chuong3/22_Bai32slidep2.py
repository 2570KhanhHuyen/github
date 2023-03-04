n=int(input('n='))
x=1
while x<=n and 1<=n<=50:
    print(x,end=' ')
    x=x+1
    while x%10==0:
        print(x)
        x=x+1