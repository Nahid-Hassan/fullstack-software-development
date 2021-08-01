#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    // read file
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdin);

    // Input and Ouput
    int a, b;
    string x;

    cin >> a >> b >> x;
    cout << a << " " << b << " " << x << "\n";

    // printf() and scanf(); is bit faster than cin and cout.
    // "\n" is faster than endl;

    // get whole line
    cin.ignore(); // ignore new line 
    string s;
    getline(cin, s);
    cout << s << endl;

    // if the amount of data is unkown while loop is helpful
    // while (cin >> x) {
    //     cout << x;
    // }

    // Working with numbers
    // int a = -2^31 .... 2^32 - 1 (10**9)
    // long long b = -2^63 .... 2^63 - 1(10**18)

    // error 
    int num = 123456789;
    cout << num << endl;
    // long long res = num * num;  // num * num return int value not long long
    // solution
    long long res = (long long) num * num; // type casting

    // __int128_t c = 2323232; (range(-10^38, 10^38)) 

    return 0;
}