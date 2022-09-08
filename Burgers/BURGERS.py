# cook your dish here
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    max=0
    if(x>y):
        max=y
    else:
        max=x
    print(max)