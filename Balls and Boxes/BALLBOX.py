# cook your dish here
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    if b*(b+1)/2<=a :
        print("YES")
    else:
        print("NO")


