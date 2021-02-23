import threading
import time

class WorkerThread(threading.Thread):

    def __init__(self, name): 

        threading.Thread.__init__(self) 

        self.name = name 
    
    def run(self):

        print("Thread " + self.name + ": starting")
    
        time.sleep(2)
    
        print("Thread " + self.name + ": finishing")

if __name__ == "__main__":

    print("Main    : before creating thread")

    x = WorkerThread("1")
    
    print("Main    : before running thread")
    
    x.start()
    
    print("Main    : wait for the thread to finish")
    
    x.join()
    
    print("Main    : all done")