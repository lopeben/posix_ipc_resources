#!/usr/bin/env python3

import json
from ipc_resources import mmap_shm


def main():
	
	shm = mmap_shm()
	fh = shm.open(shm.READ_ONLY)
	jdata = shm.read(fh)
	
	data = json.loads(jdata)
	print(data['temperature'])
	print(data['humidity'])  



if __name__ == "__main__":
    main() 


