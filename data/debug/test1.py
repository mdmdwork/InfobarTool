import psutil

cpu = f"CPU{psutil.cpu_percent()}%"
mem = f"内存{psutil.virtual_memory().percent}%"
print((4, cpu, mem))
