def bsf(x, y):
    q=[]
    v=[[0]*m for _ in range(n)]
    q.append((0,0))
    v[0][0]=1
    
    while q:
        ci,cj=q.pop(0)
        
        if (ci,cj)==(x,y):
            return v[x][y]
        
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj=ci+di,cj+dj
            if 0<=ni<n and 0<=nj<m and arr[ni][nj]==1 and v[ni][nj]==0:
                q.append((ni,nj))
                v[ni][nj]=v[ci][cj]+1        

n,m=map(int,input().split())
arr=[list(map(int,input())) for _ in range(n)]  

ans=bsf(n-1,m-1)
print(ans)
