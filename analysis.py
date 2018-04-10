import pandas as pd

from pymongo import MongoClient

from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import viridis
from bokeh.plotting import figure
from bokeh.transform import factor_cmap

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
    df = df.dropna()
    group = df.groupby('PropertyStyle').count().sort_values(by='_Sold', ascending=False)

    cities = list(group.reset_index().PropertyStyle)
    solds = list(group.reset_index()._Sold)

    source = ColumnDataSource(data=dict(cities=cities, solds=solds, color=viridis(len(cities))))

    p = figure(x_range=cities, title="Solds by Styles", toolbar_location=None, tools="", sizing_mode='stretch_both')

    p.vbar(x='cities', top='solds', width=0.9, color='color', legend=None, source=source)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.xgrid.grid_line_color = None
    p.xaxis.major_label_orientation = 1.2
    p.outline_line_color = None

    show(p)

if __name__ == '__main__':

    cl = MongoClient()
    coll = cl["local"]["solds"]
    cursor = coll.find({})

    df = pd.DataFrame(list(cursor))

    df['Pictures'] = df.Pictures.apply(flatten_photos)
    df['PropertyStyle'] = df._ownershiptype.apply(extract_style)
    df['PropertyType'] = df._ownershiptype.apply(extract_type)

    plot_counts_by_type(df)