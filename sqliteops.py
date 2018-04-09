import click
from persistence import sqlite

@click.command()
@click.option('--name', prompt='Table name',
              help='The table name to create in SQLite.')
def db(name):
    sqlite.create_table(name)

if __name__ == '__main__':
    db()