import system
import time # type: ignore
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))) # type: ignore

system.printme('Hello, World!')  # This is a function call