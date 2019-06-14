#include <iostream>
using namespace std;

void bubble_sort(int* l, int len)
{
    int tmp = 0;
    for(int i=0;i<len-1;i++)
    {
        for(int j=0;j<len-i-1;j++)
        {
            if(l[j] > l[j+1])
            {
                tmp = l[j];
                l[j] = l[j+1];
                l[j+1] = tmp;

            }
        }
    }
}

void selection_sort(int* l, int len)
{
    int tmp = 0;
    for(int i=0;i<len-1;i++)
    {
        int minIndex = i;
        for(int j=i+1;j<len;j++)
        {
            if(l[minIndex] > l[j])
                minIndex = j;
        }

        if(minIndex != i)
        {
            tmp = l[minIndex];
            l[minIndex] = l[i];
            l[i] = tmp;
        }
    }
}

void insert_sort(int* l, int len)
{
	for(int i=1; i<len;i++)
	{
		int key = l[i];
		int j = i-1;
		while(j>=0)
		{
			if(key<l[j])
			{
				l[j+1] = l[j];
				l[j] = key;
				
			}
			j--;
		}
	}
}

void shell_sort(int* l, int len)
{
	int gap = len/2;
	while(gap>0)
	{
		for(int i=gap;i<len;i++)
		{
			int j = i-gap;
			int tmp = l[i];
			while(j>=0 && tmp<l[j])
			{
				l[j+gap] = l[j];
				j -= gap;
			} 
			l[j+gap] = tmp; 
		}
		gap /= 2;
	 } 
}

void merge(int arr[], int left, int mid, int right)
{
	int help[right-left+1]; 
	int i=0;
	int left_index = left;
	int right_index = mid+1;
	while(left_index <= mid && right_index <= right)
	{
		help[i++] = arr[left_index++]<arr[right_index++]? arr[left_index++]:arr[right_index]; 
	 }
	
	while(left_index<=mid)
	{
		help[i++] = arr[left_index++];	
	} 
	
	while(right_index<=right)
	{
		help[i++] = arr[right_index++];
	}
	
	for(int i=0;i<right-left+1;i++)
	{
		arr[left+i] = help[i];
	}
	
}

void merge_sort(int arr[], int left, int right)
{
	if(left==right)
	{
		return;
	}
	
	int len = sizeof(arr)/ sizeof(arr[0]);
    if(len<2){
    	return;
	}
	
	int mid = (left+right)/2;
	merge_sort(arr, left, mid);
	merge_sort(arr,mid+1,right);
	
	merge(arr,left,mid,right);
}

void print(int* l, int len)
{
    for(int i=0;i<len;i++)
    {
        cout << l[i] << '\t';
    }
    cout << endl;
}


int main() {
    int l1[] = {9,8,7,6,5,4,3,2,1};
    int l2[] = {1};
    int l3[] = {};

//    C++
    int len = sizeof(l1)/ sizeof(l1[0]);
    
    selection_sort(l1,len);
    print(l1,len);
    return 0;

}
