# Dockerfile for building images to build / run iRIC solvers

This repository contains Dockerfiles to build images to build or run iRIC solvers

## Requirements

* Python >= 3.6
* Docker

## How to build

```
python3 build_images.py
```

## Built images

This will build the two images below:

* iric/solver-build
* iric/solver-run

### iric/solver-build

This is the image to build solvers.
The following libraries and programs are instaled:

* Compilers (gcc, g++, gfortran)
* hdf5, cgnslib library in /usr/lib/x86_64_linux-gnu
* iriclib library in /usr/local/lib

You can build solvers using this image.

### iric/solver-run

This is the image to run solvers.
The following libraries are installed.

* hdf5, cgnslib library in /usr/lib/x86_64_linux-gnu (only runtimes, no headers)
* iriclib library in /usr/local/lib

We recommend this image to use this image, because this is much smaller than iric/solver-build.

## How to build image to run models

TODO: add description here
