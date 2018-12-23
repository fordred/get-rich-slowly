#!/usr/bin/env python3

import sys
import datetime
import dateutil.tz
import psycopg2
import psycopg2.extras

sys.exit()

if __name__ == "__main__":
    transactions = []
    transactions.append({'tz': datetime.datetime(2018,12,23, 5,10,40, tzinfo=dateutil.tz.tzlocal()), 'v': 1500.00})
    transactions.append({'tz': datetime.datetime(2018, 4,21,18,26,21, tzinfo=dateutil.tz.tzlocal()), 'v': 1500.00})
    transactions.append({'tz': datetime.datetime(2018,11,27, 8, 3,42, tzinfo=dateutil.tz.tzlocal()), 'v': 1500.00})
    transactions.append({'tz': datetime.datetime(2018, 2, 6,10, 5,47, tzinfo=dateutil.tz.tzlocal()), 'v': 1500.00})

    # postgres db insert
    conn = psycopg2.connect(dbname='tutorial', user='postgres', password='password', host='localhost')
    cur = conn.cursor()

    for F in transactions:
        print(F)
        cur.execute("""
            INSERT INTO degiro_test (
                time,
                fund_name,
                fund_currency,
                fund_isin,
                totVal,
                size
            )
            VALUES (
                %(time)s,
                %(fund_name)s,
                %(fund_currency)s,
                %(fund_isin)s,
                %(totVal)s,
                %(size)s
            );""", {
                'time':F['tz'],
                'fund_name':'Deposit',
                'fund_currency':'EUR',
                'fund_isin':'',
                'totVal':F['v'],
                'size':F['v']
                }
        )
        # conn.commit()
