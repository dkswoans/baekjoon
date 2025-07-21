node, edge, start=map(int, input().split())

graph = [[0]*(node+1) for _ in range(node+1)]
for i in range(edge):
    a, b=map(int,input().split())
    graph[a][b] = graph[b][a] = 1
visited1=[0]*(node+1) #node개수 + 1
visited2=[0]*(node+1)

def dfs(start):
    visited1[start]=1
    print(start, end=' ')
    for i in range(1,node+1):
        if graph[start][i]==1 and visited1[i]==0:
            dfs(i)
def bfs(start):
    queue=[start]
    visited2[start]=1
    while queue:
        start=queue.pop(0)
        print(start, end=' ')
        for i in range(1, node+1):
            if(visited2[i]==0 and graph[start][i]==1):
                queue.append(i)
                visited2[i]=1
dfs(start)
print()
bfs(start)
    