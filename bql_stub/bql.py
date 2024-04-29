"""This is a simple stubbed BQL that returns pre-defined results for pre-defined queries. 
Not a general simulator, just for blogging purposes.
"""
import json
import pandas as pd
import hashlib
from pathlib import Path

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

MODULE_DIR = Path(__file__).parent
QUERY_CACHE_FILE = MODULE_DIR / "queries.json"

def combined_df(response: dict):
    return pd.read_json(response)

def _hash(query: str):
    return hashlib.md5(query.encode()).hexdigest()

class Service():
    query_cache = {}

    def __init__(self):
        with open(QUERY_CACHE_FILE, 'r') as f:
            self.query_cache = json.load(f)

    def execute(self, query: str):

        if _hash(query) not in self.query_cache:
            print(f"Unexpected query {_hash(query)=}")
        else:
            return self.query_cache[_hash(query)]

def _save(query, df):
    """Saves to the query """
    with open(QUERY_CACHE_FILE, 'r') as f:
        query_cache = json.load(f)

    query_cache[_hash(query)] = df.to_json(date_format='iso')

    with open(QUERY_CACHE_FILE, 'w') as f:
        json.dump(query_cache, f)