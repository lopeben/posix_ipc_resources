import os
import os.path
import mmap
import posix_ipc

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
	

def shm_destroy():
	os.remove(SH_PATH + SH_FILENAME)


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
	
	
def shm_close(shm_handle):
	shm_handle.close()


def shm_read(shm_handle):
	shm_handle.seek(0x00)
	data = shm_handle.read().decode('utf8').rstrip('\x00')         
	return data  


def shm_write(shm_handle, data):
	shm_handle.seek(0x00)
	shm_handle.write(bytes(data, encoding="utf8"))
