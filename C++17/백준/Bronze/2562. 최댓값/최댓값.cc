#include<stdio.h>
int main(void){
    int a[10],max = 0,num = 0;
    for(int i=0;i<9;i++){
        scanf("%d",&a[i]);
        
    }
    for(int i=0;i<9;i++){
        if(max<a[i]){
            max=a[i];
            num = i+1;
        }
    }
    printf("%d\n%d",max,num);
    return 0;
}