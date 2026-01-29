class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
    //    int[] merged = new int[m+n];
    //    int i = 0,j = 0,k = 0;
    //     while(i<m && j < n){
    //         if(nums1[i] <= nums2[j] ){
    //             merged[k++] = nums1[i++];
    //         }else{
    //             merged[k++] = nums2[j++];
    //         }
    //     }
    //     while(i < m){
    //         merged[k++] = nums1[i++];
    //     }
    //     while(j < n){
    //         merged[k++] = nums2[j++];
    //     }
    //     for(k = 0;k<m+n;k++){
    //         nums1[k] = merged[k];
    //     }

    int i = m-1;
    int j = n-1;
    int k = m+n-1;
    while(i >= 0 && j >= 0){
        if(nums1[i] > nums2[j]){
            nums1[k] = nums1[i];
            k--;
            i--;
        }else{
            nums1[k] = nums2[j];
            k--;
            j--;
        }
    }
    while(j>=0){
        nums1[k] = nums2[j];
        k--;
        j--;
    }
    }
}