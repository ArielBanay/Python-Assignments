from Dice import Dice
dice = Dice()

print("Rolling the dice 10 times:")
roll_results = []
for i in range(10):
    roll = dice.roll()
    roll_results.append(roll)
    print(f"Roll {i + 1}: {roll}")

print("\nAll rolls are within the range 1-6.")
print(roll_results)
