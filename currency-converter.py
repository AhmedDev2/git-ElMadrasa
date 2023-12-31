import requests

def convert_currency(amount, from_currency, to_currency):
    # API endpoint for currency conversion
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

    try:
        # Send GET request to the API
        response = requests.get(url)
        data = response.json()

        # Check if the API request was successful
        if response.status_code == 200:
            # Get the conversion rate from the API response
            conversion_rate = data['rates'][to_currency]

            # Calculate the converted amount
            converted_amount = amount * conversion_rate

            return converted_amount
        else:
            print("Failed to retrieve currency conversion rates.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Example usage
amount = int(input("Enter amount: "))
from_currency = input("Enter from currency: USD, EUR, GBP, etc.")
to_currency = input("Enter to currency: USD, EUR, GBP, etc.")

converted_amount = convert_currency(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equivalent to {converted_amount} {to_currency}")


