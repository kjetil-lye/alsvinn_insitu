set(CMAKE_CXX_COMPILER "/opt/cray/pe/craype/2.5.15/bin/CC")
set(CMAKE_CXX_COMPILER_ARG1 "")
set(CMAKE_CXX_COMPILER_ID "GNU")
set(CMAKE_CXX_COMPILER_VERSION "6.2.0")
set(CMAKE_CXX_COMPILER_VERSION_INTERNAL "")
set(CMAKE_CXX_COMPILER_WRAPPER "CrayPrgEnv")
set(CMAKE_CXX_STANDARD_COMPUTED_DEFAULT "14")
set(CMAKE_CXX_COMPILE_FEATURES "cxx_std_98;cxx_template_template_parameters;cxx_std_11;cxx_alias_templates;cxx_alignas;cxx_alignof;cxx_attributes;cxx_auto_type;cxx_constexpr;cxx_decltype;cxx_decltype_incomplete_return_types;cxx_default_function_template_args;cxx_defaulted_functions;cxx_defaulted_move_initializers;cxx_delegating_constructors;cxx_deleted_functions;cxx_enum_forward_declarations;cxx_explicit_conversions;cxx_extended_friend_declarations;cxx_extern_templates;cxx_final;cxx_func_identifier;cxx_generalized_initializers;cxx_inheriting_constructors;cxx_inline_namespaces;cxx_lambdas;cxx_local_type_template_args;cxx_long_long_type;cxx_noexcept;cxx_nonstatic_member_init;cxx_nullptr;cxx_override;cxx_range_for;cxx_raw_string_literals;cxx_reference_qualified_functions;cxx_right_angle_brackets;cxx_rvalue_references;cxx_sizeof_member;cxx_static_assert;cxx_strong_enums;cxx_thread_local;cxx_trailing_return_types;cxx_unicode_literals;cxx_uniform_initialization;cxx_unrestricted_unions;cxx_user_literals;cxx_variadic_macros;cxx_variadic_templates;cxx_std_14;cxx_aggregate_default_initializers;cxx_attribute_deprecated;cxx_binary_literals;cxx_contextual_conversions;cxx_decltype_auto;cxx_digit_separators;cxx_generic_lambdas;cxx_lambda_init_captures;cxx_relaxed_constexpr;cxx_return_type_deduction;cxx_variable_templates;cxx_std_17")
set(CMAKE_CXX98_COMPILE_FEATURES "cxx_std_98;cxx_template_template_parameters")
set(CMAKE_CXX11_COMPILE_FEATURES "cxx_std_11;cxx_alias_templates;cxx_alignas;cxx_alignof;cxx_attributes;cxx_auto_type;cxx_constexpr;cxx_decltype;cxx_decltype_incomplete_return_types;cxx_default_function_template_args;cxx_defaulted_functions;cxx_defaulted_move_initializers;cxx_delegating_constructors;cxx_deleted_functions;cxx_enum_forward_declarations;cxx_explicit_conversions;cxx_extended_friend_declarations;cxx_extern_templates;cxx_final;cxx_func_identifier;cxx_generalized_initializers;cxx_inheriting_constructors;cxx_inline_namespaces;cxx_lambdas;cxx_local_type_template_args;cxx_long_long_type;cxx_noexcept;cxx_nonstatic_member_init;cxx_nullptr;cxx_override;cxx_range_for;cxx_raw_string_literals;cxx_reference_qualified_functions;cxx_right_angle_brackets;cxx_rvalue_references;cxx_sizeof_member;cxx_static_assert;cxx_strong_enums;cxx_thread_local;cxx_trailing_return_types;cxx_unicode_literals;cxx_uniform_initialization;cxx_unrestricted_unions;cxx_user_literals;cxx_variadic_macros;cxx_variadic_templates")
set(CMAKE_CXX14_COMPILE_FEATURES "cxx_std_14;cxx_aggregate_default_initializers;cxx_attribute_deprecated;cxx_binary_literals;cxx_contextual_conversions;cxx_decltype_auto;cxx_digit_separators;cxx_generic_lambdas;cxx_lambda_init_captures;cxx_relaxed_constexpr;cxx_return_type_deduction;cxx_variable_templates")
set(CMAKE_CXX17_COMPILE_FEATURES "cxx_std_17")
set(CMAKE_CXX20_COMPILE_FEATURES "")

set(CMAKE_CXX_PLATFORM_ID "Linux")
set(CMAKE_CXX_SIMULATE_ID "")
set(CMAKE_CXX_SIMULATE_VERSION "")



set(CMAKE_AR "/usr/bin/ar")
set(CMAKE_CXX_COMPILER_AR "/usr/bin/gcc-ar")
set(CMAKE_RANLIB "/usr/bin/ranlib")
set(CMAKE_CXX_COMPILER_RANLIB "/usr/bin/gcc-ranlib")
set(CMAKE_LINKER "/apps/daint/UES/xalt/0.7.6/bin/ld")
set(CMAKE_MT "")
set(CMAKE_COMPILER_IS_GNUCXX 1)
set(CMAKE_CXX_COMPILER_LOADED 1)
set(CMAKE_CXX_COMPILER_WORKS TRUE)
set(CMAKE_CXX_ABI_COMPILED TRUE)
set(CMAKE_COMPILER_IS_MINGW )
set(CMAKE_COMPILER_IS_CYGWIN )
if(CMAKE_COMPILER_IS_CYGWIN)
  set(CYGWIN 1)
  set(UNIX 1)
endif()

set(CMAKE_CXX_COMPILER_ENV_VAR "CXX")

if(CMAKE_COMPILER_IS_MINGW)
  set(MINGW 1)
endif()
set(CMAKE_CXX_COMPILER_ID_RUN 1)
set(CMAKE_CXX_IGNORE_EXTENSIONS inl;h;hpp;HPP;H;o;O;obj;OBJ;def;DEF;rc;RC)
set(CMAKE_CXX_SOURCE_FILE_EXTENSIONS C;M;c++;cc;cpp;cxx;mm;CPP)
set(CMAKE_CXX_LINKER_PREFERENCE 30)
set(CMAKE_CXX_LINKER_PREFERENCE_PROPAGATES 1)

# Save compiler ABI information.
set(CMAKE_CXX_SIZEOF_DATA_PTR "8")
set(CMAKE_CXX_COMPILER_ABI "ELF")
set(CMAKE_CXX_LIBRARY_ARCHITECTURE "")

if(CMAKE_CXX_SIZEOF_DATA_PTR)
  set(CMAKE_SIZEOF_VOID_P "${CMAKE_CXX_SIZEOF_DATA_PTR}")
endif()

if(CMAKE_CXX_COMPILER_ABI)
  set(CMAKE_INTERNAL_PLATFORM_ABI "${CMAKE_CXX_COMPILER_ABI}")
endif()

if(CMAKE_CXX_LIBRARY_ARCHITECTURE)
  set(CMAKE_LIBRARY_ARCHITECTURE "")
endif()

set(CMAKE_CXX_CL_SHOWINCLUDES_PREFIX "")
if(CMAKE_CXX_CL_SHOWINCLUDES_PREFIX)
  set(CMAKE_CL_SHOWINCLUDES_PREFIX "${CMAKE_CXX_CL_SHOWINCLUDES_PREFIX}")
endif()





set(CMAKE_CXX_IMPLICIT_INCLUDE_DIRECTORIES "/opt/cray/pe/netcdf/4.6.1.2/gnu/6.1/include;/opt/cray/pe/hdf5/1.10.2.0/gnu/6.1/include;/opt/cray/pe/libsci/18.07.1/GNU/6.1/x86_64/include;/opt/cray/pe/mpt/7.7.2/gni/mpich-gnu/5.1/include;/opt/nvidia/cudatoolkit9.2/9.2.148_3.19-6.0.7.1_2.1__g3d9acc8/include;/opt/nvidia/cudatoolkit9.2/9.2.148_3.19-6.0.7.1_2.1__g3d9acc8/extras/CUPTI/include;/opt/nvidia/cudatoolkit9.2/9.2.148_3.19-6.0.7.1_2.1__g3d9acc8/nvvm/include;/opt/cray/rca/2.2.18-6.0.7.1_5.48__g2aa4f39.ari/include;/opt/cray/alps/6.6.43-6.0.7.1_5.46__ga796da32.ari/include;/opt/cray/xpmem/2.2.15-6.0.7.1_5.11__g7549d06.ari/include;/opt/cray/gni-headers/5.0.12.0-6.0.7.1_3.11__g3b1768f.ari/include;/opt/cray/pe/pmi/5.0.14/include;/opt/cray/ugni/6.0.14.0-6.0.7.1_3.13__gea11d3d.ari/include;/opt/cray/udreg/2.3.2-6.0.7.1_5.13__g5196236.ari/include;/opt/cray/wlm_detect/1.3.3-6.0.7.1_5.6__g7109084.ari/include;/opt/cray/krca/2.2.4-6.0.7.1_5.44__g8505b97.ari/include;/opt/cray-hss-devel/8.0.0/include;/apps/daint/UES/jenkins/6.0.UP07/gpu/easybuild/software/Boost/1.67.0-CrayGNU-18.08-python3/include;/apps/daint/UES/jenkins/6.0.UP07/gpu/easybuild/software/zlib/1.2.11-CrayGNU-18.08/include;/apps/daint/UES/jenkins/6.0.UP07/gpu/easybuild/software/bzip2/1.0.6-CrayGNU-18.08/include;/opt/gcc/6.2.0/snos/include/g++;/opt/gcc/6.2.0/snos/include/g++/x86_64-suse-linux;/opt/gcc/6.2.0/snos/include/g++/backward;/opt/gcc/6.2.0/snos/lib/gcc/x86_64-suse-linux/6.2.0/include;/usr/local/include;/opt/gcc/6.2.0/snos/include;/opt/gcc/6.2.0/snos/lib/gcc/x86_64-suse-linux/6.2.0/include-fixed;/usr/include")
set(CMAKE_CXX_IMPLICIT_LINK_LIBRARIES "cupti;cudart;cuda;AtpSigHandler;AtpSigHCommData;rca;netcdf_c++4;netcdf;hdf5_hl;hdf5;hdf5_hl_cpp;hdf5_cpp;sci_gnu_61_mpi;sci_gnu_61;mpich_gnu_51;mpichcxx_gnu_51;gfortran;quadmath;mvec;m;pthread;stdc++;m;gcc_s;gcc;c;gcc_s;gcc")
set(CMAKE_CXX_IMPLICIT_LINK_DIRECTORIES "/opt/cray/pe/netcdf/4.6.1.2/gnu/6.1/lib;/opt/cray/pe/hdf5/1.10.2.0/gnu/6.1/lib;/opt/cray/pe/libsci/18.07.1/GNU/6.1/x86_64/lib;/opt/cray/dmapp/default/lib64;/opt/cray/pe/mpt/7.7.2/gni/mpich-gnu/5.1/lib;/opt/nvidia/cudatoolkit9.2/9.2.148_3.19-6.0.7.1_2.1__g3d9acc8/lib64;/opt/nvidia/cudatoolkit9.2/9.2.148_3.19-6.0.7.1_2.1__g3d9acc8/extras/CUPTI/lib64;/opt/nvidia/cudatoolkit9.2/9.2.148_3.19-6.0.7.1_2.1__g3d9acc8/nvvm/lib64;/opt/cray/nvidia/default/lib64;/opt/cray/rca/2.2.18-6.0.7.1_5.48__g2aa4f39.ari/lib64;/opt/cray/pe/atp/2.1.2/libApp;/opt/gcc/6.2.0/snos/lib/gcc/x86_64-suse-linux/6.2.0;/opt/gcc/6.2.0/snos/lib64;/lib64;/usr/lib64;/apps/daint/UES/jenkins/6.0.UP07/gpu/easybuild/software/Boost/1.67.0-CrayGNU-18.08-python3/lib;/apps/daint/UES/jenkins/6.0.UP07/gpu/easybuild/software/zlib/1.2.11-CrayGNU-18.08/lib;/apps/daint/UES/jenkins/6.0.UP07/gpu/easybuild/software/bzip2/1.0.6-CrayGNU-18.08/lib;/opt/gcc/6.2.0/snos/lib")
set(CMAKE_CXX_IMPLICIT_LINK_FRAMEWORK_DIRECTORIES "")
