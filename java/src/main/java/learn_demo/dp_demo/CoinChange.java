package learn_demo.dp_demo;

/**
 * 凑零钱问题
 */
public class CoinChange {
    static int coins[]={1,2,5};
    static int amount = 11;

    int coinChange() {
        return dp(amount);
    }

    int dp(int n){

        if (n==0){
            return 0;
        }
        if(n<0){
            return 1;
        }
        int max = 1<<30;
        for (int coin : coins) {
            int subprogram = dp(n-coin);
            if (subprogram==-1)continue;
            max = Math.min(max,1+subprogram);
        }
        return max !=(1<<31) ? max:-1;
    }
}
