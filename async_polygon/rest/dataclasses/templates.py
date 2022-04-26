from typing import Dict, Union


class Template:

    _results: Union[str, None] = 'results'
    _keys_to_work: Dict[str, str]


    def make_pretty_json(self, resp_json: dict):
        print(type(resp_json))
        return
    pass


class AggregateBars(Template):

    _keys_to_work = {
        'c': 'Close',
        'h': 'High',
        'l': 'Low',
        'n': 'Transactions',
        'o': 'Open',
        't': 'Timestamp',
        'v': 'Volume',
        'vw': 'Volume_AVG_Price',
    }


class PreviousClose(Template):

    _keys_to_work = {
        'T': 'Ticker',
        'c': 'Close',
        'h': 'High',
        'l': 'Low',
        'o': 'Open',
        't': 'Timestamp',
        'v': 'Volume',
        'vw': 'Volume_AVG_Price',
    }


class LastTrade(Template):

    _keys_to_work = {
        'T': 'Ticker',
        'p': 'Price',
        's': 'Volume'
    }


class LastTradeCryptoPair(Template):

    _results = 'last'
    _keys_o_work = {
        'price': 'Price',
        'size': 'Volume',
        'timestamp': 'Timestamp',
    }