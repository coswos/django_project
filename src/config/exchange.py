from django.http import HttpResponse
import requests
from pydantic import BaseModel, Field

BASE_URL = "https://www.alphavantage.co"
API = "WNQY7BD3RJ1OI3F1"


def request(cur_from: str, target):
    payload: str = (
        "/query?function=CURRENCY_EXCHANGE_RATE&"
        f"from_currency={cur_from.upper()}&"
        f"to_currency={target.upper()}&"
        f"apikey={API}"
    )
    url: str = "".join([BASE_URL, payload])

    raw_response: requests.Response = requests.get(url)
    result = RawData(**raw_response.json())
    return result


class RawData(BaseModel):
    all_dt: dict = Field(alias="Realtime Currency Exchange Rate")


class ValueData(BaseModel):
    dt_from: str = Field(alias="1. From_Currency Code")
    dt_to: str = Field(alias="3. To_Currency Code")
    rate: float = Field(alias="5. Exchange Rate")


def main_exchange(_):
    cur_from = 'usd'
    cur_to = 'uah'
    req = request(cur_from=cur_from, target=cur_to)
    values = ValueData(**req.all_dt)
    return HttpResponse(f"Rate {cur_from.upper()} to {cur_to.upper()} is {values.rate}")


if __name__ == "__main__":
    main_exchange()
