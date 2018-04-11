import click
from scraper import scraper
from pprint import pprint
from persistence import mongodb

GRID_SIZE = 0.05
NORTH_MIN = 43.30885611701781
NORTH_MAX = 44.40844002224228
EAST_MIN = -79.79405580573729
EAST_MAX = -78.5558622937744

@click.command()
@click.option('--price-min', default=0, help='Minimum price')
@click.option('--price-max', default=999999999, help='Maximum price')
@click.option('--sold-day-back', default=2, help='Maximum days sold back')
@click.option('--db-name', default='solds', help='Table name to store results in')
def scrape(price_min, price_max, sold_day_back, db_name):
    for i in range(0, int((NORTH_MAX-NORTH_MIN) / GRID_SIZE)):
        for j in range(0, int((EAST_MAX-EAST_MIN) / GRID_SIZE)):
            
            south = NORTH_MAX - (i + 1) * GRID_SIZE
            north = NORTH_MAX - i * GRID_SIZE
            east  = EAST_MIN + j * GRID_SIZE
            west  = EAST_MIN + (j + 1) * GRID_SIZE

            listing_ids = scraper.get_listings(price_min, price_max, sold_day_back, south, west, north, east)
            for id in listing_ids:
                try:
                    listing = scraper.get_listing(id)
                except:
                    continue
                mongodb.insert_listing(listing)
            
if __name__ == '__main__':
    scrape()