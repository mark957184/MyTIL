'''
DAY 15: HTTPS Requests
Today I Learned how to make HTTPS requests in Python using the requests library and how to handle responses from the server that are in JSON format.
Here is an example of how to make a GET request to an API and handle the JSON response:
'''

import requests

def get_rate():
    response = requests.get('https://open.er-api.com/v6/latest/USD')

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return
    else:
        data = response.json()
        rates = data['rates']

        print("----------------------------- Currency Exchanger 2.0 -----------------------------")
        from_currency = input("from what currency do you want to exchange? (USD, EUR, GBP, etc.): ")
        to_currency = input("to what currency do you want to exchange? (USD, EUR, GBP, etc.): ")

        try:
            amount = float(input("how much do you want to exchange?: "))
        except:
            print("\nAmount invalid! Please try again\n")

        if from_currency in rates:
            amount_in_usd = amount / rates[from_currency]
            final_amount = amount_in_usd * rates[to_currency]
            print(f"\n{amount:.2f}{from_currency} are equivalent to: {final_amount:.2f}{to_currency}\n")
        else:
            print("\nInvalid currency! Please try again\n")     

while True:
    get_rate()


'''
In this way our code is not "offline" anymore, it does an exchange from "online" data, so we can be sure that the exchange rate is up to date!
'''