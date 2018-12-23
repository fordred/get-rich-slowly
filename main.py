#!/usr/bin/env python3

import degiro
import log
import json
import psycopg2
import psycopg2.extras

createTable = False

if __name__ == "__main__":
    session = degiro.login()
    portfolio = session.get_portfolio()
    active_portfolio = portfolio.get_active_portfolio()
    # log.write_money_amount(portfolio.get_money_amount())
    log.write_portfolio(active_portfolio)
    # postgres db insert
    conn = psycopg2.connect(dbname='tutorial', user='postgres', password='password', host='localhost')
    cur = conn.cursor()

    if (createTable):
        cur.execute("""
        CREATE TABLE degiro_test (
            time TIMESTAMPTZ NOT NULL,
            fund_name TEXT NOT NULL,
            fund_currency TEXT NOT NULL,
            fund_isin TEXT NULL,
            totVal DOUBLE PRECISION NOT NULL,
            size DOUBLE PRECISION NOT NULL
        );""")
        cur.execute("""
        SELECT create_hypertable('degiro_test', 'time');
        """)
        conn.commit()

    for F in active_portfolio:
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
                NOW(),
                %(fund_name)s,
                %(fund_currency)s,
                %(fund_isin)s,
                %(totVal)s,
                %(size)s
            );""", {
                'fund_name':F['fund']['name'],
                'fund_currency':F['fund']['currency'],
                'fund_isin':F['fund']['isin'],
                'totVal':F['totVal'],
                'size':F['size']
                }
        )
        conn.commit()
