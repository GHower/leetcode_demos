package leetcode.LC00009;

/*
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

进阶:
你能不将整数转为字符串来解决这个问题吗？
 */
public class LC00009 {
    public static void main(String[] args) {
        LC00009 lc = new LC00009();
        lc.isPalindrome2(121);
    }

    public boolean isPalindrome(int x) {
//        if (x <= 0) return false;
        String s = String.valueOf(x);
        int left = 0, right = s.length() - 1;
        while (s.charAt(left) == s.charAt(right) && left < right) {
            ++left;
            --right;
        }
        System.out.println(left >= right);
        return left >= right;
    }

    /*
    进阶
    8

     */
    public boolean isPalindrome2(int x) {

        int f = x;
        int sum = 0;
        while (f > 0) {
            sum = sum * 10 + f % 10;
            f /= 10;
        }
        System.out.println(sum==x);
        return sum == x;
    }
}
