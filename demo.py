import ctypes
import os

# Load the shared library.
# The path might need to be adjusted based on your OS and where the library is.
if os.name == 'nt':  # Windows
    libhello = ctypes.CDLL("./libhello.dll")
else:  # Linux or macOS
    libhello = ctypes.CDLL("./libhello.so")

# Define the function signature for the Go function 'Hello'.
# It takes a C string (char pointer) and returns a C string (char pointer).
libhello.Hello.argtypes = [ctypes.c_char_p]
libhello.Hello.restype = ctypes.c_char_p

# Prepare the argument to be passed to the Go function.
name_to_greet = "Python User"
c_name = ctypes.c_char_p(name_to_greet.encode('utf-8'))

# Call the Go function.
result_ptr = libhello.Hello(c_name)

# Convert the C string result back to a Python string.
# ctypes.string_at() creates a Python bytes object from the C string pointer.
# .decode('utf-8') decodes the bytes to a Python string.
result_bytes = ctypes.string_at(result_ptr)
greeting_from_go = result_bytes.decode('utf-8')

# Print the result.
print(greeting_from_go)