#include <stdio.h>
int main()
{
    int n,i,j;
    printf("Enter array size ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter values in array \n");

    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }


    for(i=n;i>0;i--)
    {
        for(j=0;j<i-1;j++)
        {
            if(arr[j]>arr[j+1])

            {
                int temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
        }
    }

    printf("sorted result :\n");
    for(i=0;i<n;i++)
    {
        printf("%d ",arr[i]);
    }
    return 0;
}