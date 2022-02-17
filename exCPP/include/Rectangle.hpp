#pragma once


namespace excpp {
    
class Rectangle {

    private:
        int x0, y0, x1, y1;
    public:
        Rectangle(int x0, int y0, int x1, int y1);
        ~Rectangle();
        
        int get_length();
        int get_height();
        int get_area();
        void move (int dx, int dy);
};

}