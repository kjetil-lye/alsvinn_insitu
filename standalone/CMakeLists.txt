add_executable(standalone src/standalone.cpp)

target_link_libraries(standalone dll_writer)
