#!/usr/bin/env python3

import json
from mmap_shm import mmap_shm


def main():
	
	shm = mmap_shm()

	fh = shm.shm_open()

	data = {}
	data['temperature'] = 27
	data['humidity'] = 61
	jdata = json.dumps(data)

	shm.shm_write(fh, jdata)   


if __name__ == "__main__":
    main() 


