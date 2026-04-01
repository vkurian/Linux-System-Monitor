import os
import time
import psutil



def clear_screen():
        os.system("clear")

def memory():
        vmemory = psutil.virtual_memory()
        print("Total Memory: ", vmemory[0],"byte")
        print("memory available",vmemory[1],"byte")
        print("memory used ", vmemory[3], "byte")
        print("percentage of memory being used", vmemory[2], "%")
def proc():
        p=psutil.Process()
        cpu_percentage=psutil.cpu_percent()

        Name=p.name()
        mem=p.memory_percent()
        print("Name of the Process",Name)
        print("System Cpu Percentage",cpu_percentage)
        print("Memory of the processor",mem)

def download():
        counters=psutil.net_io_counters(pernic=False, nowrap=True)
        old_value=counters.bytes_recv
        time.sleep(1)
        counters=psutil.net_io_counters(pernic=False, nowrap=True)
        new_value=counters.bytes_recv
        print("Upload_speed, {new_value-old_value:.2f} Mbps")
def upload():
        counters=psutil.net_io_counters(pernic=False, nowrap=True)
        old_value=counters.bytes_sent
        time.sleep(1)
        counters=psutil.net_io_counters(pernic=False, nowrap=True)
        new_value=counters.bytes_sent
        print("Upload_speed, {new_value-old_value:.2f} Mbps")
while True:
        clear_screen()
        proc()
        memory()
        download()
        upload()
        break;

