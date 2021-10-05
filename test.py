""" from concurrent.futures import ThreadPoolExecutor, thread
import threading
import time

def thread_function():
    time.sleep(2)
    print("thread_function Executed {}".format(threading.current_thread()))
def main():
    executor = ThreadPoolExecutor(max_workers = 3)
    task1 = executor.submit(thread_function)
    task2 = executor.submit(thread_function)
if __name__ == "__main__":
    main()

 """
a = [[]] * 3
a[1].append(1)
print(a)


