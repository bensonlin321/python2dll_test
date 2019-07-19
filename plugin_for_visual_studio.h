/* file plugin.h, Windows-friendly version */
//typedef struct { int x, y; } point_t;

/* When including this file from ffibuilder.set_source(), the
   following macro is defined to '__declspec(dllexport)'.  When
   including this file directly from your C program, we define
   it to 'extern __declspec(dllimport)' instead.

   With non-MSVC compilers we simply define it to 'extern'.
   (The 'extern' is needed for sharing global variables;
   functions would be fine without it.  The macros always
   include 'extern': you must not repeat it when using the
   macros later.)
*/

/*#ifndef CFFI_DLLEXPORT
#  if defined(_MSC_VER)
#    define CFFI_DLLEXPORT  extern __declspec(dllimport)
#  else
#    define CFFI_DLLEXPORT  extern
#  endif
#endif*/

extern "C" unsigned char* set_image(unsigned char*);
extern "C" int   test_int();
extern "C" char* test_tensorflow();
extern "C" char* test_char();