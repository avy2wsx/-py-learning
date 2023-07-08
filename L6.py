#!/Usr/bin/pythin3.10.2

import random

min = 1
max = 10
count = 0
target = random.randint(min,max)
#print(target)

while True:
    keyin =int(input(f"猜數字範圍{min}~{max}:"))
    count +=1
    if(keyin == target):
        print(f"Bingo,answer is {target}")
        print(f"總共猜了{count}次")
        break
    else:
        print("wrong")
        print(f"總共猜了{count}次")
print("game over")