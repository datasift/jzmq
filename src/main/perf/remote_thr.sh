#!/bin/sh
java -classpath "../src/zmq4.jar:zmq4-perf.jar" remote_thr $@
