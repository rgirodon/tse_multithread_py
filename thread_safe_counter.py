import threading


class Counter :

    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.value += 1


counter = Counter()

def incrementCounter():

    global counter
    
    for x in range(100000):

        counter.increment()


threads = []

for t in range(10):

    threads.append(threading.Thread(target = incrementCounter))


for t in threads:

    t.start()


for t in threads:

    t.join()


print(counter.value)