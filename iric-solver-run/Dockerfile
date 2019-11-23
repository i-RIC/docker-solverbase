FROM ubuntu:18.04
RUN apt update
RUN apt upgrade -y
RUN apt install -y libcgns3.3 libhdf5-100
COPY libiriclib.so /usr/local/lib/
RUN chmod a+x /usr/local/lib/libiriclib.so
RUN ldconfig
RUN mkdir /data
WORKDIR /data
# COPY unittests_cgnsfile /data
