import random
import time

roll_times = input("How many times to roll? ")
if int(roll_times) < 1:
    quit("no.")

start = time.time()

onerolls = 0
tworolls = 0
thrrolls = 0
forrolls = 0
fivrolls = 0
sixrolls = 0
sumnum = 0

for x in range(int(roll_times)):
    flip = random.randint(1, 6)
    if flip == 1:
        onerolls = onerolls + 1
        print("1!")
    elif flip == 2:
        tworolls = tworolls + 1
        print("2!")
    elif flip == 3:
        thrrolls = thrrolls + 1
        print("3!")
    elif flip == 4:
        forrolls = forrolls + 1
        print("4!")
    elif flip == 5:
        fivrolls = fivrolls + 1
        print("5!")
    elif flip == 6:
        sixrolls = sixrolls + 1
        print("6!")

print(f"1: {onerolls}")
print(f"2: {tworolls}")
print(f"3: {thrrolls}")
print(f"4: {forrolls}")
print(f"5: {fivrolls}")
print(f"6: {sixrolls}")

for x in range(onerolls):
    sumnum = sumnum + 1
for x in range(tworolls):
    sumnum = sumnum + 2
for x in range(thrrolls):
    sumnum = sumnum + 3
for x in range(forrolls):
    sumnum = sumnum + 4
for x in range(fivrolls):
    sumnum = sumnum + 5
for x in range(sixrolls):
    sumnum = sumnum + 6

maxsum = int(roll_times) * 6

print(f"Sum: {sumnum}")
print(f"Max sum: {maxsum}")

end = time.time()
print(f"Time elapsed: {end - start} seconds!")