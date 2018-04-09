import click
from scraper import scraper
from pprint import pprint

SOUTH=43.75244011635154
WEST=-79.44002579968873
NORTH=43.77016905151843
EAST=-79.40522145551148

@click.command()
@click.option('--price-min', default=0, help='Minimum price')
@click.option('--price-max', default=999999999, help='Maximum price')
@click.option('--sold-day-back', default=90, help='Maximum days sold back')
@click.option('--db-name', default='solds', help='Table name to store results in')
def scrape(price_min, price_max, sold_day_back):
    listing_ids = scraper.get_listings(price_min, price_max, sold_day_back, SOUTH, WEST, NORTH, EAST)
    for id in listing_ids:
        listing = scraper.get_listing(id)
        pprint(listing)

if __name__ == '__main__':
    scrape()