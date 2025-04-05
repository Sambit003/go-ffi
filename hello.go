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
