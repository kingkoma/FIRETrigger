from . import db
from .enums import (
    TimeScale,
    TriggerType,
    AlertStatus,
    SymbolType,
    Market,
    NotificationStatus,
    APIProvider,
    SuggestedAction,
    SuggestedTradingType,
)


class Symbol(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    symbol = db.Column(db.String(50), nullable=False)
    market = db.Column(db.Enum(Market), nullable=False)
    type = db.Column(db.Enum(SymbolType), nullable=False)

    def __repr__(self):
        return f"<Symbol {self.name}>"


class Alert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    symbol_id = db.Column(db.Integer, db.ForeignKey("symbol.id"), nullable=False)
    condition = db.Column(
        db.String(500), nullable=False
    )  # JSON or string representation
    time_scale = db.Column(db.Enum(TimeScale), nullable=False)
    trigger_type = db.Column(db.Enum(TriggerType), nullable=False)
    status = db.Column(db.Enum(AlertStatus), nullable=False, default=AlertStatus.ACTIVE)
    start_time = db.Column(db.DateTime, default=db.func.current_timestamp())
    end_time = db.Column(db.DateTime)
    suggested_action = db.Column(db.Enum(SuggestedAction))
    suggested_trading_type = db.Column(db.Enum(SuggestedTradingType))
    memo = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp(),
    )

    def __repr__(self):
        return f"<Alert {self.name}>"


class AlertTrigger(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    alert_id = db.Column(db.Integer, db.ForeignKey("alert.id"), nullable=False)
    triggered_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    value = db.Column(db.String(500))

    def __repr__(self):
        return f"<AlertTrigger {self.id}>"


class Price(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol_id = db.Column(db.Integer, db.ForeignKey("symbol.id"), nullable=False)
    time_scale = db.Column(db.Enum(TimeScale), nullable=False)
    open = db.Column(db.Float)
    high = db.Column(db.Float)
    low = db.Column(db.Float)
    close = db.Column(db.Float)
    volume = db.Column(db.Float)
    adjusted_close = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<Price {self.id}>"


class TechnicalIndicator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol_id = db.Column(db.Integer, db.ForeignKey("symbol.id"), nullable=False)
    time_scale = db.Column(db.Enum(TimeScale), nullable=False)
    indicator = db.Column(db.String(50), nullable=False)
    value = db.Column(db.Float)

    def __repr__(self):
        return f"<Technical Indicator {self.id}>"


class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    alert_id = db.Column(db.Integer, db.ForeignKey("alert.id"), nullable=False)
    sent_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    email = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Enum(NotificationStatus), nullable=False)

    def __repr__(self):
        return f"<Notification {self.id}>"


class SymbolMapping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol_id = db.Column(db.Integer, db.ForeignKey("symbol.id"), nullable=False)
    app_symbol = db.Column(db.String(50), nullable=False)
    api_provider = db.Column(db.Enum(APIProvider), nullable=False)
    api_symbol = db.Column(db.String(50), nullable=False)
    last_updated = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f"<Symbol Mapping {self.id}>"
