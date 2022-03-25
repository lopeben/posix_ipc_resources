#!/usr/bin/env python3

import json
from mmap_shm import mmap_shm


def main():
	
	shm = mmap_shm()

	fh = shm.shm_create()

	data = {}
	data['temperature'] = 27
	data['humidity'] = 65
	jdata = json.dumps(data)

	shm.shm_write(fh, jdata)   


if __name__ == "__main__":
    main() 


