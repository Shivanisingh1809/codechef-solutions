# cook your dish here
n=int(input())
for i in range(n):
    x,y,z,s= map(int,input().split())
    if (x+y)>=(z+s):
        print(z+s)
    else:
        print(x+y)