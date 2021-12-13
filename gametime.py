import time
import math
from reader import feed

start_time=time.time()
elapsed_time=start_time-time.time()

run=True
while run:
 elapsed_time=elapsed_time-(start_time-time.time())
 time.sleep(1)
 print(elapsed_time)
 
