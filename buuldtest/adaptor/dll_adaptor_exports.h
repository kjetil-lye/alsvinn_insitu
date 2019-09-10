
#ifndef DLL_ADAPTOR_EXPORT_H
#define DLL_ADAPTOR_EXPORT_H

#ifdef DLL_ADAPTOR_STATIC_DEFINE
#  define DLL_ADAPTOR_EXPORT
#  define DLL_ADAPTOR_NO_EXPORT
#else
#  ifndef DLL_ADAPTOR_EXPORT
#    ifdef dll_adaptor_EXPORTS
        /* We are building this library */
#      define DLL_ADAPTOR_EXPORT __attribute__((visibility("default")))
#    else
        /* We are using this library */
#      define DLL_ADAPTOR_EXPORT __attribute__((visibility("default")))
#    endif
#  endif

#  ifndef DLL_ADAPTOR_NO_EXPORT
#    define DLL_ADAPTOR_NO_EXPORT __attribute__((visibility("hidden")))
#  endif
#endif

#ifndef DLL_ADAPTOR_DEPRECATED
#  define DLL_ADAPTOR_DEPRECATED __attribute__ ((__deprecated__))
#endif

#ifndef DLL_ADAPTOR_DEPRECATED_EXPORT
#  define DLL_ADAPTOR_DEPRECATED_EXPORT DLL_ADAPTOR_EXPORT DLL_ADAPTOR_DEPRECATED
#endif

#ifndef DLL_ADAPTOR_DEPRECATED_NO_EXPORT
#  define DLL_ADAPTOR_DEPRECATED_NO_EXPORT DLL_ADAPTOR_NO_EXPORT DLL_ADAPTOR_DEPRECATED
#endif

#if 0 /* DEFINE_NO_DEPRECATED */
#  ifndef DLL_ADAPTOR_NO_DEPRECATED
#    define DLL_ADAPTOR_NO_DEPRECATED
#  endif
#endif

#endif /* DLL_ADAPTOR_EXPORT_H */
