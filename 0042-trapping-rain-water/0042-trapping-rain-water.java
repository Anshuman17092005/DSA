class Solution {
    public int trap(int[] height) {
        int water = 0;
        int lmax = 0;
        int rmax = 0;
        int l = 0,r = height.length-1;
        // for(int i = 0;i<height.length;i++){
        //     int left = i,right = i;

        //         lmax = height[i];
        //     while(left >= 0){
        //         if(height[left] > lmax){
        //             lmax = height[left];
        //         }else{
        //             left--;
        //         }
        //     }
        //        rmax = height[i];
        //     while(right < height.length){
        //        if(height[right] > rmax){
        //         rmax = height[right];
        //         }else{
        //         right++;
        //         }
        //     }
        //     int qnt = Math.min(lmax,rmax) - height[i];
        //     if (qnt > 0) water += qnt;
        // }
        // return water;

        while(l <= r){
            if(height[l] <= height[r]){
                lmax = Math.max(lmax,height[l]);
                water += lmax - height[l];
                l++;
            }else{
                    rmax = Math.max(rmax,height[r]);
                    water += rmax - height[r];
                    r--;
        }
    }
    return water;
    }
}