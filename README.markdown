MPI Ubuntu install
==================

1) Install dependencies:

    sudo apt-get install openmpi-bin mpi-default-dev python-dev libssl-dev

2) Download **mpi4py** from http://code.google.com/p/mpi4py/downloads/list
    For example

    wget http://mpi4py.googlecode.com/files/mpi4py-1.2.1.tar.gz
    tar xzvf mpi4py-1.2.1.tar.gz
    cd mpi4py
    sudo python setup.py install
