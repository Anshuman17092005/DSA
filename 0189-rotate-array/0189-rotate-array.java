class Solution {
    public int[] reverse(int arr[],int l,int r){
        int i = l;
        int j = r;

        while(i < j){
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            i++;
            j--;
        }
        return arr;
    }
    public void rotate(int[] nums, int k) {
       int n = nums.length;
       k = k%n;
       reverse(nums,0,n-1);
       reverse(nums,0,k-1);
       reverse(nums,k,n-1);
    }
}