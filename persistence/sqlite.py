import sqlite3
conn = sqlite3.connect('housing.db')

def create_table(name):
    conn.execute('''CREATE TABLE {0}
                    (date text, trans text, symbol text, qty real, price real)'''.format(name))