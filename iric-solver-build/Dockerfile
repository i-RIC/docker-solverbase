FROM ubuntu:16.04
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y gcc
RUN apt-get install -y g++
RUN apt-get install -y gfortran
RUN apt-get install -y make
RUN apt-get install -y wget
RUN apt-get install -y cmake
WORKDIR /tmp
RUN wget https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-1.8/hdf5-1.8.14/src/hdf5-1.8.14.tar.gz
RUN tar zxvf hdf5-1.8.14.tar.gz
RUN mkdir /tmp/hdf5-1.8.14/build
WORKDIR /tmp/hdf5-1.8.14/build
RUN cmake -D BUILD_SHARED_LIBS:BOOL=ON ..
RUN make
RUN make install
WORKDIR /tmp
RUN rm -rf hdf5-1.8.14
RUN rm hdf5-1.8.14.tar.gz

RUN wget https://github.com/CGNS/CGNS/archive/v3.2.1.tar.gz
RUN tar zxvf v3.2.1.tar.gz
RUN mkdir /tmp/CGNS-3.2.1/build
WORKDIR /tmp/CGNS-3.2.1/build
RUN cmake -D CGNS_ENABLE_FORTRAN:BOOL=ON -D CGNS_ENABLE_HDF5:BOOL=ON ..
RUN make install
WORKDIR /tmp
RUN rm -rf CGNS-3.2.1
RUN rm v3.2.1.tar.gz
RUN sed -i -e "s/^c/\!/g" /usr/local/include/cgnslib_f.h

RUN wget https://github.com/i-RIC/iriclib/archive/v0.2.tar.gz
RUN tar zxvf v0.2.tar.gz
RUN mkdir iriclib-0.2/build
WORKDIR /tmp/iriclib-0.2/build
RUN cmake -D HDF5_LIBRARIES=/usr/local/lib/libhdf5.so ..
RUN make
RUN make install
WORKDIR /tmp
RUN rm -rf iriclib-0.2
RUN rm v0.2.tar.gz
RUN ldconfig
WORKDIR /usr
RUN tar zcvf /tmp/local.tar.gz local
RUN mkdir /data
WORKDIR /data
