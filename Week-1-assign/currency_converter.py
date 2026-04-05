"""
Assignment Week 1

Description:

Assignment: Build a Currency Converter in Python You are required to build a simple 
currency converter program. 

Requirements: 
1. The program must: Accepts users input in Nigerian Naira (NGN) and  

2. Convert the amount to at least three currencies.For example, USD, EUR, GBP

3. You must: Use functions properly Store exchange rates using a dictionary. Use input() to collect user data 

4. Display clearly formatted output .Structure your program properly: Create a dictionary to store exchange rates 

5. Write a reusable conversion function  Ensure your code is clean and well organized
"""

from rich import print


exchange_rates = {
    "USD": 0.00062,   # 1 NGN to USD
    "EUR": 0.00057,   # 1 NGN to EUR
    "GBP": 0.00049    # 1 NGN to GBP
}


def convert_currency(amount_ngn, rates_dict):
    """
    Converts NGN to multiple currencies using provided exchange rates.
    Returns a dictionary of converted values.
    """
    converted = {}
    for currency, rate in rates_dict.items():
        converted[currency] = amount_ngn * rate
    return converted


def main():

    "Main function to run the currency converter program."

    try:
        
        amount = float(input("Enter The  amount you wish to convert in Naira (NGN): "))

        results = convert_currency(amount, exchange_rates)
      
        print("\n=== Currency Conversion Results ===")
        print(f"NGN: ₦{amount:,.2f}")

        for currency, value in results.items():
            print(f"{currency}: {value:,.2f}")

    except ValueError:
        print("Invalid input! Please enter a valid numeric amount.")


if __name__ == "__main__":
    main()