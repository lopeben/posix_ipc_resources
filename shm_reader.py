#!/usr/bin/env python3

import posix_ipc
import os
import mmap
import json

SH_PATH = '/dev/shm'
SH_FILENAME = '/shfile'


def shm_open():

    if os.path.exists(SH_PATH + SH_FILENAME):
        shref = posix_ipc.SharedMemory(SH_FILENAME, flags=0, mode=0o600, size=0)
    else:
        shref = None
    
    if (None == shref) :
        shm_handle = None
    else:
        shm_handle = mmap.mmap(shref.fd, length=0, access=mmap.ACCESS_READ, offset=0)

    return shm_handle


def shm_read(shm_handle):
    shm_handle.seek(0x00)
    _text = shm_handle.read().decode('utf8').rstrip('\x00')         
    data = json.loads(_text)
    return data  


def main():

    fh = shm_open()
    data = shm_read(fh)
    
    print(data['temperature'])
    print(data['humidity'])


if __name__ == "__main__":
    main()