#!/usr/bin/env python3

import os
import os.path
import mmap
import posix_ipc
import json

SH_PATH = '/dev/shm'
SH_FILENAME = '/shfile'

BUFFER_SIZE = 64


def shm_create():    
    if os.path.exists(SH_PATH + SH_FILENAME):
        os.remove(SH_PATH + SH_FILENAME)

    try:
        shref = posix_ipc.SharedMemory(SH_FILENAME, flags=posix_ipc.O_CREX, mode=0o600, size=0)
        os.ftruncate(shref.fd, BUFFER_SIZE)
    except:
        shref = None

    if not (None == shref):
        shm_handle = mmap.mmap(shref.fd, length=0, access=mmap.ACCESS_WRITE, offset=0)
    else:
        shm_handle = None
 
    shref.close_fd()

    return shm_handle


def shm_write(sh_handle, data):
    json_data = json.dumps(data)
    sh_handle.seek(0x00)
    sh_handle.write(bytes(json_data, encoding="utf8"))


def shm_destroy(sh_handle):
    sh_handle.unlink() 
    os.remove(SH_PATH + SH_FILENAME)   


def main():

    fh = shm_create()

    data = {}
    data['temperature'] = 27
    data['humidity'] = 63

    shm_write(fh, data)    




if __name__ == "__main__":
    main()