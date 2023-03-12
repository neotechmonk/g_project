"""
    Multi threading is about spreading idle time across multiple tasks within the same thread

    Only one thread can be run by the interpreter at a given time, In multi threading, different treads take turn


"""

import  time
import random
import threading


def get_price_feed():
    time.sleep(2)
    print('Done getting price feed')

def check_positions():
    time.sleep(8)

    outcome = True if random.sample(range(1, 10), 1)[0] > 5 else False
    if outcome : 
        print('No positions to close') 
    else : 
        print('All positions closed') 

def submit_order(*args):
    time.sleep(5)
    print(f'Submitted order for {random.choice(args)}')

print(f"-----Active threas before spawning new threads {threading.active_count()}")

start=time.perf_counter()

price_feed_thread = threading.Thread(target=get_price_feed, args=())
price_feed_thread.start()

positions_thread = threading.Thread(target=check_positions, args=())
positions_thread.start()

order_thread = threading.Thread(target=submit_order, args=("ETH", "BTC", "LTC"))
order_thread.start()

print(f"-----Active threas after spawning new threads {threading.active_count()}")

end_spawn=time.perf_counter()
for t in threading.enumerate():
    print(f'Thread Name {t.name}')




# Wait for all threads to complete
# This is important if the main thread's next step is to happen after all the threads are done
price_feed_thread.join()
positions_thread.join()
order_thread.join()

end=time.perf_counter()

print(f'^^^^Thread creating {start}; \n^^^^Thread done creating {end_spawn}; \n^^^^Threads done running {end}' )
