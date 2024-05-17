cmake_minimum_required(VERSION 3.27)
project(audio_learning_chapter2)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(audio_learning_chapter2
        ieee80.c
        ieee80.h
        portsf.c
        portsf.h
        sf2float.cpp)
add_executable(check check.cpp)
