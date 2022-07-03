#include <iostream>
#include <conio.h>
using namespace std;
void min_heap(int *a, int m, int n){
   int y, t;
   t= a[m];
   y = 2 * m;
   while (y <= n) {
      if (y < n && a[y+1] < a[y])
         y = y + 1;
      if (t < a[y])
         break;
      else if (t >= a[y]) {
         a[y/2] = a[y];
         y = 2 * y;
      }
   }
   a[y/2] = t;
   return;
}
void build_minheap(int *a, int n) {
    int k;
   for(k = n/2; k >= 1; k--) {
      min_heap(a,k,n);
   }
}
int main() {
   int n, i;
   cout<<"enter no of elements of array\n";
   cin>>n;
   int a[30];
   for (i = 1; i <= n; i++) {
      cout<<"enter element"<<" "<<(i)<<endl;
      cin>>a[i];
   }
   build_minheap(a, n);
   cout<<"Min Heap\n";
   for (i = 1; i <= n; i++) {
      cout<<a[i]<<endl;
   }
   getch();
}
