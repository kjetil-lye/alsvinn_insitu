set(CMAKE_C_COMPILER "/opt/cray/pe/craype/2.5.15/bin/cc")
set(CMAKE_C_COMPILER_ARG1 "")
set(CMAKE_C_COMPILER_ID "GNU")
set(CMAKE_C_COMPILER_VERSION "6.2.0")
set(CMAKE_C_COMPILER_VERSION_INTERNAL "")
set(CMAKE_C_COMPILER_WRAPPER "CrayPrgEnv")
set(CMAKE_C_STANDARD_COMPUTED_DEFAULT "11")
set(CMAKE_C_COMPILE_FEATURES "c_std_90;c_function_prototypes;c_std_99;c_restrict;c_variadic_macros;c_std_11;c_static_assert")
set(CMAKE_C90_COMPILE_FEATURES "c_std_90;c_function_prototypes")
set(CMAKE_C99_COMPILE_FEATURES "c_std_99;c_restrict;c_variadic_macros")
set(CMAKE_C11_COMPILE_FEATURES "c_std_11;c_static_assert")

set(CMAKE_C_PLATFORM_ID "Linux")
set(CMAKE_C_SIMULATE_ID "")
set(CMAKE_C_SIMULATE_VERSION "")



set(CMAKE_AR "/usr/bin/ar")
set(CMAKE_C_COMPILER_AR "/usr/bin/gcc-ar")
set(CMAKE_RANLIB "/usr/bin/ranlib")
set(CMAKE_C_COMPILER_RANLIB "/usr/bin/gcc-ranlib")
set(CMAKE_LINKER "/apps/daint/UES/xalt/0.7.6/bin/ld")
set(CMAKE_MT "")
set(CMAKE_COMPILER_IS_GNUCC 1)
set(CMAKE_C_COMPILER_LOADED 1)
set(CMAKE_C_COMPILER_WORKS TRUE)
set(CMAKE_C_ABI_COMPILED TRUE)
set(CMAKE_COMPILER_IS_MINGW )
set(CMAKE_COMPILER_IS_CYGWIN )
if(CMAKE_COMPILER_IS_CYGWIN)
  set(CYGWIN 1)
  set(UNIX 1)
endif()

set(CMAKE_C_COMPILER_ENV_VAR "CC")

if(CMAKE_COMPILER_IS_MINGW)
  set(MINGW 1)
endif()
set(CMAKE_C_COMPILER_ID_RUN 1)
set(CMAKE_C_SOURCE_FILE_EXTENSIONS c;m)
set(CMAKE_C_IGNORE_EXTENSIONS h;H;o;O;obj;OBJ;def;DEF;rc;RC)
set(CMAKE_C_LINKER_PREFERENCE 10)

# Save compiler ABI information.
set(CMAKE_C_SIZEOF_DATA_PTR "8")
set(CMAKE_C_COMPILER_ABI "ELF")
set(CMAKE_C_LIBRARY_ARCHITECTURE "")

if(CMAKE_C_SIZEOF_DATA_PTR)
  set(CMAKE_SIZEOF_VOID_P "${CMAKE_C_SIZEOF_DATA_PTR}")
endif()

if(CMAKE_C_COMPILER_ABI)
  set(CMAKE_INTERNAL_PLATFORM_ABI "${CMAKE_C_COMPILER_ABI}")
endif()

if(CMAKE_C_LIBRARY_ARCHITECTURE)
  set(CMAKE_LIBRARY_ARCHITECTURE "")
endif()

set(CMAKE_C_CL_SHOWINCLUDES_PREFIX "")
if(CMAKE_C_CL_SHOWINCLUDES_PREFIX)
  set(CMAKE_CL_SHOWINCLUDES_PREFIX "${CMAKE_C_CL_SHOWINCLUDES_PREFIX}")
endif()





set(CMAKE_C_IMPLICIT_INCLUDE_DIRECTORIES "/opt/cray/pe/netcdf/4.6.1.2/gnu/6.1/include;/opt/cray/pe/hdf5/1.10.2.0/gnu/6.1/include;/opt/cray/pe/libsci/18.07.1/GNU/6.1/x86_64/include;/opt/cray/pe/mpt/7.7.2/gni/mpich-gnu/5.1/include;/opt/nvidia/cudatoolkit9.2/9.2.148_3.19-6.0.7.1_2.1__g3d9acc8/include;/opt/nvidia/cudatoolkit9.2/9.2.148_3.19-6.0.7.1_2.1__g3d9acc8/extras/CUPTI/include;/opt/nvidia/cudatoolkit9.2/9.2.148_3.19-6.0.7.1_2.1__g3d9acc8/nvvm/include;/opt/cray/rca/2.2.18-6.0.7.1_5.48__g2aa4f39.ari/include;/opt/cray/alps/6.6.43-6.0.7.1_5.46__ga796da32.ari/include;/opt/cray/xpmem/2.2.15-6.0.7.1_5.11__g7549d06.ari/include;/opt/cray/gni-headers/5.0.12.0-6.0.7.1_3.11__g3b1768f.ari/include;/opt/cray/pe/pmi/5.0.14/include;/opt/cray/ugni/6.0.14.0-6.0.7.1_3.13__gea11d3d.ari/include;/opt/cray/udreg/2.3.2-6.0.7.1_5.13__g5196236.ari/include;/opt/cray/wlm_detect/1.3.3-6.0.7.1_5.6__g7109084.ari/include;/opt/cray/krca/2.2.4-6.0.7.1_5.44__g8505b97.ari/include;/opt/cray-hss-devel/8.0.0/include;/apps/daint/UES/jenkins/6.0.UP07/gpu/easybuild/software/Boost/1.67.0-CrayGNU-18.08-python3/include;/apps/daint/UES/jenkins/6.0.UP07/gpu/easybuild/software/zlib/1.2.11-CrayGNU-18.08/include;/apps/daint/UES/jenkins/6.0.UP07/gpu/easybuild/software/bzip2/1.0.6-CrayGNU-18.08/include;/opt/gcc/6.2.0/snos/lib/gcc/x86_64-suse-linux/6.2.0/include;/usr/local/include;/opt/gcc/6.2.0/snos/include;/opt/gcc/6.2.0/snos/lib/gcc/x86_64-suse-linux/6.2.0/include-fixed;/usr/include")
set(CMAKE_C_IMPLICIT_LINK_LIBRARIES "cupti;cudart;cuda;AtpSigHandler;AtpSigHCommData;rca;netcdf;hdf5_hl;hdf5;sci_gnu_61_mpi;sci_gnu_61;mpich_gnu_51;gfortran;quadmath;mvec;m;pthread;gcc;gcc_s;c;gcc;gcc_s")
set(CMAKE_C_IMPLICIT_LINK_DIRECTORIES "/opt/cray/pe/netcdf/4.6.1.2/gnu/6.1/lib;/opt/cray/pe/hdf5/1.10.2.0/gnu/6.1/lib;/opt/cray/pe/libsci/18.07.1/GNU/6.1/x86_64/lib;/opt/cray/dmapp/default/lib64;/opt/cray/pe/mpt/7.7.2/gni/mpich-gnu/5.1/lib;/opt/nvidia/cudatoolkit9.2/9.2.148_3.19-6.0.7.1_2.1__g3d9acc8/lib64;/opt/nvidia/cudatoolkit9.2/9.2.148_3.19-6.0.7.1_2.1__g3d9acc8/extras/CUPTI/lib64;/opt/nvidia/cudatoolkit9.2/9.2.148_3.19-6.0.7.1_2.1__g3d9acc8/nvvm/lib64;/opt/cray/nvidia/default/lib64;/opt/cray/rca/2.2.18-6.0.7.1_5.48__g2aa4f39.ari/lib64;/opt/cray/pe/atp/2.1.2/libApp;/opt/gcc/6.2.0/snos/lib/gcc/x86_64-suse-linux/6.2.0;/opt/gcc/6.2.0/snos/lib64;/lib64;/usr/lib64;/apps/daint/UES/jenkins/6.0.UP07/gpu/easybuild/software/Boost/1.67.0-CrayGNU-18.08-python3/lib;/apps/daint/UES/jenkins/6.0.UP07/gpu/easybuild/software/zlib/1.2.11-CrayGNU-18.08/lib;/apps/daint/UES/jenkins/6.0.UP07/gpu/easybuild/software/bzip2/1.0.6-CrayGNU-18.08/lib;/opt/gcc/6.2.0/snos/lib")
set(CMAKE_C_IMPLICIT_LINK_FRAMEWORK_DIRECTORIES "")
