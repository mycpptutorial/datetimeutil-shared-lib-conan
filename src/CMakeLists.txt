cmake_minimum_required(VERSION 2.8.12)
project(DatetimeUtilSharedLibConan CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

SET(CMAKE_EXE_LINKER_FLAGS
          "${CMAKE_EXE_LINKER_FLAGS} -Wl,-rpath -Wl,$ORIGIN")

add_library(datetimeutil SHARED datetimeutil.cpp)
install(TARGETS datetimeutil DESTINATION /usr/local/lib)
