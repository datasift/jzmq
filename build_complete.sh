#!/bin/bash

if [ ! -n "$1" ]
then
  echo "Usage: build_complete /path/to/libzmq.so"
  exit 1
fi 

LIB_FILE=`basename $1`

# ensure argument is path to libzmq.so
if [[ ! -r "$1" || "$LIB_FILE" != "libzmq.so" ]]
then
  echo "Usage: build_complete /path/to/libzmq.so"
  exit 1
fi

PREFIX="`readlink -f $(dirname $1)/../`"
echo "Using libzmq at: $PREFIX"

# search for libzmq headers
if [[ ! -r "$PREFIX/include/zmq.h" || ! -r "$PREFIX/include/zmq_utils.h" ]]
then
  echo "Unable to find libzmq headers at expected path: $PREFIX/include"
  exit 1
fi

# run autogen.sh if needs be
if [ ! -e "./configure" ]
then
  echo "Generating configure..."
  ./autogen.sh
fi

# drop the first argument so we can pass all remaining args to configure
shift

# build the binaries and JAR
./configure --with-zeromq="$PREFIX" "$@" && make && ln -fs $PREFIX/lib/libzmq.so* ./src/.libs/ && mvn verify

