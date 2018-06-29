#include <stdio.h>
#include <stdint.h>
int main() {
  for(int64_t a = 1; a < 1000000; a++) {
    for(int64_t b = 1; b < a; b++) {
    	for(int64_t c = 0; c < 10000; c++) {
    		if(a*a*a + b*b*b == c*c*c) {
    			printf("a=%lld b=%lld c=%lld\n", a,b,c);
    		}
    	}
    }
    printf("%lld\n", a);
  }
}