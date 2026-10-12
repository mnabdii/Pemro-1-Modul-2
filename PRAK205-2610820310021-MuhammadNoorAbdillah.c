#include <stdio.h>
#include <math.h>

int main() {
    int A, B;
    scanf("%d %d", &A, &B);
    int alas = (int)(sqrt((double)(B * B - A * A)) + 0.5);
    printf("Alas = %d cm\n", alas);
    printf("Tinggi = %d cm\n", A);
    printf("Keliling = %d cm\n", alas + A + B);
    printf("Luas = %d cm^2\n", alas * A / 2);
    return 0;
}