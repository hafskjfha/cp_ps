#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define ll long long

int main(void) {
	int n;
	double prev,cur,s=0;
	scanf("%d",&n);
	for (int i = 0;i < n;i++) {
		scanf("%lf",&cur);
		s += cur + (i != 0 ? (prev * (1 - cur) + (1 - prev) * cur) : 0);
		prev = cur;
	}
	printf("%lf",s);
}