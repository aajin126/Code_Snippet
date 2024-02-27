#include<stdio.h>
int min (int x, int y);
int main()
{
    int num[1000001];
    num[0] =0;
    num[1] =0;
    
    int n;
    scanf("%d",&n);
    
    for(int i = 2;i<=n;i++)
    {
        num[i]=num[i-1]+1;
        
        if(i%3==0)
        {
            num[i]=min((num[i/3]+1),num[i]);
        }
        if(i%2==0)
        {
            num[i]=min((num[i/2]+1),num[i]);
        }
    }
    printf("%d",num[n]);
    return 0;
}
int min (int x, int y)
{
    if(x>y)
        return y;
    else
        return x;
}