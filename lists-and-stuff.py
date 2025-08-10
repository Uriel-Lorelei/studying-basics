import random

supplies = ['pens', 'staplers', 'flamethrowers', 'binders']

for i in range(len(supplies)):
    print(f"Index {i} in supplies is: {supplies[i]}")

print('pens' not in supplies)
print('apple' in supplies)

write, pins, fire, bind = supplies

print(fire)

print(random.choice(supplies))

random.shuffle(supplies)

print(supplies[1])