package learn_demo.dp_demo;

/**
 * 动态规划(Dynamic Programming)
 * 三核心:
 * 1. 重叠子问题
 * 2. 最优子结构
 * 3. 状态转移方程
 *
 *
 */
public class dp_learn {

    public static void main(String[] args) {
        CoinChange coinChange = new CoinChange();
        int i = coinChange.coinChange();
        System.out.println(i);
    }
}
