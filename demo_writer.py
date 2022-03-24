#!/usr/bin/env python3

import os
import os.path
import mmap
import posix_ipc
import json

import posix_shm as ps


def main():

    fh = ps.shm_create()

    data = {}
    data['temperature'] = 27
    data['humidity'] = 63

    ps.shm_write(fh, data)   


if __name__ == "__main__":
    main() 


