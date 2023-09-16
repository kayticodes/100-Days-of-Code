# day 2 - 100 days of coding
# todays project is a tip calculator
count = input("how many people will be splitting? ")
price = input("what is the cost? ")
total = round(int(price)/int(count), 2)
twenty = total * .2
twenty_five = total * .25
thirty = total * .3
print("Each person's portion is: " + str(total) + "\n")
print("tip options:\n" + "20% = $" + str(twenty) + ", total = $" + str(total + twenty))
print("25% = $" + str(twenty_five) + ", total = $" + str(total + twenty_five))
print("30% = $" + str(thirty) + ", total = $" + str(total + thirty))
