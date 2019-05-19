cmake_minimum_required(VERSION 2.8.12)
project(DatetimeUtilSharedLibConan CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_library(datetimeutil SHARED datetimeutil.cpp)
