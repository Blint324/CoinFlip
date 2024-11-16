import random
import time

flip_times = input("How many times to flip? ")
if int(flip_times) < 1:
    quit("no.")

start = time.time()

tailsflips = 0
headsflips = 0
difference = 0

for x in range(int(flip_times)):
    flip = random.randint(0, 1)
    if flip == 0:
        headsflips = headsflips + 1
        print("Heads!")
    else:
        tailsflips = tailsflips + 1
        print("Tails!")

print(f"Heads: {headsflips}")
print(f"Tails: {tailsflips}")

if min(headsflips, tailsflips) == headsflips:
    while not headsflips == tailsflips:
        difference = difference + 1
        headsflips = headsflips + 1
    print(f"Difference: {difference}")
else:
    while not tailsflips == headsflips:
        difference = difference + 1
        tailsflips = tailsflips + 1
    print(f"Difference: {difference}")

end = time.time()
print(f"Time elapsed: {end - start} seconds!")