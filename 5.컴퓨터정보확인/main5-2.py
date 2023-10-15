import psutil

cpu_core = psutil.cpu_count(logical=False)
print(f"코어:{cpu_core}개")
print()

memory=psutil.virtual_memory()
memory_total=round(memory.total/1024**3)
print(f"memory:{memory_total}GB")
print()

disk = psutil.disk_partitions()
for p in disk:
    print(p.mountpoint)
    du = psutil.disk_usage(p.mountpoint)
    disk_total=round(du.total/1024**3)
    print(f'disk size:{disk_total}GB')
    print()
    
net = psutil.net_io_counters()
sent=round(net.bytes_sent/1024**2,1)
recv=round(net.bytes_recv/1024**2,1)
print(f'sent:{sent}MB, receive:{recv} MB')

