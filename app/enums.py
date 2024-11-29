from enum import Enum


class SymbolType(Enum):
    STOCK = 1
    ETF = 2
    INDICES = 3
    FOREX = 4
    COMMODITIES = 5


class Market(Enum):
    US = 1
    JP = 2


class TimeScale(Enum):
    DAILY = 1
    WEEKLY = 2
    MONTHLY = 3


class TriggerType(Enum):
    ONCE = 1
    DAILY = 2


class AlertStatus(Enum):
    ACTIVE = 1
    STOPPED = 2


class SuggestedAction(Enum):
    BUY = 1
    SELL = 2


class SuggestedTradingType(Enum):
    DAILY = 1
    SWING = 2
    LONG_TERM = 3


class NotificationStatus(Enum):
    SENT = 1
    FAILED = 2


class APIProvider(Enum):
    YAHOO_FINANCE = 1
