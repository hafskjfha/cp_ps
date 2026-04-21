#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

#define ll long long
#define mod(a, b) (((a) % (b) + (b)) % (b))

typedef struct EEA_RESULT {
	ll gcd;
	ll x;
	ll y;
} EEA_RESULT;


EEA_RESULT extended_gcd_with_while(ll a, ll b) {
	ll s0 = 1, s1 = 0;
	ll t0 = 0, t1 = 1;
	ll q, temp;

	while (b != 0) {
		q = a /b;
		temp = a % b;
		a = b;
		b = temp;

		temp = s1;
		s1 = s0 - q * s1;
		s0 = temp;

		temp = t1;
		t1 = t0 - q * t1;
		t0 = temp;
	}

	EEA_RESULT result;
	result.gcd = a;
	result.x = s0;
	result.y = t0;

	return result;
}

ll modular_inverse(ll a, ll m) {
	EEA_RESULT result = extended_gcd_with_while(a, m);
	if (result.gcd != 1) return -1;

	return mod(result.x, m);
}

int main(void) {
	ll n,a;
    scanf("%lld %lld",&n,&a);
    ll mi = modular_inverse(a,n);
    printf("%lld %lld",n-a,mi);
}