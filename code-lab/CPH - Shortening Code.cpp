#include <bits/stdc++.h>
using namespace std;

// Type names
typedef long long ll;
typedef vector <int> vi;
typedef pair<int, int> pi;

// macros
# define F first
# define S second
# define PB push_back
# define MP make_pair

# define SQ(a) (a) * (a)

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    ll a = 10;
    vi vec; // use vi instead of vector<int> 

    vec.PB(19);

    cout << a << endl;
    cout << vec[0] << endl;

    vector <pi> vpi;
    vpi.PB(MP(10, 20));

    cout << vpi[0].first << " -- " << vpi[0].second << endl;
    cout << SQ(10) << endl;    
}
