# cook your dish here
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    if a<10 or b<10 or c<10 or (a+b+c)<100:
        print("FAIL")
    else:
        print("PASS")