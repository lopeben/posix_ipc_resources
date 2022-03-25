#!/usr/bin/env python3

import json
import posix_shm as ps


def main():

    fh = ps.shm_open()
    jdata = ps.shm_read(fh)
    data = json.loads(jdata)
    
    print(data['temperature'])
    print(data['humidity'])  


if __name__ == "__main__":
    main() 
