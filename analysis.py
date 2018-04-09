import pandas as pd

from pymongo import MongoClient
from bokeh.io import show, output_file
from bokeh.plotting import figure

def flatten_photos(x):
    if type(x) is list:
        return x[0]['url']
    else:
        return None

def extract_style(x):
    if type(x) is dict and 'style' in x and len(x['style']) > 0:
        return x['style'][0]
    else:
        return None

def extract_type(x):
    if type(x) is dict and 'type' in x:
        return x['type']
    else:
        return None

def plot_counts_by_type(df):
    group_df = df.groupby('PropertyStyle')['count'].sum()
    print(group_df)

if __name__ == '__main__':

    cl = MongoClient()
    coll = cl["local"]["solds"]
    cursor = coll.find({})

    df = pd.DataFrame(list(cursor))

    df.Pictures = df.Pictures.apply(flatten_photos)
    df.PropertyStyle = df._ownershiptype.apply(extract_style)
    df.PropertyType = df._ownershiptype.apply(extract_type)

    plot_counts_by_type(df)
    print(list(df))