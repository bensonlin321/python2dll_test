# file plugin_build.py
import cffi
import tensorflow as tf
ffibuilder = cffi.FFI()

with open('plugin.h') as f:
    # read plugin.h and pass it to embedding_api(), manually
    # removing the '#' directives and the CFFI_DLLEXPORT
    data = ''.join([line for line in f if not line.startswith('#')])
    data = data.replace('CFFI_DLLEXPORT', '')
    ffibuilder.embedding_api(data)

ffibuilder.set_source("my_plugin", r'''
    #include "plugin.h"
''')

ffibuilder.embedding_init_code("""
    from my_plugin import ffi
    import tensorflow as tf

    @ffi.def_extern()
    def set_image(arr):
        return arr

    @ffi.def_extern()
    def test_tensorflow():
        hello = tf.constant('Hello, TensorFlow!')
        sess = tf.Session()
        temp = sess.run(hello)
        cov_string = str(temp)
        temp = cov_string.encode('ascii')
        output = ffi.new("char[]", temp)
        return output

    @ffi.def_extern()
    def test_int():
        return 18

    @ffi.def_extern()
    def test_char():
        result = "benson"
        temp = result.encode('ascii')
        output = ffi.new("char[]", temp)
        return output
""") 


ffibuilder.compile(target="plugin.*", verbose=True)
# or: ffibuilder.emit_c_code("my_plugin.c")