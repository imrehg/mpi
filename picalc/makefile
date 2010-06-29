.PHONY: default build test clean

default: run

PYTHON=python
MPIEXEC=mpiexec
NPFLAG= -n

run:
	${MPIEXEC} ${NPFLAG} 1 ${PYTHON} master.py
