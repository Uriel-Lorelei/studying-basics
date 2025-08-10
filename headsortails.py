import random

heads = 0 
tails = 0 

for i in range(1,1000001):
    if random.randint(0,1) == 0:
        heads += 1
    else:
        tails += 1

print(f'heads = {heads} and tails = {tails}')