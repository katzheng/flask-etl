import pandas as pd
import os


def get_demo_fp():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, './../resources/prices.csv')
    return filename


def read_csv():
    filepath = get_demo_fp()
    return pd.read_csv(filepath)
