package leetcode.LC00006;

import java.util.ArrayList;
import java.util.List;

/*
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G

 */
public class LC00006 {
    public static void main(String[] args) {
        LC00006 lc00006 = new LC00006();

    }
    /*
    解法一:按行排序
     */
    public String convert(String s, int numRows) {
        List<StringBuilder> list = new ArrayList<StringBuilder>();
        StringBuilder result = new StringBuilder();

        if (numRows == 1 || s.length() <= 1) {
            return s;
        }
        for (int i = 0; i < Math.min(numRows, s.length()); ++i) {
            list.add(new StringBuilder());
        }
        int curRow = 0;
        boolean goingDown = false;
        for (int i = 0; i < s.length(); ++i) {
            list.get(curRow).append(s.toCharArray()[i]);
            if (curRow == 0 || curRow == numRows - 1) {
                goingDown=!goingDown;
            }
            curRow += goingDown? 1:-1;
        }
        for(StringBuilder row:list){
            result.append(row);
        }
        return result.toString();
    }
    /*
    对于numRow=4的情况，不难发现每个字符所在行变为
    0 1 2 3 4 5 6 7 8 9 10 11 12 13
    0 1 2 3 2 1 0 1 2 3  2  1  0 ...
    重组后，有  mod=6
    0     6       12
    1   5 7    11 13
    2 4   8 10    14
    3     9       15

    numRow=3:mod=4
    0   4   8     12
    1 3 5 7 9  11 13 15
    2   6   10    14

    numRow=5:mod=8
    0      8
    1    7 9        15
    2  6   10    14
    3 5    11 13
    4      12
    numRow=6:mod=10,  
    0      10
    1    9 11
    2   8  12
    3  7   13
    4 6    14
    5      15
    range(0,len/2*(numRows-1))*2*(numRows-1)

     */
    public String convert2(String s, int numRows) {
        if (numRows <= 1 || s.length() <= 1) {
            return s;
        }

        for(int i =0;i<s.length();++i){
            int num = i%(2*(numRows-1));

        }
        return s;
    }

}
