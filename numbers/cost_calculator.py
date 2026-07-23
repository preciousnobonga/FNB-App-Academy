# Ask the user how many kilometers they want to drive
# Ask them for the current petrol price per liter (this can be a decimal, like R22.45)
# Assume their car uses exactly 1 liter of fuel for every 10 km driven
# (Formula: liters_needed = kilometers / 10)
# Calculate the total cost (liters_needed * petrol_price)
# Use type casting to ensure your numbers work, and use round() to format the final cost to 2 decimal places


# Ask the user how many kilometers they want to drive
kilometers = float(input("Enter the number of kilometers you want to drive: "))

# Ask them for the current petrol price per liter
petrol_price = float(input("Enter the current petrol price per liter: R"))

# Assume the car uses 1 liter per 10 km
liters_needed = kilometers / 10

# Calculate total cost
total_cost = liters_needed * petrol_price

# Round to 2 decimal places
print("Total cost of the trip: R", round(total_cost, 2))

