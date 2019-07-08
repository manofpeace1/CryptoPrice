import requests
from config import my_crypto_wallet


def request_crypto_info():
    global json_response
    currency = 'EUR'
    url = 'https://api.alternative.me/v1/ticker/?convert=' + currency
    send_request = requests.get(url)
    json_response = send_request.json()


def get_my_crypto_info():
    i = 0
    while i < len(json_response):
        for item in my_crypto_wallet:
            if item == json_response[i]['symbol']:
                my_crypto_wallet[item]['current_price_eur'] = float(
                    json_response[i]['price_eur'])
        i += 1


def calc_profitability():
    overall_profit = 0
    for item in my_crypto_wallet:
        current_total_price = my_crypto_wallet[item]['current_price_eur'] * \
            my_crypto_wallet[item]['owned']
        original_total_price = my_crypto_wallet[item]['buy_price_eur'] * \
            my_crypto_wallet[item]['owned']
        each_currency_profit = current_total_price - original_total_price
        overall_profit += each_currency_profit
        print(item, "%.2f" % each_currency_profit, '€')

    print('> TOTAL', "%.2f" % overall_profit, '€\n')
