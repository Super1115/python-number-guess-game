import random


num = random.randint(0,1000)
low = 0
high = 1000
for i in range(10):
    print(f"數字介於{low}到{high}")
    userNum = int(input(f"你還有{10-i}次機會"))
    if userNum == num:
        print("YOU WIN!!!")
        break
    elif userNum > num:
        high = userNum
    elif userNum < num:
        low = userNum
if userNum != num:
    print(f"YOU LOSE!!! The Number is {num}")