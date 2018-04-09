import pandas as pd

from pymongo import MongoClient

from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral5
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
    group = df.groupby(['PropertyStyle'])
    source = ColumnDataSource(group)
    cyl_cmap = factor_cmap('PropertyStyle', palette=Spectral5, factors=df.PropertyStyle.unique())

    p = figure(x_range=group, title="Solds by Type", tools="")
 
    p.vbar(x='PropertyStyle', top='_Sold_count', width=1, source=source,
       line_color=cyl_cmap, fill_color=cyl_cmap)

    p.y_range.start = 0
    p.xgrid.grid_line_color = None
    p.xaxis.axis_label = "some stuff"
    p.xaxis.major_label_orientation = 1.2
    p.outline_line_color = None

    show(p)

    #print(group_df)

if __name__ == '__main__':

    cl = MongoClient()
    coll = cl["local"]["solds"]
    cursor = coll.find({})

    df = pd.DataFrame(list(cursor))

    df['Pictures'] = df.Pictures.apply(flatten_photos)
    df['PropertyStyle'] = df._ownershiptype.apply(extract_style)
    df['PropertyType'] = df._ownershiptype.apply(extract_type)

    plot_counts_by_type(df)
    print(list(df))