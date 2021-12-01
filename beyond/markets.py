from dataclasses import dataclass, asdict
from currencies import CURRENCIES, Currency


@dataclass
class Market:
    code: str
    name: str
    currency: Currency

    def to_dict(self):
        return asdict(self)


class MARKETS:
    # Codes
    SAN_FRANCISCO = "san-francisco"
    LISBON = "lisbon"
    PARIS = "paris"
    TOKYO = "tokyo"
    JERUSALEM = "jerusalem"
    BRISBANE = "brisbane"

    # Define all markets
    __ALL__ = [
        Market(SAN_FRANCISCO, "San Francisco", CURRENCIES.USD),
        Market(LISBON, "Lisbon", CURRENCIES.EUR),
        Market(PARIS, "Paris", CURRENCIES.EUR),
        Market(TOKYO, "Tokyo", CURRENCIES.JPY),
        Market(JERUSALEM, "Jerusalem", CURRENCIES.ILS),
        Market(BRISBANE, "Brisbane", CURRENCIES.AUD),
    ]
    # Organize per code for convenience
    __PER_CODE__ = {market.code: market for market in __ALL__}

    @classmethod
    def get_all(cls):
        return cls.__ALL__

    @classmethod
    def get_by_code(cls, code):
        if code not in cls.__PER_CODE__:
            raise Exception(f"Market with code={code} does not exist")
        return cls.__PER_CODE__[code]
