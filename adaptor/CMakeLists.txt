
include(GenerateExportHeader)
SET(MPI_CXX_SKIP_MPICXX ON)


find_package(ParaView REQUIRED COMPONENTS vtkPVPythonCatalyst)
find_package(MPI REQUIRED)

add_library(dll_adaptor SHARED src/dll_adaptor.cpp)
target_compile_definitions(dll_adaptor PUBLIC  -DOMPI_SKIP_MPICXX -DMPICH_SKIP_MPICXX)
GENERATE_EXPORT_HEADER( dll_adaptor
            BASE_NAME dll_adaptor
            EXPORT_MACRO_NAME DLL_ADAPTOR_EXPORT
            EXPORT_FILE_NAME dll_adaptor_exports.h
)
target_link_libraries(dll_adaptor PUBLIC vtkPVPythonCatalyst) #LINK_PRIVATE
target_link_libraries(dll_adaptor PUBLIC  MPI::MPI_C)

target_include_directories(dll_adaptor PUBLIC
   $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
   $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}/>
   $<INSTALL_INTERFACE:include>
   )
