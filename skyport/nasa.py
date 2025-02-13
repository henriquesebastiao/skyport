"""Provides the resources needed to consume all NASA APIs programmatically."""

from datetime import date as dt
from datetime import datetime
from enum import Enum
from http import HTTPStatus
from typing import Optional, Union

import requests

from skyport.exceptions import (
    ApiKeyInvalid,
    ApiKeyLimitExceeded,
    IncompatibleParameterFormat,
    ItemNotFound,
)
from skyport.types import Apod, NeoWs


class Endpoint(str, Enum):
    """NASA API Endpoints."""

    APOD = 'planetary/apod'
    NEOWS = 'neo/rest/v1/neo/'


class Nasa:
    """One object to interact with all [NASA APIs](https://api.nasa.gov)."""

    def __init__(self, api_key: str = 'DEMO_KEY'):
        self._base_url = 'https://api.nasa.gov/'
        self._api_key = api_key
        self._params = {'api_key': self._api_key}
        self._rate_limit_remaining = 0

    def _get(self, endpoint: str, params: Optional[dict] = None) -> dict:
        """Sends a GET request seeking information from the API.

        Args:
            endpoint (str): Endpoint of the requested service
            params (Optional[dict], optional): Parameters of request. Defaults to None.

        Raises:
            ApiKeyInvalid: API key provided is invalid
            ApiKeyLimitExceeded: API request limit exceeded
            ImcompatibleParameterFormat: Invalid parameter provided for the request
            ItemNotFound: No items found for the given parameters

        Returns:
            dict: A dict instance containing the data obtained from the API
        """
        url = self._base_url + endpoint
        params = self._params | (params or {})
        response = requests.get(url, params=params)

        if response.status_code == HTTPStatus.FORBIDDEN:
            raise ApiKeyInvalid('An invalid api_key was supplied.')

        if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:  # pragma: no cover
            raise ApiKeyLimitExceeded(
                'Too many requests, '
                'you have exceeded the request limit for your API key.'
            )

        if response.status_code == HTTPStatus.BAD_REQUEST:
            raise IncompatibleParameterFormat(
                'The provided parameter is incompatible with the expected format.'
            )

        if response.status_code == HTTPStatus.NOT_FOUND:
            raise ItemNotFound('No item found.')

        rate_limit = response.headers.get('X-RateLimit-Remaining', None)

        if rate_limit is not None:  # pragma: no cover
            self._rate_limit_remaining = int(rate_limit)

        return response.json()

    @property
    def rate_limit_remaining(self) -> int:
        """Returns the remaining number of requests to the API."""
        return self._rate_limit_remaining

    def apod(self, date: Union[dt, str, None] = None) -> Apod:
        """Get an [Astronomy Picture of Day (APOD)](http://apod.nasa.gov/apod/astropix.html) item.

        Args:
            date (Union[dt, str, None], optional): Astronomy Picture of Day Date. Defaults is the current date.

        Returns:
            Apod: Returns a dataclass containing all the APOD data.
        """
        if isinstance(date, dt):
            date = date.isoformat()
        if date is None:
            date = datetime.now().date().isoformat()

        response = self._get(Endpoint.APOD, {'date': date})
        return Apod(**response)

    def apod_timeline(
        self, start_date: Union[dt, str], end_date: Union[dt, str]
    ) -> list[Apod]:
        """Get a list of [Astronomy Picture of Day (APOD)](http://apod.nasa.gov/apod/astropix.html) items within a time range.

        Args:
            start_date (Union[dt, str]): The start of a date range.
            end_date (Union[dt, str]): The end of the date range.

        Returns:
            list[Apod]: A list containing dataclasses containing all data from all retrieved items.
        """
        if isinstance(start_date, dt):
            start_date = start_date.isoformat()
        if isinstance(end_date, dt):
            end_date = end_date.isoformat()

        response = self._get(
            Endpoint.APOD, {'start_date': start_date, 'end_date': end_date}
        )
        return [Apod(**item) for item in response]

    def apod_random(self, count: int) -> list[Apod]:
        """Get a given number of randomly chosen
        [Astronomy Picture of Day](http://apod.nasa.gov/apod/astropix.html) items.

        Args:
            count (int): Number of items to be obtained.

        Returns:
            list[Apod]: A list containing dataclasses containing
                all data from all retrieved items.
        """
        response = self._get(Endpoint.APOD, {'count': count})
        return [Apod(**item) for item in response]

    def neows_lookup(self, asteroid_id: int) -> NeoWs:
        """Lookup a specific Asteroid based on its
        [NASA JPL small body (SPK-ID) ID](http://ssd.jpl.nasa.gov/sbdb_query.cgi).

        Args:
            asteroid_id (int): SPK-ID of the asteroid in JPL Small-Body Database

        Returns:
            NeoWs: A dataclass containing all the data obtained about the asteroid
        """
        response = self._get(Endpoint.NEOWS + f'{asteroid_id}')
        return NeoWs(**response)
