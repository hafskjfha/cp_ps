#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

inline int readInt() {
    int x = 0;
    char c;
    while ((c = getchar()) < '0' || c > '9');
    do {
        x = x * 10 + (c - '0');
    } while ((c = getchar()) >= '0' && c <= '9');
    return x;
}

int main() {
    int t = readInt();
    for (int case_num = 1; case_num <= t; ++case_num) {
        int n = readInt();
        vector<int> a(n);
        for (int i = 0; i < n; ++i) {
            a[i] = readInt();
        }

        long long c = 0; // Use long long to avoid overflow
        for (int i = 0; i < n; ++i) {
            vector<int> b;
            int l = 0;

            for (int j = i; j < n; ++j) {
                int v = a[j];
                if (b.empty() || b.back() < v) {
                    b.push_back(v);
                    l++;
                } else {
                    auto pos = lower_bound(b.begin(), b.end(), v);
                    *pos = v; // Update the position
                }
                c += l;
            }
        }
        printf("Case #%d: %lld\n", case_num, c);
    }
    return 0;
}
