from pprint import pprint
from typing import Literal, Any

from investiny import search_assets, historical_data


def request_to_investing(
        query: str,
        limit: int = 10,
        type_of_asset: Literal[
                           "Stock", "ETF", "Commodity", "Index", "Future", "Yield", "FX"
                       ] | None = None,
        exchange: str = None,
        from_date: str | None = None,
        to_date: str | None = None,
        interval: Literal[1, 5, 15, 30, 60, 300, "D", "W", "M"] = "D"
) -> dict[str, Any]:
    """
    The function queries the Investing.com site, searching for the specified
    asset and returns its historical data.
    """

    search_results = search_assets(query, limit, type_of_asset, exchange)
    investing_id = int(search_results[0]["ticker"])
    data = historical_data(investing_id, from_date, to_date, interval)
    pprint(search_results)
    pprint(data)

    return data


def main() -> None:
    result = request_to_investing(query="AAPL", limit=1, type_of_asset="Stock", exchange="NASDAQ")
    last_price = result["close"][-1]

    print(f"The last price before closing is {round(last_price, 2)}")


if __name__ == "__main__":
    main()
