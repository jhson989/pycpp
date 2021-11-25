cmake_minimum_required(VERSION 3.10.2)

# Project information
project ("Fast_PI_calculator"
    VERSION 1.0
    DESCRIPTION "PI Calculator with Monte Carlo method"
    )


include_directories (include)
add_subdirectory(src)