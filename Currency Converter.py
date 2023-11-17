from forex_python.converter import CurrencyRates

def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    converted_amount = c.convert(from_currency, to_currency, amount)
    return converted_amount

print("Currency Converter")

from_currency = input("Enter the currency to convert from (e.g., USD): ").upper()
to_currency = input("Enter the currency to convert to (e.g., EUR): ").upper()
amount = float(input("Enter the amount: "))

result = convert_currency(amount, from_currency, to_currency)
print(f"{amount} {from_currency} equals {result} {to_currency}")
