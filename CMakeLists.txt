CMAKE_MINIMUM_REQUIRED(VERSION 3.10)
PROJECT(alsvinn_insitu C CXX)
SET(CXX_STANDARD 11)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/cmake/Modules/")
#add_subdirectory(writer)
add_subdirectory(adaptor)
#add_subdirectory(standalone)
