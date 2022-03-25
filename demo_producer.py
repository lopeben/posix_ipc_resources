#!/usr/bin/env python3

import json
from ipc_resources import mmap_shm


def main():
	
	
	data = {}
	data['temperature'] = 30
	data['humidity'] = 65
	jdata = json.dumps(data)
	
	
	shm = mmap_shm()
	fh = shm.open(shm.WRITE_ONLY)
	shm.write(fh, jdata)
	
	
	print("Wrote temperature: {0}".format(data['temperature']))   
	print("Wrote humidity: {0}".format(data['humidity']))   


if __name__ == "__main__":
    main() 


