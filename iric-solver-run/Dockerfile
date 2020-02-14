FROM ubuntu:18.04
RUN apt update
RUN apt upgrade -y
COPY local.tar.gz /usr
WORKDIR /usr
RUN tar zxvf local.tar.gz
RUN rm local.tar.gz
RUN ldconfig
RUN mkdir /data
WORKDIR /data
