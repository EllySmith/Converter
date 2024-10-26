from django.shortcuts import render

from django.http import HttpResponse

from .currency_fetcher import fetch_conversion_rates

api_key = '91169fb003b5cd05f738b1dac2930472'

def convert_currency(currency_from, currency_to, amount):

    conversion_rates = fetch_conversion_rates(api_key, currency_from)

    if currency_from in conversion_rates and currency_to in conversion_rates[currency_from]:
        conversion_rate = conversion_rates[currency_from][currency_to]
        return amount * conversion_rate
    else:
        return None


def home(request):
    result = None
    if request.method == "POST":
        currency_from = request.POST.get("currency_from").upper()
        currency_to = request.POST.get("currency_to").upper()
        amount = float(request.POST.get("amount"))

        result = convert_currency(currency_from, currency_to, amount)
        if result is not None:
            result = f"{amount} {currency_from} is equal to {result:.2f} {currency_to}"
        else:
            result = "Conversion rate not available."

    return render(request, 'converterapp/currency_converter.html', {'result': result})
