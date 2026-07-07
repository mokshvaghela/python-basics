# Write a python function which converts inches to cms.

def inches_to_cms(inches):
    cms = inches * 2.54  # Conversion formula: 1 inch = 2.54 cm
    return cms

inches = float(input("Enter length in inches: "))
print(f"{inches} inches is equal to {inches_to_cms(inches)} centimeters.")