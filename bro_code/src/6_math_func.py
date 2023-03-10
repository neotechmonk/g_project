import math

pos_num = 99334.233343
neg_num = -343.2


# round
print(f'round  on {pos_num}  is  {0}'.format(round(pos_num))) #Note this is not math.round


# round up
print('math.ceil  on {}  is  {}'.format(pos_num, math.ceil(pos_num))) 

# round down
print('math.floor  on {}  is  {}'.format(pos_num, math.floor(pos_num))) 

# Absolute
print('abs  on {}  is  {}'.format(neg_num, abs(neg_num)))#Note this is not math.abs

# Power
print('math.pow  on {}  is  {}'.format(pos_num, math.pow(pos_num, 2))) 
# Sqrt
print('math.sqrt  on {}  is  {}'.format(pos_num, math.sqrt(pos_num)))

# Max
print('max  on {} and {}  is  {}'.format(pos_num,neg_num,  max(pos_num, neg_num)))#Note this is not math....

# Min 
print('min  on {} and {}  is  {}'.format(pos_num,neg_num,  min(pos_num, neg_num)))#Note this is not math....

