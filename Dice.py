import random
Dice=random.randint(1,7)
print(f"You rolled {Dice}")
if Dice ==1:
    print("Drop the dice")
elif Dice ==3:
    print("Roll again")
elif Dice ==6:
    print("Move to the next stage")
else:
    print("Opps,Better luck next time")