#include <string>
#include <vector>
#include <numeric>
using namespace std;
/* numeric�������ۼӺ��� 
״̬: ��p[i]��β���ַ�����󳤶�Ϊdp[i]
ѡ��: 
base case: dp[..]=0
*/
class Solution {
	public:
		Solution(){};
		~Solution(){};
		int findSubstringInWraproundString(string p) {
			vector<int> dp(26,0);
			int num=0;
			int result=0;
			for (int i =0; i<p.size(); i++) {
				if(i>0&&((p[i-1]+1)%26==p[i]%26)){
					++num;
				}else{
					num=1;
				}
				cout<<"�±�["<<p[i]-'a'<<"]��"<<dp[p[i]-'a']<<"->"; 
				dp[p[i]-'a'] = max(dp[p[i]-'a'],num);
				cout<<dp[p[i]-'a']<<endl; 
			}
			
			return accumulate(dp.begin(),dp.end(),0);
		}
	private:
		
};
