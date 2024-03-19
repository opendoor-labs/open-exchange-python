# Standard Library
import logging
import os
import platform
from typing import Optional

# Third-Party Libraries
import requests
import requests.adapters
import urllib3.util.retry

# 1st Party Libraries
import open_exchange
from open_exchange import resources
from open_exchange.compat import cached_property
from open_exchange.contants import DEFAULT_MAX_RETRIES, DEFAULT_RETRY_BACKOFF_FACTOR, DEFAULT_RETRYABLE_STATUS_CODES
from open_exchange.exceptions import OpenExchangeError

logger = logging.getLogger(__name__)

PYTHON_VERSION = platform.python_version()
SDK_VERSION = open_exchange.__version__


class OpenExchangeClient:
    data: resources.Data

    def __init__(
        self,
        *,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
    ) -> None:
        if api_key is None:
            api_key = os.getenv("OPEN_EXCHANGE_API_KEY")
        if api_key is None:
            raise OpenExchangeError(
                'API key is required. Pass it in the "api_key" argument or set the "OPEN_EXCHANGE_API_KEY" '
                "environment variable."
            )
        self.api_key = api_key

        if base_url is None:
            base_url = "https://directaccess.opendoor.com/api/v2"
        self.base_url = base_url

        self.data = resources.Data(self)

    def _request(self, method: str, path: str, body: Optional[dict] = None) -> dict:
        session = requests.Session()
        session.mount("https://", requests.adapters.HTTPAdapter(max_retries=self._retry_config))

        response = session.request(
            method=method,
            url=f"{self.base_url}{path}",
            headers={
                "AUTHORIZATION": self.api_key,
                "X-PYTHON-VERSION": PYTHON_VERSION,
                "X-SDK-VERSION": SDK_VERSION,
            },
            json=body,
        )
        response.raise_for_status()  # Raise custom exception for HTTP errors here?
        return response.json()

    @cached_property
    def _retry_config(self) -> urllib3.util.retry.Retry:
        return urllib3.util.retry.Retry(
            total=DEFAULT_MAX_RETRIES,
            backoff_factor=DEFAULT_RETRY_BACKOFF_FACTOR,
            status_forcelist=DEFAULT_RETRYABLE_STATUS_CODES,
            # POST is not in the default set of allowed methods. Override the default to include it.
            allowed_methods=urllib3.util.retry.Retry.DEFAULT_ALLOWED_METHODS | {"POST"},
        )
