FROM ubuntu:18.04
RUN apt update
RUN apt upgrade -y
RUN apt install -y cmake gfortran g++ libcgns-dev libhdf5-dev wget 
WORKDIR /tmp
RUN wget https://github.com/i-RIC/iriclib/archive/v0.2.tar.gz
RUN tar zxvf v0.2.tar.gz
RUN mkdir iriclib-0.2/build
WORKDIR /tmp/iriclib-0.2/build
RUN cmake -D HDF5_LIBRARIES=/usr/lib/x86_64-linux-gnu/hdf5/serial/lib/libhdf5.so ..
RUN make
RUN make install
