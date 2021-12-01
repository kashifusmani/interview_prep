from dataclasses import dataclass, asdict


@dataclass
class Currency:
    code: str
    name: str
    symbol: str

    def to_dict(self):
        return asdict(self)


class CURRENCIES:
    # Codes
    USD = "USD"
    EUR = "EUR"
    JPY = "JPY"
    ILS = "ILS"
    AUD = "AUD"

    # Define all currencies
    __ALL__ = [
        Currency(USD, "United States Dollar", "$"),
        Currency(EUR, "Euro", "€"),
        Currency(JPY, "Japanese Yen", "¥"),
        Currency(ILS, "Israeli shekel", "₪"),
        Currency(AUD, "Australian Dollar", "A$"),
    ]
    # Organize per code for convenience
    __PER_CODE__ = {currency.code: currency for currency in __ALL__}

    @classmethod
    def get_all(cls):
        return cls.__ALL__

    @classmethod
    def get_by_code(cls, code):
        if code not in cls.__PER_CODE__:
            raise Exception(f"Currency with code={code} does not exist")
        return cls.__PER_CODE__[code]
