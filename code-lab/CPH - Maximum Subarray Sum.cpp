#include<bits/stdc++.h>
using namespace std;

int maximum_subarray_sum(vector<int> nums, int n) {
    int best = 0;

    for(int a = 0; a < n; a++) {
        int sum = 0;
        for(int b = a; b < n; b++) {
            for(int c = a; c < n; c++) {
                sum += nums[c];
            }
            best = max(best, sum);
        }
    }
    return best;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    vector <int> nums;
    int n;
    cout << "Enter the value of n: " << endl;
    cin >> n;
    
    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;
        nums.push_back(a);
    }

    int result = maximum_subarray_sum(nums, nums.size());
    cout << result << endl;

    return 0;
}