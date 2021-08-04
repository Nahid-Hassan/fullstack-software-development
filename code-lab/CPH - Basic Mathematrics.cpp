#include<bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
    // sum formulas
    // Arithmetic Progression
    // 1 + 2 + 3 + .... + n = n(n + 1) / 2
    int n = 10;
    cout << "for N = 10" << endl;
    cout << "Sum 1, 2, ... ,10: " << (n * (n + 1)) / 2 << endl;

    // 1^2 + 2^2 + ... + n^2 =  n(n+1)(2n+1)/6
    cout << "1^2 + 2^2 + ... + n^2: " << (n * (n + 1) * (2 * n + 1)) / 6 << endl;

    // 3, 7, 11, 15 
    // a + .... + b = n(a + b) / 2
    cout << "3 + 7 + 11 + 15: " << (4 * (3 + 15)) / 2 << endl;

    // a + ak + ak^2 + ... + b = (bk - a) / (k - 1)
    // 3 + 6 + 12 + 24 = (24.2 - 3)/(2-1) = 45
    
    // Set theory
    set <int> s1, s2;
    s1.insert(10);
    s1.insert(20);
    s1.insert(30);

    // set s1
    for (auto it = s1.begin(); it != s.end(); it++) {
        cout << *it << " ";
    }
    cout << endl;

    

    return 0;
}
