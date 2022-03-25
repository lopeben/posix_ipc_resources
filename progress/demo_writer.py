#!/usr/bin/env python3

import json
import posix_shm as ps


def main():

    fh = ps.shm_create()

    data = {}
    data['temperature'] = 27
    data['humidity'] = 65
    jdata = json.dumps(data)

    ps.shm_write(fh, jdata)   


if __name__ == "__main__":
    main() 


