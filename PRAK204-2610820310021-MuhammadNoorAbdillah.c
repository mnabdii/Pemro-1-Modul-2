#include <stdio.h>

int main() {
    double r, t, pi = 22.0 / 7.0;
    scanf("%lf %lf", &r, &t);
    printf("Volume = %.2f\n", pi * r * r * t);
    printf("Luas = %.2f\n", 2 * pi * r * (r + t));
    printf("Keliling = %.2f\n", 2 * pi * r);
    return 0;
}