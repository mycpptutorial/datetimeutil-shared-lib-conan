cmake_minimum_required(VERSION 2.8.12)
project(DatetimeUtilSharedLibConan)

link_directories(${CMAKE_CURRENT_BINARY_DIR})

SET(CMAKE_EXE_LINKER_FLAGS
          "${CMAKE_EXE_LINKER_FLAGS} -Wl,-rpath -Wl,$ORIGIN")

add_library(datetimeutil SHARED src/datetimeutil.h src/datetimeutil.cpp)

install(TARGETS datetimeutil DESTINATION /usr/local/lib)
