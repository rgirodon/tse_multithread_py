import concurrent.futures
import threading
import time

def thread_function(name):

    print("Thread " + str(name) + ": starting")
    
    time.sleep(2)
    
    print("Thread " + str(name) + ": finishing")

if __name__ == "__main__":
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:

        executor.map(thread_function, range(6))