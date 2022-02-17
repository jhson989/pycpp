#pragma once

namespace excpp {

const double PI = 3.141592;

class Circle {
    private:
        int x, y, r;
    public:
        Circle(int x, int y, int r);
        double get_circumference();
        double get_area();
};

}