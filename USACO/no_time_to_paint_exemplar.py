a=[0 for _ in range(100005)]
q=[0 for _ in range(100005)]
p=[0 for _ in range(100005)]
pl=[False for _ in range(30)]

n,m=map(int,input().split())
a=list(map(int,input().split()))
for i in range(n):
    a[i]-=64

p[1]=1
pl[a[1]]=True
for i in range(2,n+1):
    p[i]=p[i-1]
    if (a[i]>a[i-1]):
            pl[a[i]]=True
            p[i]+=1
    if (a[i]<a[i-1]):
        if (pl[a[i]]):
                p[i]+=1
                pl[a[i]]=True
        for j in range(a[i]+1,30):
                pl[j]=False

for j in range(30):
        pl[j]=False
        
q[n]=1
pl[a[n]]=True
for i in range(n-1,0,-1):
        q[i]=q[i+1]
        if (a[i]>a[i+1]):
            pl[a[i]]=True
            q[i]+=1
        if (a[i]<a[i+1]):
            if (pl[a[i]]):
                q[i]+=1
                pl[a[i]]=True
            for j in range(a[i]+1,30):
                pl[j]=False

for i in range(m):
    x,y=map(int,input().split())
    print(p[x-1]+q[y+1])