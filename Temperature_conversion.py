def convert_temperature(value, unit):
    if unit == 'C':
        celsius = value
        fahrenheit = value * 9/5 + 32
        kelvin = value + 273.15
    elif unit == 'F':
        celsius = (value - 32) * 5/9
        fahrenheit = value
        kelvin = celsius + 273.15
    elif unit == 'K':
        celsius = value - 273.15
        fahrenheit = celsius * 9/5 + 32
        kelvin = value
    return celsius, fahrenheit, kelvin

def main():
    value = float(input("Enter the temperature value: "))
    unit = input("Enter the unit (C, F, K): ").upper()

    if unit not in ['C', 'F', 'K']:
        print("Invalid unit. Please enter C, F, or K.")
        return

    celsius, fahrenheit, kelvin = convert_temperature(value, unit)
    
    if unit == 'C':
        print(f"{value}°C = {fahrenheit:.2f}°F = {kelvin:.2f}K")
    elif unit == 'F':
        print(f"{value}°F = {celsius:.2f}°C = {kelvin:.2f}K")
    elif unit == 'K':
        print(f"{value}K = {celsius:.2f}°C = {fahrenheit:.2f}°F")

if ___name___ == "___main___":
    main()
