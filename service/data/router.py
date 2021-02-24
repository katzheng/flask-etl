from data import app
import data.dao.loader as loader


@app.route('/')
def index():
    df = loader.read_csv()
    # ‘records’ : list like [{column -> value}, … , {column -> value}]
    return df.to_json(orient='records')
