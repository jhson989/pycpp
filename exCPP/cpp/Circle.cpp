#include "Circle.hpp"


excpp::Circle::Circle(int ix, int iy, int ir): x(ix), y(iy), r(ir) {

}

double excpp::Circle::get_circumference() {
    return excpp::PI * 2 * r;
}

double excpp::Circle::get_area() {
    return excpp::PI * excpp::PI * r;
}