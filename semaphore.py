# importing the modules 
import threading		
import time		 

# creating semaphore with count = 5 (restaurant with 5 tables)
semaphore = threading.Semaphore(5)		 

# creating instance 
def welcomeClient(name):	 
	
    # calling acquire method 
    semaphore.acquire()

    print('Client ' + name + ' having dinner...') 	
    
    time.sleep(5)

    print('Client ' + name + ' has finished.') 
		
    # calling release method 
    semaphore.release()	 

		
# creating multiple threads
for i in range(12) : 
    
    t = threading.Thread(target = welcomeClient , args = ('Thread-' + str(i),))

    t.start()