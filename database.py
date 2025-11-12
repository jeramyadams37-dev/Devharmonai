import os
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

DATABASE_URL = os.getenv("DATABASE_URL")

Base = declarative_base()

engine = None
SessionLocal = None

if DATABASE_URL:
    try:
        engine = create_engine(DATABASE_URL, pool_pre_ping=True)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    except Exception as e:
        print(f"Database connection error: {str(e)}")
        engine = None
        SessionLocal = None

class Portfolio(Base):
    __tablename__ = "portfolio"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, default="default_user", index=True)
    crypto_id = Column(String, nullable=False)
    crypto_name = Column(String, nullable=False)
    crypto_symbol = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    purchase_price = Column(Float, nullable=False)
    purchase_date = Column(DateTime, default=datetime.utcnow)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Watchlist(Base):
    __tablename__ = "watchlist"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, default="default_user", index=True)
    crypto_id = Column(String, nullable=False)
    crypto_name = Column(String, nullable=False)
    crypto_symbol = Column(String, nullable=False)
    target_price = Column(Float, nullable=True)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class TradingSignal(Base):
    __tablename__ = "trading_signals"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, default="default_user", index=True)
    crypto_id = Column(String, nullable=False)
    crypto_name = Column(String, nullable=False)
    signal_type = Column(String, nullable=False)
    confidence = Column(Integer, nullable=False)
    current_price = Column(Float, nullable=False)
    target_price = Column(Float, nullable=True)
    stop_loss = Column(Float, nullable=True)
    reasoning = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    exported = Column(Boolean, default=False)

class StakingPosition(Base):
    __tablename__ = "staking_positions"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, default="default_user", index=True)
    crypto_id = Column(String, nullable=False)
    crypto_name = Column(String, nullable=False)
    crypto_symbol = Column(String, nullable=False)
    amount_staked = Column(Float, nullable=False)
    stake_price = Column(Float, nullable=False)
    apy = Column(Float, nullable=False)
    start_date = Column(DateTime, default=datetime.utcnow)
    end_date = Column(DateTime, nullable=True)
    status = Column(String, default="active")
    rewards_claimed = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)

class Podcast(Base):
    __tablename__ = "podcasts"
    
    id = Column(Integer, primary_key=True, index=True)
    episode_number = Column(Integer, nullable=False)
    week = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    episode_title = Column(String, nullable=False)
    duration_estimate = Column(String, nullable=True)
    podcast_data = Column(Text, nullable=False)
    generated_at = Column(DateTime, default=datetime.utcnow)
    published = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Subscription(Base):
    __tablename__ = "subscriptions"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, default="default_user", index=True)
    email = Column(String, nullable=False)
    subscription_type = Column(String, nullable=False)
    status = Column(String, default="trial")
    trial_start_date = Column(DateTime, nullable=True)
    trial_end_date = Column(DateTime, nullable=True)
    subscription_start_date = Column(DateTime, nullable=True)
    subscription_end_date = Column(DateTime, nullable=True)
    payment_account_info = Column(Text, nullable=True)
    disclaimer_accepted = Column(Boolean, default=False)
    disclaimer_accepted_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class DisclaimerAcceptance(Base):
    __tablename__ = "disclaimer_acceptances"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, default="default_user", index=True)
    email = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    signature = Column(String, nullable=False)
    disclaimer_text = Column(Text, nullable=False)
    ip_address = Column(String, nullable=True)
    accepted_at = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)

class AutoTradingSettings(Base):
    __tablename__ = "auto_trading_settings"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, default="default_user", index=True)
    email = Column(String, nullable=False)
    auto_trading_enabled = Column(Boolean, default=False)
    risk_level = Column(String, default="conservative")  # conservative, moderate, aggressive
    max_trade_amount = Column(Float, default=100.0)
    stop_loss_percentage = Column(Float, default=10.0)
    take_profit_percentage = Column(Float, default=20.0)
    diversification_limit = Column(Integer, default=5)  # max different coins
    waiver_accepted = Column(Boolean, default=False)
    waiver_accepted_at = Column(DateTime, nullable=True)
    education_completed = Column(Boolean, default=False)
    education_completed_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class NotificationPreferences(Base):
    __tablename__ = "notification_preferences"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, default="default_user", index=True)
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=True)
    email_notifications = Column(Boolean, default=True)
    sms_notifications = Column(Boolean, default=False)
    trade_alerts = Column(Boolean, default=True)
    auto_trade_confirmations = Column(Boolean, default=True)
    price_alerts = Column(Boolean, default=True)
    weekly_summary = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class AutoTradeHistory(Base):
    __tablename__ = "auto_trade_history"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, default="default_user", index=True)
    email = Column(String, nullable=False)
    crypto_id = Column(String, nullable=False)
    crypto_name = Column(String, nullable=False)
    crypto_symbol = Column(String, nullable=False)
    trade_type = Column(String, nullable=False)  # buy, sell
    amount = Column(Float, nullable=False)
    price = Column(Float, nullable=False)
    total_value = Column(Float, nullable=False)
    ai_reasoning = Column(Text, nullable=True)
    confidence_score = Column(Integer, nullable=True)
    notification_sent = Column(Boolean, default=False)
    executed_at = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)

def init_db():
    if engine:
        try:
            Base.metadata.create_all(bind=engine)
        except Exception as e:
            print(f"Failed to initialize database: {str(e)}")
    else:
        print("Database not configured. Portfolio features will not be available.")

def get_db():
    if not SessionLocal:
        return None
    db = SessionLocal()
    try:
        return db
    finally:
        pass

def get_database_engine():
    return engine

def get_session():
    if not SessionLocal:
        return None
    return SessionLocal()

def is_database_available():
    return engine is not None and SessionLocal is not None
