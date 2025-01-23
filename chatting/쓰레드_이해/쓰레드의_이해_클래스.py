import threading
import time

class Worker(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name          

    def run(self):
        print("sub thread start! ", threading.current_thread().name)
        time.sleep(3)
        print("sub thread end! ", threading.current_thread().name)


print("main thread start")
for i in range(5):
    name = f"thread number : {i}"
    thd = Worker(name)             
    thd.start()                       
print("main thread end")