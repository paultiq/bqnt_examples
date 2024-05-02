import pandas as pd
import numpy as np


corr_query = """get(sales_rev_turn)
    for(members('SPX Index'))
    with(fpo=range(-9Q, 0Q), fpt=Q, fill=prev)
    preferences(addcols=all)"""

basics_query = """get(
      px_last
    ) for(
      ['IBM US Equity']
    ) with(
      dates=range(-29d, 0d),
      fill=prev,
      currency=USD
    )"""

QUERY_RESULTS = {}


def basics():
    # Data for Basics

    periods = 30

    dates = pd.date_range(
        start=pd.Timestamp.now() - pd.DateOffset(years=1), periods=periods
    ).normalize()

    basics_response = pd.DataFrame(
        {"ID": "IBM US Equity", "DATE": dates, "px_last": np.random.rand(periods) * 10}
    )

    return basics_response


def corr():
    start_year = 2020
    num_periods = 10
    periods = [f"{start_year + n//4} Q{n%4+1}" for n in range(num_periods, 0, -1)]
    period_offset = [
        f"{n - num_periods if n != num_periods else 0}Q"
        for n in range(num_periods, 0, -1)
    ]
    companies = [f"CO{n+1} FAKE" for n in range(0, 500)]

    dfs: list[pd.DataFrame] = []
    for co in companies:
        co_df = pd.DataFrame(
            {
                "ID": co,
                "PERIOD": periods,
                "PERIOD_OFFSET": period_offset,
                "sales_rev_turn": np.random.rand(num_periods) * 1000,
            }
        )
        dfs.append(co_df)

    corr_response: pd.DataFrame = pd.concat(dfs).reset_index(drop=True).set_index("ID")  # type: ignore
    return corr_response


QUERY_RESULTS[basics_query] = basics()
QUERY_RESULTS[corr_query] = corr()
