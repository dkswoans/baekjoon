#include<stdio.h>
#include <string.h>

int arr[1001][1001]={0,};
int visited[1001]={0,};
int node, edge, start;

int queue[1001];

void bfs(int start){
    int front=0;
    int rear=1;
    int pop;
    
    visited[start]=1;
    printf("%d ",start);
    queue[0]=start;
    while(front<rear){ //큐가 비어있으면 반복 종료
        pop=queue[front++]; //dequeue연산
        for(int i=1;i<=node+1;i++){
            if (arr[pop][i] && !visited[i]) {
				visited[i] = 1;
				printf("%d ", i);
				queue[rear++] = i; // enqueue 연산
			}
        }
    }
}

void dfs(int start){
    int i;
    visited[start]=1;
    printf("%d ",start);
    for (i=0;i<node+1;i++){
        if(arr[start][i]==1&&visited[i]==0){
            dfs(i);
        }
    }
    if (i == node) return;
}

int main(void){
    scanf("%d %d %d",&node, &edge, &start);
    
    for (int i=0;i<edge;i++){
        int a,b;
        scanf("%d %d",&a,&b);
        arr[a][b]=1;
        arr[b][a]=1;
    }
    dfs(start);
    printf("\n");
    memset(visited, 0, sizeof(visited));
    bfs(start);
}