cmake_minimum_required(VERSION 2.6)

project (CodingBattle)

set (CMAKE_CXX_STANDARD 11)
set (CMAKE_RUNTIME_OUTPUT_DIRECTORY "./bin")
set (CMAKE_CXX_FLAGS "-O2")

include_directories(
    ../
)

add_executable(coding
    ../main.cpp
)
