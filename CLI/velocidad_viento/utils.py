"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from datetime import datetime, timedelta

from requests import get
from requests.exceptions import HTTPError
from prototools import MESES


def _get_dates(yy, mm, format_="%Y-%m-%dT%H:%M:%S"):
    start = datetime(yy, mm, 1)
    if mm == 12:
        end = datetime(yy + 1, 1, 1) - timedelta(seconds=1)
    else:
        end = datetime(yy, mm + 1, 1) - timedelta(seconds=1)
    return start.strftime(format_), end.strftime(format_)


def get_data(url, params):
    try:
        response = get(url.format(params))
        response.raise_for_status()
        data = response.json()
    except HTTPError as http_err:
        print(f"HTTP error: {http_err}")
    except Exception as err:
        print(f"Error: {err}")
    else:
        return data


def set_params(params, yy, mm):
    return params.format(*_get_dates(yy, mm))


def get_sheetname(m):
    return MESES[m-1]
