#!/bin/bash

# Build the Go code as a C-shared library
go build -buildmode=c-shared -o libhello.so hello.go

# Make the script executable
chmod +x build.sh
