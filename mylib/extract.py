"""
Extract a dataset from a URL like Kaggle or data.gov. 
JSON or CSV formats tend to work well
"""
import os
import requests
import pandas as pd


def extract(
    url="""
    https://github.com/fivethirtyeight/data/blob/master/tennis-time/serve_times.csv?raw=true 
    """,
    url2="""
    https://github.com/fivethirtyeight/data/blob/master/tennis-time/events_time.csv?raw=true
    """,
    file_path="data/serve_times.csv",
    file_path2="data/event_times.csv",
    directory="data",
):
    """Extract a url to a file path"""
    if not os.path.exists(directory):
        os.makedirs(directory)
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    with requests.get(url2) as r:
        with open(file_path2, "wb") as f:
            f.write(r.content)
    df = pd.read_csv(file_path2)

    df_subset = df.head(121)

    df_subset.to_csv(file_path2, index=False)
    return file_path, file_path2
