#include<stdio.h>
int main(){
    int N,max,min;
    scanf("%d",&N);
    int a[N];
    for(int i=0;i<N;i++){
        scanf("%d",&a[i]);
        max=a[0];
        min=a[0];
    }
    for(int i = 0; i<N; i++){
        if(max<a[i]){
            max=a[i];
        }
        if(min>a[i]){
            min = a[i];
        }
    }
    printf("%d %d",min,max);
    return 0;
}