import os
import time
import threading

folder = "Occlusion"

print(len(os.listdir(folder)))
print("create thread every : <number of files> e.g. 10000 (default: 10000)")

recent = 0
thread_interval = int(input())
if not thread_interval:
    thread_interval = 10000

time.sleep(1)
    
def rem(list):
    for i in list:
        # time.sleep(.001)
        os.remove(f'{folder}/{i}')
        print(i)

for index, item in enumerate(os.listdir(folder)):
    if index % thread_interval == 0:
        t = threading.Thread(target=rem, args=(os.listdir(folder)[recent:index],))
        t.start()
        recent = index

t = threading.Thread(target=rem, args=(os.listdir(folder)[-(len(os.listdir(folder)) % thread_interval):],))
t.start()
