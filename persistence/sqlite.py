import sqlite3
conn = sqlite3.connect('housing.db')

def create_table(name):
    conn.execute('''CREATE TABLE {0}
                    (id text primary key, address1 text,  address2 text, bedrooms int, 
                     city text, list_price real, sold_date price real)'''.format(name))