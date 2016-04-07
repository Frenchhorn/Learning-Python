import time  
import threading  
from multiprocessing import Process   
  
def takeuptime(n):  
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'  
    s = chars * 10000
    for i in range(10*n):  
        for c in chars:  
            s.count(c)  
  
'''
    # Serial computation  
    start = time.time()  
    serial_results = [takeuptime(args) for args in list_of_args]  
    print ("%f s for traditional, serial computation." % (time.time() - start))  
  

    # Multithreading computation  
    nthead = 4 # number of threads  
    threads = [threading.Thread(target=takeuptime, args=(list_of_args[i],)) for i in range(nthead)]  
    start = time.time()  
    # Start threads one by one  
    for thread in threads:  
        thread.start()  
    # Wait for all threads to finish  
    for thread in threads:  
        thread.join()  
    print "%f s for multithreading computation." % (time.time() - start)  
  
'''
list_of_args = [10000, 10000, 10000, 10000]
# Multiprocessing computation  
process = []  
nprocess = 4 # number of processes  
for i in range(nprocess):  
    process.append(Process(target=takeuptime, args=(list_of_args[i],)))  
start = time.time()
# Start processes one by one  
for p in process:  
    p.start()  
# Wait for all processed to finish  
for i in process:  
    p.join()  
print ("%f s for multiprocessing computation." % (time.time() - start))
