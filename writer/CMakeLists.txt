include(GenerateExportHeader)
SET(MPI_CXX_SKIP_MPICXX ON)
find_package(MPI REQUIRED)
add_library(dll_writer SHARED src/dll_writer.cpp)
target_compile_definitions(dll_writer PUBLIC -DOMPI_SKIP_MPICXX -DMPICH_SKIP_MPICXX)
GENERATE_EXPORT_HEADER( dll_writer
             BASE_NAME dll_writer
             EXPORT_MACRO_NAME DLL_WRITER_EXPORT
             EXPORT_FILE_NAME dll_writer_exports.h
)
target_link_libraries(dll_writer PUBLIC MPI::MPI_C)
target_include_directories(dll_writer PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}/>
    $<INSTALL_INTERFACE:include>
    )
