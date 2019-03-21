#!/usr/local/bin/python3
"""eth_hist.py

grabs last day ending price of various instruments and writes to file.
"""

import datetime
import gdax
import json
import pytz
import time


def get_start_and_end_times(tz='America/Los_Angeles'):
    now = datetime.datetime.now()
    start_time = datetime.datetime(year=now.year, month=now.month, day=now.day, hour=0, minute=0)
    end_time = datetime.datetime(year=now.year, month=now.month, day=now.day, hour=0, minute=20)
    local_tz = pytz.timezone(tz)
    start_time = local_tz.localize(start_time)
    end_time = local_tz.localize(end_time)
    return start_time, end_time



def get_yest_end_price(product):
    start_time, end_time = get_start_and_end_times()
    resp = gdax.PublicClient().get_product_historic_rates(product, start_time, end_time)
    price = resp[0][3]
    time.sleep(1)  # don't overload our gdax connection
    return price


def write_yest_end_prices(products, output_file=None):
    if output_file is None:
        output_file = '/Users/yiws/.cryptoprice.json'
    price_dict = {product: get_yest_end_price(product) for product in products}
    with open(output_file, 'w') as fd:
        json.dump(price_dict, fd, indent=4)


def main():
    products = [
        'BTC-USD',
        'ETH-USD',
        'LTC-USD',
        'BCH-USD',
    ]
    write_yest_end_prices(products)


if __name__=='__main__':
    pass
    # main()
