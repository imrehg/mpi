#!/usr/bin/env python
from mpi4py import MPI
import numpy
import sys

clients = int(sys.argv[1]) if len(sys.argv) > 1 else 5
print "Clients: %d" %clients
start = MPI.Wtime()
comm = MPI.COMM_SELF.Spawn(sys.executable,
                           args=['cpi.py'],
                           maxprocs=clients)

N = numpy.array(100000, 'i')
comm.Bcast([N, MPI.INT], root=MPI.ROOT)
PI = numpy.array(0.0, 'd')
comm.Reduce(None, [PI, MPI.DOUBLE],
            op=MPI.SUM, root=MPI.ROOT)

print "Results from slaves: %.30f" %PI
print "True valiue (numpy): %.30f" %numpy.pi
print "Total time: %fs" %(MPI.Wtime()-start)

comm.Disconnect()
