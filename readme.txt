>>> shmem.unlink()
>>> shmem = posix_ipc.SharedMemory('/shard', flags=posix_ipc.O_CREX, mode=0o600, size=0)
>>> os.ftruncate(shmem.fd, 4096)
>>> mmap_object= mmap.mmap(shmem.fd,length=0,access=mmap.ACCESS_WRITE,offset=0)
>>> text='{"json": "string"}'
>>> mmap_object.write(bytes(text,encoding="utf8"))
18
>>> text='{"json": "string2"}'
>>> mmap_object.write(bytes(text,encoding="utf8"))




>>> import posix_ipc
>>> import os
>>> import mmap
>>> 
>>> 
>>> 
>>> shmem = posix_ipc.SharedMemory('/shard', flags=0, mode=0o600, size=0)
>>> os.ftruncate(shmem.fd, 4096)
>>> mmap_object= mmap.mmap(shmem.fd,length=0,access=mmap.ACCESS_READ,offset=0)
>>> mmap_object.read()
