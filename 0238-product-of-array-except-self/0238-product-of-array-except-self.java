// class Solution {
//     public int[] productExceptSelf(int[] nums) {
//         // int[] answer = new int[n];
//         // for(int i = 0;i<n;i++){
//         //     int left = 0;
//         //     int right = n-1;
//         //     int product = 1;
//         //     while(left < i){
//         //         product *= nums[left];
//         //         left++;
//         //     }
//         //     while(right > i){
//         //         product *= nums[right];
//         //         right--;
//         //     }
//         //     answer[i] = product;
//         // }
//         // return answer;

       

//     }
// }

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] answer = new int[n];

        // Step 1: Left products
        answer[0] = 1;
        for (int i = 1; i < n; i++) {
            answer[i] = answer[i - 1] * nums[i - 1];
        }

        // Step 2: Right products
        int rightProduct = 1;
        for (int i = n - 1; i >= 0; i--) {
            answer[i] *= rightProduct;
            rightProduct *= nums[i];
        }

        return answer;
    }
}
