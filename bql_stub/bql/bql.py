"""This is a simple stubbed BQL that returns pre-defined results for pre-defined queries.
Not a general simulator, just for blogging purposes.
"""

from . import bql_faker
import warnings
import pandas as pd
from typing import Iterable
from .bql_faker import stripquery
from iql.extensions.bql_ext import bql_wrapper as bw

warnings.simplefilter(action="ignore", category=FutureWarning)


def combined_df(response: pd.DataFrame) -> pd.DataFrame:
    return response


class Service:
    def __init__(self):
        pass

    def execute(self, query: str):
        query = stripquery(query)
        if query not in bql_faker.QUERY_RESULTS:
            print(bql_faker.QUERY_RESULTS.keys())
            raise ValueError(f"Query not defined: {query=}")

        else:
            return bql_faker.QUERY_RESULTS[query]

    def execute_many(self, query: Iterable[str], on_request_error=None):
        return [self.execute(q) for q in query]


# Monkey Patch shortcut
orig_to_data_arrow = bw._to_data_arrow


def new_to_data_arrow(response):
    if isinstance(response, pd.DataFrame):
        return response.melt(id_vars=["ID", "DATE"], var_name="name")
    else:
        return orig_to_data_arrow(response)


bw._to_data_arrow = new_to_data_arrow
