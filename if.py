import random

lo = 1
hi = 1000
guessed = False
answer = random.randint(lo,hi)
trails = 10
guess = 0
i=1

print(f"guess what the the random number is, between {lo} and {hi} within {trails}")
while answer!= guess and trails!=0:
    guess = int(input(f"number {i} trail, guess the answer Amoory and Hamoody: "))
    i=i+1
    if guess == 0:
        print("you've quitted:(")
        break
    elif guess == answer:
        print("********** you got it! ***********")
        break
    else:
        if guess > answer:
             print("guess lower")
             trails-=1
        else:
             print("guess higher")
             trails-=1
print(answer)

