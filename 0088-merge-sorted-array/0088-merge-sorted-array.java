class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
       int[] merged = new int[m+n];
       int i = 0,j = 0,k = 0;
        while(i<m && j < n){
            if(nums1[i] <= nums2[j] ){
                merged[k++] = nums1[i++];
            }else{
                merged[k++] = nums2[j++];
            }
        }
        while(i < m){
            merged[k++] = nums1[i++];
        }
        while(j < n){
            merged[k++] = nums2[j++];
        }
        for(k = 0;k<m+n;k++){
            nums1[k] = merged[k];
        }
    }
}