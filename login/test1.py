a=[-2, 3, 5, 0, -1, 2, 1]
n=len(a)
s=0
for i in range(n-1):
    for j in range(i+1,n):
        for k in range(j+1,n):
                if a[i]+a[j]+a[k]==s:
                     print(a[i],a[j],a[k])

