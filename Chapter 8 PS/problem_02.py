# Write a python program using function to convert Celsius to Fahrenheit.

def temp():
    Celsius = float(input("Enter temperature in Celsius: "))
    # Conversion formula: Fahrenheit = (Celsius * 9/5) + 32
    Fahrenheit = (Celsius * 9/5) + 32
    print(f"{Celsius} degrees celsius is equals to {Fahrenheit} degrees fahrenheit.")

temp()