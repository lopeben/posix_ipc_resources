#!/usr/bin/env python3

import json
from ipc_resources import mmap_shm


def main():
	
	shm = mmap_shm() 
	fh = shm.create()


if __name__ == "__main__":
    main() 


