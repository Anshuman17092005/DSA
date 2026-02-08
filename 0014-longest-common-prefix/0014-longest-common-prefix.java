class Solution {
    public String longestCommonPrefix(String[] strs) {
        String str = strs[0];
        if (strs == null || strs.length == 0) return "";
        for(int i = 1;i < strs.length;i++){
            int j = 0;
            while (j < str.length() &&
                   j < strs[i].length() &&
                   str.charAt(j) == strs[i].charAt(j)) {
                j++;
            }

            str = str.substring(0, j);
            if (str.isEmpty()) return "";
            }
        return str;
    }
}