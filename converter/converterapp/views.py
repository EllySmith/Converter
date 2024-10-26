from django.shortcuts import render

from django.http import HttpResponse

conversion_rates = {
    'USD': {'EUR': 0.85, 'JPY': 110.0, 'GBP': 0.75},
    'EUR': {'USD': 1.18, 'JPY': 130.0, 'GBP': 0.88},
    'JPY': {'USD': 0.009, 'EUR': 0.0077, 'GBP': 0.0068},
    'GBP': {'USD': 1.33, 'EUR': 1.14, 'JPY': 148.0}
}

def convert_currency(currency_from, currency_to, amount):
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
