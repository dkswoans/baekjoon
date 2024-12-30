n=int(input())
l=[]
result=0
for _ in range(n):
    l.append(input())
for i in range(n):
    l1=[]
    d=True
    for j in range(len(l[i])):
        
        if l[i][j] in l1:
            if l[i][j]!=l[i][j-1]:
                d=False
                break
        else:
            l1.append(l[i][j])
    if d==True:
        result+=1
print(result)