#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
bill = float(input("What was the total bill? "))
people = int(input("How many people are splitting the bill? "))
tip = float(input("What percentage tip? "))/100 + 1
split = (bill / people) * tip

print(f"({bill:.2f} / {people}) * {tip:.2f} = {split:.2f}")
print(f"{split:.2f}")