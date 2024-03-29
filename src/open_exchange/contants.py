# Standard Library
from http import HTTPStatus

DEFAULT_MAX_RETRIES = 2
DEFAULT_RETRY_BACKOFF_FACTOR = 0.1
DEFAULT_RETRYABLE_STATUS_CODES = {
    HTTPStatus.BAD_GATEWAY,  # 502 status code
    HTTPStatus.GATEWAY_TIMEOUT,  # 504 status code
    HTTPStatus.SERVICE_UNAVAILABLE,  # 503 status code
}

MAX_CONCURRENT_REQUESTS = 4

MAX_ADDRESSES_PER_PROPERTY_DETAILS_REQUEST = 50
MAX_ADDRESSES_PER_PROPERTY_VALUES_REQUEST = 50
MAX_ADDRESSES_PER_RENTAL_COMPS_REQUEST = 10
MAX_ADDRESSES_PER_RENT_ESTIMATES_REQUEST = 50
