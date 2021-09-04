import threading
import time
import random
class Hello(threading.Thread):
    def __init__(self, min, max):
        self.min, self.max = min, max
        threading.Thread.__init__(self)

    def run(self):
        time.sleep(self.max)

        for i in range(1000):
            print(random.choice(range(self.min, self.max)))

# This creates the thread objects, but they don't do anything yet
h = Hello(3,5)
k = Hello(0,3)

# This causes each thread to do its work
h.start()
k.start()