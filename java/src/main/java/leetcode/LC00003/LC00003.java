package leetcode.LC00003;


import java.util.HashMap;

public class LC00003 {
    public static void main(String[] args) {
        LC00003 lc = new LC00003();
        System.out.println(lc.lengthOfLongestSubstring("akcabckb"));
    }

    /*
    通过滑动窗口map，不断修改最左边left，和当前字符下标i，并得到max，全程出现的最大max即为答案
    复杂度o(n)
     */
    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 0) return 0;

        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        int left = 0;
        int max = 0;
        for (int i = 0; i < s.length(); ++i) {
            if (map.containsKey(s.charAt(i))) {
                left = Math.max(left, map.get(s.charAt(i)) + 1);
            }
            map.put(s.charAt(i), i);
            max = Math.max(max, i - left + 1);
        }
        return max;
    }

    /*

     */
    public int lengthOfLongestSubstring2(String s) {
        int max = 0, start = 0;
        int[] lastCharIdx = new int[128];
        for (int i = 0; i < 128; ++i) lastCharIdx[i] = -1;
        for (int i = 0; i < s.length(); ++i) {
            start = Math.max(start,lastCharIdx[s.charAt(i)]+1);
            max = Math.max(max,i-start+1);
            lastCharIdx[s.charAt(i)]=i;
        }
        return max;
    }
}
