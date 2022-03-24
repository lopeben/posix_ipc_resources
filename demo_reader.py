#!/usr/bin/env python3

import os
import os.path
import mmap
import posix_ipc
import json

import posix_shm as ps


def main():

    fh = ps.shm_open()
    data = ps.shm_read(fh)
    
    print(data['temperature'])
    print(data['humidity'])  


if __name__ == "__main__":
    main() 