t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    for j in range(len(a.sort())):
        if a[j]%a[0]!=0 or a[0] < len(a)  :
            print("YES")
        else:
            print("NO") 
