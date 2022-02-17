#include "Rectangle.hpp"

excpp::Rectangle::Rectangle(int ix0, int iy0, int ix1, int iy1) : x0(ix0), y0(iy0), x1(ix1), y1(iy1) {

};

excpp::Rectangle::~Rectangle() {

};

int excpp::Rectangle::get_length() {
    return (x1-x0);
}

int excpp::Rectangle::get_height() {
    return (y1-y0);
}

int excpp::Rectangle::get_area() {
    return get_height()*get_length();
}

void excpp::Rectangle::move(int dx, int dy) {
    x0 += dx;
    y0 += dy;
    x1 += dx;
    y1 += dy;
}