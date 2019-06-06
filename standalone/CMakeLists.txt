add_executable(standalone src/standalone.cpp)
find_package(NetCDF REQUIRED)
target_link_libraries(standalone dll_writer ${NETCDF_LIBRARIES})
target_include_directories(standalone PRIVATE ${NETCDF_INCLUDE_DIRS})
