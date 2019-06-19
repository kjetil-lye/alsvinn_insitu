
#ifndef DLL_WRITER_EXPORT_H
#define DLL_WRITER_EXPORT_H

#ifdef DLL_WRITER_STATIC_DEFINE
#  define DLL_WRITER_EXPORT
#  define DLL_WRITER_NO_EXPORT
#else
#  ifndef DLL_WRITER_EXPORT
#    ifdef dll_writer_EXPORTS
        /* We are building this library */
#      define DLL_WRITER_EXPORT __attribute__((visibility("default")))
#    else
        /* We are using this library */
#      define DLL_WRITER_EXPORT __attribute__((visibility("default")))
#    endif
#  endif

#  ifndef DLL_WRITER_NO_EXPORT
#    define DLL_WRITER_NO_EXPORT __attribute__((visibility("hidden")))
#  endif
#endif

#ifndef DLL_WRITER_DEPRECATED
#  define DLL_WRITER_DEPRECATED __attribute__ ((__deprecated__))
#endif

#ifndef DLL_WRITER_DEPRECATED_EXPORT
#  define DLL_WRITER_DEPRECATED_EXPORT DLL_WRITER_EXPORT DLL_WRITER_DEPRECATED
#endif

#ifndef DLL_WRITER_DEPRECATED_NO_EXPORT
#  define DLL_WRITER_DEPRECATED_NO_EXPORT DLL_WRITER_NO_EXPORT DLL_WRITER_DEPRECATED
#endif

#if 0 /* DEFINE_NO_DEPRECATED */
#  ifndef DLL_WRITER_NO_DEPRECATED
#    define DLL_WRITER_NO_DEPRECATED
#  endif
#endif

#endif
