
add_library(piCalculator SHARED pi_calculator.c)

set (
    C_FILES
    pi_calculator.c
)

set (
    CYTHON_FILE 
    pyInterface.pyx
)

file(COPY ${PROJECT_SOURCE_DIR}/setup.py
        DESTINATION ${CMAKE_CURRENT_BINARY_DIR}
)


file(COPY ${CMAKE_CURRENT_SOURCE_DIR}/pyInterface.pyx
        DESTINATION ${CMAKE_CURRENT_BINARY_DIR}
)

add_custom_target(
    cython ALL
    DEPENDS piCalculator
    COMMAND python setup.py build_ext --inplace
    COMMAND python setup.py install --user
)

add_custom_target(
    
)

install(
    TARGETS piCalculator 
    LIBRARY DESTINATION /home/jhson/test/
    )