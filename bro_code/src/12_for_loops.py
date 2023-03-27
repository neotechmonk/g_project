"""
    Iterate over a pre determined number of times
    (as opposed to `while` is until a condition is true)
"""

# 0 indexed
import time


for i  in range(10): 
    print(f"Iteraction {i}")


# Start with a specific start point
for i  in range(1, 10+1): 
    print(f"Iteraction {i}")

# Skip by x
print("Every other number")
for i  in range(1, 100+1, 2): 
    print(f" {i}")

# Time based wait and count backwards. I.e. can count backwards
for secs in range(10, 0, -1):
    print(secs)
    time.sleep(1)
print("Happy new year")
