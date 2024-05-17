cmake_minimum_required(VERSION 3.27)
project(audio_learning)

set(CMAKE_CXX_STANDARD 17)

add_executable(audio_learning main.cpp)

add_executable(audio_learning_decay fork.cpp)

add_executable(audio_learning_binary raw_binary_fork.cpp)
