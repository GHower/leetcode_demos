#include <iostream>
#include "Solution.h"
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	Solution sl;
	int res = sl.findSubstringInWraproundString("cdefabcdefgh");
	cout<<res<<endl;
	return 0;
}
