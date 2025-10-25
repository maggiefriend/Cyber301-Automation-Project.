# dishonest_capacity_calculator.py
# This program calculates the real storage capacity of a hard drive
# or flash drive based on the advertised (often misleading) manufacturer values.

import sys  # to allow program exit if invalid input is entered

print("=== Dishonest Capacity Calculator ===")
print("This program helps you find out the real capacity of your storage device.")
print("Note: Manufacturers often use decimal GB/TB instead of binary GB/TB.\n")

# Ask user for the unit type
unit = input("Enter the advertised unit (TB or GB): ").strip().lower()

# Calculate discrepancy based on the entered unit
if unit == 'tb':
    discrepancy = 1000000000000 / 1099511627776
elif unit == 'gb':
    discrepancy = 1000000000 / 1073741824
else:
    print("❌ Invalid unit! Please enter TB or GB.")
    sys.exit()  # Exit the program if invalid input is given

# Ask for advertised capacity
advertised_capacity_input = input("Enter the advertised capacity (e.g., 10): ")

# Validate numeric input
try:
    advertised_capacity = float(advertised_capacity_input)
except ValueError:
    print("❌ Invalid number! Please enter a numeric value.")
    sys.exit()

# Calculate the real capacity
real_capacity = round(advertised_capacity * discrepancy, 2)

# Display results
print("\n📊 Results:")
print(f"Advertised capacity: {advertised_capacity} {unit.upper()}")
print(f"Actual capacity: {real_capacity} {unit.upper()}")

# Fun note
print("\n💡 Note: Notice how the real capacity is always smaller!")
print("Manufacturers use decimal measurements, but computers use binary.")
