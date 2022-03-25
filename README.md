# posix_ipc_resources

Transforming to a class
 

Complete - Completed converting into a class 

Progress - Migrating functions into a single file. Added a separated script for testing

Original - First standalone programs after discovering the steps 

Algorithm testing in REPL
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


References:
1. https://stackoverflow.com/questions/17615414/how-to-convert-binary-string-to-normal-string-in-python3
2. https://stackoverflow.com/questions/38883476/how-to-remove-those-x00-x00
3. https://www.geeksforgeeks.org/__init__-in-python/
4. https://docs.python.org/3/library/mmap.html
5. https://semanchuk.com/philip/posix_ipc/
