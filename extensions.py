# coding=UTF-8
import requests
import json
from config import keys


class ConvertionException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        tickers = f'{quote_ticker}_{base_ticker}'
        url = f'https://free.currconv.com/api/v7/convert?q={tickers}&compact=ultra&apiKey=2386411d8ef1ed3d32e5'
        r = requests.get(url)
        total_base = json.loads(r.content)[tickers]
        total_base = total_base * amount
        return total_base
