import java.util.*;

class Solution {
    public int longestConsecutive(int[] nums) {

        HashSet<Integer> set = new HashSet<>();

        for(int i = 0; i < nums.length; i++){
            set.add(nums[i]);
        }

        int maxi = 0;

        Integer[] arr = set.toArray(new Integer[0]);

        for(int i = 0; i < arr.length; i++){

            int ele = arr[i];

            if(!set.contains(ele - 1)){

                int cnt = 1;

                while(set.contains(ele + 1)){
                    ele++;
                    cnt++;
                }

                maxi = Math.max(maxi, cnt);
            }
        }

        return maxi;
    }
}