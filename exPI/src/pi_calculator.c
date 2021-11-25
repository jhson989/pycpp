#include "pi_calculator.h"

double get_PI(int num_iters) {


    const int radius = 10000;
    const int diameter = 10000;
    const int center_x = radius;
    const int center_y = radius;

    int num_in = 0;

    int x, y;
    for (int i=0; i<num_iters; i++) {
        x = rand()%(diameter+1);
        y = rand()%(diameter+1);

        if (  (x-center_x)*(x-center_x) + (y-center_y)*(y-center_y) < radius * radius )
            num_in++;
    }


    return 4.0f * (num_in) / num_iters;
}