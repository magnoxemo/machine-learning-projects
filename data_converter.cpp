
"""this code is written by  which basically trims the raw cross section data """

include<bits/stdc++.h>
using namespace std;
int main()
{
    FILE  *ptr=fopen("data.txt","r");
    FILE *ptr2=fopen("Output.txt","w");
    int cnt=0;
    char ch[500],s;
    while(fscanf(ptr,"%[^\n]",ch)!=EOF)
    {
        cnt=0;
        int flag=0,flag2=1;
        for(int i=0; ch[i]!='\0'; i++)
        {
            if(ch[i]!=' ')
            {
                fprintf(ptr2,"%c",ch[i]);
                flag++;
            }
            else if(flag && flag2==1)
            {
                fprintf(ptr2,",");
                flag=0;
                flag2=0;
            }
        }
        fprintf(ptr2,"\n");
        fscanf(ptr,"%c",&s);
    }
    return 0;
}
