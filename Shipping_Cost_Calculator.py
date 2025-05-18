# Shipping Cost Calculator

## Input package weight, volume dimensions, and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
length  = float(input("Enter the package length in centimeters: "))
width = float(input("Enter the package weigth in centimeters: "))
height = float(input("Enter the package height in centimeters: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate volumetric weight
volumetric_weight = (length * width * height) / 5000

# Use the greater of the two weights
chargeable_weight = max(weight, volumetric_weight)

## Calculate shippping cost
shipping_cost = chargeable_weight * rate

print(f"Shipping Cost: {shipping_cost:.2f} USD (Based on {chargeable_weight:.2f} kg)")

