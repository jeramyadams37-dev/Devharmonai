from database import Portfolio, Watchlist, TradingSignal, StakingPosition, get_session, init_db, is_database_available
from crypto_data import fetcher
from sqlalchemy import func
from datetime import datetime

if is_database_available():
    init_db()

class WalletManager:
    def __init__(self, user_id="default_user"):
        self.user_id = user_id
    
    def add_holding(self, crypto_id, crypto_name, crypto_symbol, amount, purchase_price, purchase_date=None, notes=None):
        session = get_session()
        if not session:
            return False
        try:
            holding = Portfolio(
                user_id=self.user_id,
                crypto_id=crypto_id,
                crypto_name=crypto_name,
                crypto_symbol=crypto_symbol,
                amount=amount,
                purchase_price=purchase_price,
                purchase_date=purchase_date or datetime.utcnow(),
                notes=notes
            )
            session.add(holding)
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            print(f"Error adding holding: {e}")
            return False
        finally:
            session.close()
    
    def get_all_holdings(self):
        session = get_session()
        if not session:
            return []
        try:
            holdings = session.query(Portfolio).filter_by(user_id=self.user_id).all()
            return holdings
        finally:
            session.close()
    
    def delete_holding(self, holding_id):
        session = get_session()
        if not session:
            return False
        try:
            holding = session.query(Portfolio).filter_by(id=holding_id, user_id=self.user_id).first()
            if holding:
                session.delete(holding)
                session.commit()
                return True
            return False
        except Exception as e:
            session.rollback()
            print(f"Error deleting holding: {e}")
            return False
        finally:
            session.close()
    
    def get_portfolio_value(self):
        holdings = self.get_all_holdings()
        total_value = 0
        total_cost = 0
        portfolio_items = []
        
        for holding in holdings:
            try:
                crypto_data = fetcher.get_crypto_by_id(holding.crypto_id)
                if crypto_data:
                    current_price = crypto_data.get('market_data', {}).get('current_price', {}).get('usd', 0)
                    current_value = holding.amount * current_price
                    cost_basis = holding.amount * holding.purchase_price
                    profit_loss = current_value - cost_basis
                    profit_loss_pct = (profit_loss / cost_basis * 100) if cost_basis > 0 else 0
                    
                    portfolio_items.append({
                        'id': holding.id,
                        'crypto_id': holding.crypto_id,
                        'name': holding.crypto_name,
                        'symbol': holding.crypto_symbol,
                        'amount': holding.amount,
                        'purchase_price': holding.purchase_price,
                        'current_price': current_price,
                        'cost_basis': cost_basis,
                        'current_value': current_value,
                        'profit_loss': profit_loss,
                        'profit_loss_pct': profit_loss_pct,
                        'purchase_date': holding.purchase_date,
                        'notes': holding.notes
                    })
                    
                    total_value += current_value
                    total_cost += cost_basis
            except Exception as e:
                print(f"Error fetching data for {holding.crypto_name}: {e}")
        
        total_profit_loss = total_value - total_cost
        total_profit_loss_pct = (total_profit_loss / total_cost * 100) if total_cost > 0 else 0
        
        return {
            'items': portfolio_items,
            'total_value': total_value,
            'total_cost': total_cost,
            'total_profit_loss': total_profit_loss,
            'total_profit_loss_pct': total_profit_loss_pct
        }
    
    def add_to_watchlist(self, crypto_id, crypto_name, crypto_symbol, target_price=None, notes=None):
        session = get_session()
        if not session:
            return False
        try:
            existing = session.query(Watchlist).filter_by(
                user_id=self.user_id,
                crypto_id=crypto_id
            ).first()
            
            if existing:
                return False
            
            watchlist_item = Watchlist(
                user_id=self.user_id,
                crypto_id=crypto_id,
                crypto_name=crypto_name,
                crypto_symbol=crypto_symbol,
                target_price=target_price,
                notes=notes
            )
            session.add(watchlist_item)
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            print(f"Error adding to watchlist: {e}")
            return False
        finally:
            session.close()
    
    def get_watchlist(self):
        session = get_session()
        if not session:
            return []
        try:
            items = session.query(Watchlist).filter_by(user_id=self.user_id).all()
            return items
        finally:
            session.close()
    
    def remove_from_watchlist(self, watchlist_id):
        session = get_session()
        if not session:
            return False
        try:
            item = session.query(Watchlist).filter_by(id=watchlist_id, user_id=self.user_id).first()
            if item:
                session.delete(item)
                session.commit()
                return True
            return False
        except Exception as e:
            session.rollback()
            print(f"Error removing from watchlist: {e}")
            return False
        finally:
            session.close()
    
    def save_trading_signal(self, crypto_id, crypto_name, signal_type, confidence, current_price, 
                           target_price=None, stop_loss=None, reasoning=None):
        session = get_session()
        if not session:
            return False
        try:
            signal = TradingSignal(
                user_id=self.user_id,
                crypto_id=crypto_id,
                crypto_name=crypto_name,
                signal_type=signal_type,
                confidence=confidence,
                current_price=current_price,
                target_price=target_price,
                stop_loss=stop_loss,
                reasoning=reasoning
            )
            session.add(signal)
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            print(f"Error saving trading signal: {e}")
            return False
        finally:
            session.close()
    
    def get_trading_signals(self, limit=50):
        session = get_session()
        if not session:
            return []
        try:
            signals = session.query(TradingSignal).filter_by(user_id=self.user_id).order_by(
                TradingSignal.created_at.desc()
            ).limit(limit).all()
            return signals
        finally:
            session.close()

    def create_staking_position(self, crypto_id, crypto_name, crypto_symbol, amount_staked, stake_price, apy):
        session = get_session()
        if not session:
            return False
        try:
            position = StakingPosition(
                user_id=self.user_id,
                crypto_id=crypto_id,
                crypto_name=crypto_name,
                crypto_symbol=crypto_symbol,
                amount_staked=amount_staked,
                stake_price=stake_price,
                apy=apy,
                status="active"
            )
            session.add(position)
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            print(f"Error creating staking position: {e}")
            return False
        finally:
            session.close()
    
    def get_staking_positions(self, status="active"):
        session = get_session()
        if not session:
            return []
        try:
            if status == "all":
                positions = session.query(StakingPosition).filter_by(user_id=self.user_id).all()
            else:
                positions = session.query(StakingPosition).filter_by(user_id=self.user_id, status=status).all()
            return positions
        finally:
            session.close()
    
    def unstake_position(self, position_id):
        session = get_session()
        if not session:
            return False
        try:
            position = session.query(StakingPosition).filter_by(id=position_id, user_id=self.user_id).first()
            if position and position.status == "active":
                position.status = "unstaked"
                position.end_date = datetime.utcnow()
                session.commit()
                return True
            return False
        except Exception as e:
            session.rollback()
            print(f"Error unstaking position: {e}")
            return False
        finally:
            session.close()
    
    def calculate_staking_rewards(self, position):
        if position.status != "active":
            return 0.0
        
        from datetime import datetime
        now = datetime.utcnow()
        time_staked = (now - position.start_date).total_seconds() / (365.25 * 24 * 3600)
        
        rewards = position.amount_staked * (position.apy / 100) * time_staked
        return rewards

wallet_manager = WalletManager()
