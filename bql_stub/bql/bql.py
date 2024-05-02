"""This is a simple stubbed BQL that returns pre-defined results for pre-defined queries. 
Not a general simulator, just for blogging purposes.
"""

from . import bql_faker
import warnings
import pandas as pd

warnings.simplefilter(action="ignore", category=FutureWarning)


def combined_df(response: pd.DataFrame) -> pd.DataFrame:
    return response


class Service:

    def __init__(self):
        pass

    def execute(self, query: str):
        if query not in bql_faker.QUERY_RESULTS:
            raise ValueError("Query not defined")
        else:
            return bql_faker.QUERY_RESULTS[query]
