import requests

LISTINGS_URL = 'https://mongohouse.com/api/soldrecords?query=true&price_min={0}&price_max={1}&sold_day_back={2}&bedrooms=0&washrooms=0&ownershiptype=all&south={3}&west={4}&north={5}&east={6}&_2dsphere=true'

def get_listings(price_min, price_max, sold_day_back, south, west, north, east):
    r = requests.get(LISTINGS_URL.format(price_min, price_max, sold_day_back, south, west, north, east))
    return r.json()