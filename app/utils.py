from decimal import Decimal

import requests

from app.settings import SEARCH_URL


def search_in_api(game_name, web):
    response = requests.get(SEARCH_URL+"{}+{}".format(game_name, web))
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        return "Error buscando en la API"

    parsed_response = response.json()
    name = parsed_response.get("items")[0].get("title")
    link = parsed_response.get("items")[0].get("link")
    if web != "amazon":
        price = Decimal(parsed_response.get("items")[0].get("pagemap").get("offer")[0].get("price"))
        currency = parsed_response.get("items")[0].get("pagemap").get("offer")[0].get("pricecurrency")
    else:
        price = Decimal(0)
        currency = "No se ha podido obtener"

    return "Nombre: {}\n" \
           "Precio: {}\n" \
           "Moneda: {}\n" \
           "Enlace: {}".format(name, price if price > Decimal(0) else "No se ha podido obtener", currency, link)


