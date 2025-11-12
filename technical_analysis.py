import pandas as pd
import numpy as np
import pandas_ta as ta

class TechnicalAnalyzer:
    def __init__(self):
        pass
    
    def calculate_indicators(self, df):
        if df.empty or len(df) < 20:
            return df
        
        df = df.copy()
        
        df['rsi'] = ta.rsi(df['price'], length=14)
        
        macd = ta.macd(df['price'])
        if macd is not None and not macd.empty:
            df['macd'] = macd.iloc[:, 0]
            df['macd_signal'] = macd.iloc[:, 1]
            df['macd_histogram'] = macd.iloc[:, 2]
        
        bbands = ta.bbands(df['price'], length=20)
        if bbands is not None and not bbands.empty:
            df['bb_upper'] = bbands.iloc[:, 0]
            df['bb_middle'] = bbands.iloc[:, 1]
            df['bb_lower'] = bbands.iloc[:, 2]
        
        df['sma_20'] = ta.sma(df['price'], length=20)
        df['sma_50'] = ta.sma(df['price'], length=50)
        df['ema_12'] = ta.ema(df['price'], length=12)
        df['ema_26'] = ta.ema(df['price'], length=26)
        
        df['volume_sma'] = ta.sma(df['volume'], length=20)
        
        return df
    
    def calculate_momentum_indicators(self, df):
        if df.empty or len(df) < 14:
            return {}
        
        df = df.copy()
        
        latest_price = df['price'].iloc[-1]
        
        if 'rsi' not in df.columns or df['rsi'].isna().all():
            df['rsi'] = ta.rsi(df['price'], length=14)
        
        rsi_value = df['rsi'].iloc[-1] if not df['rsi'].isna().all() else 50
        
        macd_data = ta.macd(df['price'])
        macd_trend = "Neutral"
        if macd_data is not None and not macd_data.empty:
            macd_value = macd_data.iloc[-1, 0]
            macd_signal = macd_data.iloc[-1, 1]
            if macd_value > macd_signal:
                macd_trend = "Bullish"
            elif macd_value < macd_signal:
                macd_trend = "Bearish"
        
        volume_avg = df['volume'].tail(20).mean()
        current_volume = df['volume'].iloc[-1]
        volume_ratio = current_volume / volume_avg if volume_avg > 0 else 1
        
        price_change_24h = ((latest_price - df['price'].iloc[-24]) / df['price'].iloc[-24] * 100) if len(df) >= 24 else 0
        
        sma_50 = ta.sma(df['price'], length=50)
        trend = "Neutral"
        if sma_50 is not None and not sma_50.isna().all():
            sma_50_value = sma_50.iloc[-1]
            if latest_price > sma_50_value * 1.02:
                trend = "Uptrend"
            elif latest_price < sma_50_value * 0.98:
                trend = "Downtrend"
        
        return {
            "rsi": round(rsi_value, 2),
            "rsi_signal": "Overbought" if rsi_value > 70 else "Oversold" if rsi_value < 30 else "Neutral",
            "macd_trend": macd_trend,
            "volume_ratio": round(volume_ratio, 2),
            "volume_signal": "High" if volume_ratio > 1.5 else "Normal" if volume_ratio > 0.5 else "Low",
            "price_change_24h": round(price_change_24h, 2),
            "trend": trend
        }
    
    def detect_patterns(self, df):
        if df.empty or len(df) < 50:
            return []
        
        patterns = []
        
        latest_price = df['price'].iloc[-1]
        
        if 'sma_20' not in df.columns:
            df['sma_20'] = ta.sma(df['price'], length=20)
        if 'sma_50' not in df.columns:
            df['sma_50'] = ta.sma(df['price'], length=50)
        
        sma_20 = df['sma_20'].iloc[-1] if not df['sma_20'].isna().all() else latest_price
        sma_50 = df['sma_50'].iloc[-1] if not df['sma_50'].isna().all() else latest_price
        sma_20_prev = df['sma_20'].iloc[-2] if len(df) > 1 and not df['sma_20'].isna().all() else sma_20
        sma_50_prev = df['sma_50'].iloc[-2] if len(df) > 1 and not df['sma_50'].isna().all() else sma_50
        
        if sma_20_prev < sma_50_prev and sma_20 > sma_50:
            patterns.append({
                "pattern": "Golden Cross",
                "description": "Bullish signal - SMA 20 crossed above SMA 50",
                "signal": "Strong Buy"
            })
        
        if sma_20_prev > sma_50_prev and sma_20 < sma_50:
            patterns.append({
                "pattern": "Death Cross",
                "description": "Bearish signal - SMA 20 crossed below SMA 50",
                "signal": "Strong Sell"
            })
        
        if 'bb_upper' in df.columns and 'bb_lower' in df.columns:
            bb_upper = df['bb_upper'].iloc[-1]
            bb_lower = df['bb_lower'].iloc[-1]
            
            if latest_price >= bb_upper:
                patterns.append({
                    "pattern": "Bollinger Band Breakout",
                    "description": "Price touched upper band - potential overbought",
                    "signal": "Caution"
                })
            
            if latest_price <= bb_lower:
                patterns.append({
                    "pattern": "Bollinger Band Support",
                    "description": "Price touched lower band - potential oversold",
                    "signal": "Buy Opportunity"
                })
        
        recent_high = df['price'].tail(20).max()
        recent_low = df['price'].tail(20).min()
        
        if latest_price >= recent_high * 0.99:
            patterns.append({
                "pattern": "Near Resistance",
                "description": "Price approaching 20-period high",
                "signal": "Watch for breakout"
            })
        
        if latest_price <= recent_low * 1.01:
            patterns.append({
                "pattern": "Near Support",
                "description": "Price approaching 20-period low",
                "signal": "Potential bounce"
            })
        
        return patterns
    
    def calculate_support_resistance(self, df, num_levels=3):
        if df.empty or len(df) < 50:
            return {"support": [], "resistance": []}
        
        prices = df['price'].values
        
        local_max = []
        local_min = []
        
        for i in range(5, len(prices) - 5):
            if prices[i] == max(prices[i-5:i+6]):
                local_max.append(prices[i])
            if prices[i] == min(prices[i-5:i+6]):
                local_min.append(prices[i])
        
        from collections import Counter
        
        def cluster_levels(levels, tolerance=0.02):
            if not levels:
                return []
            
            clustered = []
            sorted_levels = sorted(levels)
            current_cluster = [sorted_levels[0]]
            
            for level in sorted_levels[1:]:
                if level <= current_cluster[-1] * (1 + tolerance):
                    current_cluster.append(level)
                else:
                    clustered.append(np.mean(current_cluster))
                    current_cluster = [level]
            
            clustered.append(np.mean(current_cluster))
            return clustered
        
        resistance_levels = cluster_levels(local_max)[-num_levels:]
        support_levels = cluster_levels(local_min)[-num_levels:]
        
        return {
            "support": sorted(support_levels),
            "resistance": sorted(resistance_levels, reverse=True)
        }

analyzer = TechnicalAnalyzer()
