# Go-FFI Project with Python

This project demonstrates how to use Go's Foreign Function Interface (FFI) to interact with Python. The Go code exports a function that can be called from Python using the `ctypes` library.

## Project Structure

```
/home/sambit/projects/go-ffi
├── build.sh
├── demo.py
├── hello.go
```

### Files

- **hello.go**: Contains the Go code that exports a `Hello` function.
- **build.sh**: A shell script to build the Go shared library.
- **demo.py**: A Python script to demonstrate calling the Go function.

## Steps to Run the Project

1. **Build the Go Shared Library**

   Run the `build.sh` script to compile the Go code into a shared library:

   ```bash
   ./build.sh
   ```

   This will generate a shared library file (e.g., `hello.so`).

2. **Run the Python Script**

   Execute the `demo.py` script to call the Go function from Python:

   ```bash
   python3 demo.py
   ```

## Go Code (`hello.go`)

```go
package main

// #include <stdlib.h>
import "C"

//export Hello
func Hello(name *C.char) *C.char {
	goName := C.GoString(name)
	greeting := "Hello, " + goName + " from Go!"
	return C.CString(greeting)
}

func main() {}
```

## Python Code (`demo.py`)

```python
import ctypes

# Load the shared library
lib = ctypes.CDLL('./hello.so')

# Define the argument and return types for the Hello function
lib.Hello.argtypes = [ctypes.c_char_p]
lib.Hello.restype = ctypes.c_char_p

# Call the Hello function
name = b"World"
result = lib.Hello(name)
print(result.decode('utf-8'))
```

## Build Script (`build.sh`)

```bash
#!/bin/bash

echo "Building Go shared library..."
go build -o hello.so -buildmode=c-shared hello.go
```

## Requirements

- Go (1.16 or later)
- Python (3.x)

## Notes

- Ensure that the `hello.so` file is in the same directory as `demo.py` when running the Python script.
- The `ctypes` library is used in Python to load and interact with the Go shared library.