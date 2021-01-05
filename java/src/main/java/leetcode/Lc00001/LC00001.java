package leetcode.Lc00001;

import java.util.HashMap;

public class LC00001 {
    public static void main(String[] args) {
        int[] nums = {0,4,3,0};
        int target = 0;

        LC00001 lc = new LC00001();
        lc.twoSum(nums, target);
    }

    /**
     *
     *
     *
     */
    public int[] twoSum(int[] nums, int target) {
        int[] arrs = new int[2];
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for(int i=0;i<nums.length;++i){
            if (map.containsKey(nums[i])) {
                arrs[0] = i;
                arrs[1] = map.get(nums[i]);
                // sout会消耗大量的时间
//                System.out.println("arrs="+i+","+nums[i]);
                return arrs;
            }
            map.put(target-nums[i],i);
        }
        return arrs;
    }

}
