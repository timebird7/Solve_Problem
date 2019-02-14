#include <iostream>

using namespace std;

int main() {
    int start, n = 0;
    
    int nums[100][100];
    for (int i=0; i<10; ++i) {
        int m = 99;
        cin >> n;
        

        for (int j = 0; j < 100; ++j)
            for (int k = 0; k < 100; ++k)
                cin >> nums[j][k];

        for (int c=0;c<100;++c) {
            if (nums[99][c] == 2) {
                start = c;
                break;
            }
        }

        while (m > 0) {
            if (start >0 and nums[m][start-1] == 1) {
                while (start >0 and nums[m][start-1] == 1) {
                    --start;
                    
                }
                --m;
                continue;
            } else if (start<99 and nums[m][start+1] == 1) {
                while (start<99 and nums[m][start+1] == 1) {
                    ++start;
                    
                }
                --m;
                continue;
            } else {
                --m;
            }
        }

            
        
        cout << "#" << i+1 << " " << start << endl;
    }
}