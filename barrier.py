import threading 
import time		

barrier = threading.Barrier(3) 

class WorkerThread(threading.Thread): 
    def __init__(self, name): 
        threading.Thread.__init__(self) 
        self.name = name 

    def run(self):
        print('Thread ' + self.name + ' launched and waiting at the barrier')
        barrier.wait()
        print('Thread ' + self.name + ' back to business')
        time.sleep(5)
        print('Thread ' + self.name + ' has finished')

		
thread1 = WorkerThread('1') 
thread2 = WorkerThread('2')
thread3 = WorkerThread('3')

thread1.start() 
thread2.start()
thread3.start()

thread1.join() 
thread2.join()
thread3.join()

print("Exit\n") 
