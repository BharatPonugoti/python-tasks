#Performance Tracker (Decorators)#
import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Time:", end - start)
    return wrapper

@timer
def task():
    for i in range(1000000):
        pass

task()