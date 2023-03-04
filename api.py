from datetime import date, timedelta
from pprint import pprint
import requests

# Le but de api est de fournir la structure de données suivantes :
# # un dico avec comme la clef la devise et en valeur la liste de valeurs de cette devise pour chaque jour dans l'ordre
def get_rates(currencies, days):
    end_date = date.today()
    start_date = end_date - timedelta(days=days)
    symbols = ','.join(currencies)
    requete =f"https://api.exchangerate.host/timeseries?start_date={start_date}&end_date={end_date}&symbols={symbols}"
    r = requests.get(requete)

    # Cette ligne est exécutée si la requête HTTP a échoué
    # ou si la réponse JSON n'a pas de données valides pour les taux de change demandés.
    if not r and not r.json():
        # renvoie deux valeurs, la première valeur est pour les taux de change
        # et la deuxième valeur est pour les erreurs éventuelles
        return False, False

    api_rates = r.json().get("rates") # '2023-01-30': {'CAD': 1.451486, 'USD': 1.084231},

    # creer une dico avec : key-devise, value-list
    all_rates = {currency: [] for currency in currencies} # {'CAD': [], 'USD': []}
    # les dates dans l'ordre chronologique
    all_days = sorted(api_rates.keys())

    # ajouter les données dans all_rates
    for day in all_days: # recup la valeur de chaque jour
        #print(api_rates.get(day)) #{'EUR': 1, 'PLN': 4.718084}
        [all_rates[currency].append(rates) for currency, rates in api_rates[day].items()]

    return all_days, all_rates

if __name__=='__main__':
    days, rates = get_rates(currencies = ["CAD", "USD"], days=30)
    pprint(days)
    pprint(rates)
