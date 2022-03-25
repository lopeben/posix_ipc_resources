#!/usr/bin/env python3

import json
from mmap_shm import mmap_shm


def main():
	
	shm = mmap_shm()

	fh = shm.shm_open()
	jdata = shm.shm_read(fh)
	data = json.loads(jdata)
    
	print(data['temperature'])
	print(data['humidity'])  



if __name__ == "__main__":
    main() 


