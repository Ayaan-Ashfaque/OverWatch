import time
import psutil
import platform
import subprocess
import inspect 
import sys


#os
def run_time():
    return f"{(((time.time())- (psutil.boot_time()))/60/60,2)} hrs"

def os():
    return f"{platform.system()} {platform.release()} {platform.version()} {platform.machine()} {platform.architecture()}"




#CPU
def processor_name():
   return subprocess.check_output(["powershell", "-Command", "Get-CimInstance Win32_Processor | Select-Object -ExpandProperty Name"],text=True).strip()


def cpu_physical_cores():
    return (psutil.cpu_count(logical=False))

def cpu_logical_cores():
    return (psutil.cpu_count(logical=True))


def cpu_usage():
    return f"{psutil.cpu_percent(interval=1)}"


def cpu_freq_current():
        return f"{psutil.cpu_freq().current}MHz"

def cpu_freq_max():
    return f"{psutil.cpu_freq().max}MHz"

def cpu_freq_min():
    return f"{psutil.cpu_freq().min}MHz"


#RAM

def total_ram():
    return f'{(psutil.virtual_memory().total / (1024**3)):.2f} GB'

def ram_usage():
    return f"{psutil.virtual_memory().percent}"


#STORAGE

def total_disk():
    return f'{ (psutil.disk_usage("c:\\").total / (1024**3)):.2f}GB'



def used_disk_percent():
    return f'{psutil.disk_usage("c:\\").percent}'


#GPU

def gpu_model():
    return subprocess.check_output(["nvidia-smi", "--query-gpu=name", "--format=csv,noheader"],text=True).strip()


def gpu_vram_tot():
    return f"{int(subprocess.check_output('nvidia-smi --query-gpu=memory.total --format=csv,noheader,nounits',encoding='utf-8').strip())/ (1024)} GB"


def gpu_vram_usage():
    return round((lambda x: x[0] / x[1] * 100)(list(map(int, subprocess.check_output("nvidia-smi --query-gpu=memory.used,memory.total --format=csv,noheader,nounits", encoding="utf-8").strip().split(",")))), 2)



   













if __name__=="__main__":
    for name, func in inspect.getmembers(sys.modules["__main__"],inspect.isfunction):
        if func.__module__=="__main__": print(f'{name}: {func()}')    