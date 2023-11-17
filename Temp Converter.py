def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0 / 9.0

def celsius_to_fahrenheit(celsius):
    return (celsius * 9.0 / 5.0) + 32

print("Temperature Converter")
print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")

choice = input("Enter your choice (1 or 2): ")

if choice == '1':
    f_temp = float(input("Enter temperature in Fahrenheit: "))
    c_result = fahrenheit_to_celsius(f_temp)
    print(f"{f_temp}°F in Celsius is: {c_result}°C")
elif choice == '2':
    c_temp = float(input("Enter temperature in Celsius: "))
    f_result = celsius_to_fahrenheit(c_temp)
    print(f"{c_temp}°C in Fahrenheit is: {f_result}°F")
else:
    print("Invalid choice. Please enter 1 or 2.")
