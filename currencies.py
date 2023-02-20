import requests
import itertools
from typing import List
from pydantic import BaseModel

def get_currencies():
    url = "https://api.apilayer.com/exchangerates_data/symbols"
    headers = {"apikey": "uTkeoci53rf7i8Xbq8CYKQgFckOQ8Y32"}
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    
    currencies = []
    
    for key, name in data["symbols"].items():
        if key in ["USD", "EUR", "ARS", "BRL", "CLP", "COP", "MXN", "PEN", "UYU"]:
            currency = {"key": key, "name": name}
            currencies.append(currency)
    return currencies



def get_best_investment(date):
    """Returns the best investment for a given date.
    :params: date : The format of the date parameter input should be in the ISO 8601 format: YYYY-MM-DD. 
    For example, "2022-03-01" represents March 1st, 2022."""

    url = f"https://openexchangerates.org/api/fluctuation.json?start_date={date}&end_date={date}"
    headers = {"apikey": "uTkeoci53rf7i8Xbq8CYKQgFckOQ8Y32"}
    
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return "Unable to retrieve data from API"

    data = response.json()
    rates = data["rates"]

    # Find all possible combinations of 3 currencies
    combinations = itertools.combinations(rates.keys(), 3)

    best_investment = {
        "combination": "",
        "return": 0
    }

    for combination in combinations:
        # Calculate the return on investment for the current combination
        currency_a, currency_b, currency_c = combination
        investment = 1000
        usd_to_a = investment / rates[currency_a]["start_rate"]
        a_to_b = usd_to_a * rates[currency_b]["start_rate"]
        b_to_c = a_to_b * rates[currency_c]["start_rate"]
        final_return = (b_to_c - investment) / investment

        # Update best_investment if the current combination has a higher return
        if final_return > best_investment["return"]:
            best_investment["combination"] = ", ".join(combination)
            best_investment["return"] = final_return

    return best_investment