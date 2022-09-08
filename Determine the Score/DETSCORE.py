# cook your dish here
t=int(input())
for i in range(t):
    X,N=map(int,input().split())
    p=X//10
    print(N*p)
