import random
from mpi4py import MPI

def compute_pi(nsamples):
    comm = MPI.COMM_WORLD
    rank, size = comm.Get_rank(), comm.Get_size()
    print "Processor %d: %s" %(rank, MPI.Get_processor_name())

    inside_circle_cnt = 0
    for i in xrange(rank, nsamples, size):
        x = random.random()
        y = random.random()
        if ((x*x) + (y*y) < 1.0):
            inside_circle_cnt += 1

    pi = (4.0) * comm.allreduce(inside_circle_cnt, MPI.SUM) / nsamples
    return pi

if __name__ == "__main__":
    start = MPI.Wtime()
    pi = compute_pi(5000000)
    if MPI.COMM_WORLD.Get_rank() == 0:
        print "Pi is %.15f" %pi
        print "Totaltime: %f" %(MPI.Wtime()-start)
