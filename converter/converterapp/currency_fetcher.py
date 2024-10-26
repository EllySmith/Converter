import requests

def fetch_conversion_rates(api_key, currency):
    url = f"https://open.er-api.com/v6/latest/{currency}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Error fetching data: {response.status_code} {response.text}")

    data = response.json()
        
    conversion_rates = {currency: {}}

    for curr, rate in data['rates'].items():
        if curr != currency:  
            conversion_rates[currency][curr] = round(rate, 4)

            conversion_rates[curr] = {currency: round(1 / rate, 4)}

    return conversion_rates
