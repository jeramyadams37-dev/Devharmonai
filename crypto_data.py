import requests
import pandas as pd
from datetime import datetime, timedelta
import time

class CryptoDataFetcher:
    def __init__(self):
        self.coingecko_base = "https://api.coingecko.com/api/v3"
        self.cache = {}
        self.cache_duration = 60
        
    def get_top_cryptos(self, limit=100):
        cache_key = f"top_cryptos_{limit}"
        if cache_key in self.cache:
            cached_data, cached_time = self.cache[cache_key]
            if time.time() - cached_time < self.cache_duration:
                return cached_data
        
        try:
            url = f"{self.coingecko_base}/coins/markets"
            params = {
                "vs_currency": "usd",
                "order": "market_cap_desc",
                "per_page": limit,
                "page": 1,
                "sparkline": False,
                "price_change_percentage": "1h,24h,7d"
            }
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            self.cache[cache_key] = (data, time.time())
            return data
        except Exception as e:
            print(f"Error fetching top cryptos: {e}")
            return []
    
    def get_crypto_by_id(self, crypto_id):
        try:
            url = f"{self.coingecko_base}/coins/{crypto_id}"
            params = {
                "localization": False,
                "tickers": False,
                "market_data": True,
                "community_data": True,
                "developer_data": False
            }
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching crypto {crypto_id}: {e}")
            return None
    
    def get_historical_data(self, crypto_id, days=30):
        cache_key = f"historical_{crypto_id}_{days}"
        if cache_key in self.cache:
            cached_data, cached_time = self.cache[cache_key]
            if time.time() - cached_time < self.cache_duration:
                return cached_data
        
        try:
            url = f"{self.coingecko_base}/coins/{crypto_id}/market_chart"
            params = {
                "vs_currency": "usd",
                "days": days,
                "interval": "hourly" if days <= 7 else "daily"
            }
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            df = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
            df['volume'] = [v[1] for v in data['total_volumes']]
            df['market_cap'] = [m[1] for m in data['market_caps']]
            
            self.cache[cache_key] = (df, time.time())
            return df
        except Exception as e:
            print(f"Error fetching historical data: {e}")
            return pd.DataFrame()
    
    def search_crypto(self, query):
        try:
            url = f"{self.coingecko_base}/search"
            params = {"query": query}
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json().get('coins', [])
        except Exception as e:
            print(f"Error searching crypto: {e}")
            return []
    
    def get_trending_coins(self):
        cache_key = "trending_coins"
        if cache_key in self.cache:
            cached_data, cached_time = self.cache[cache_key]
            if time.time() - cached_time < self.cache_duration:
                return cached_data
        
        try:
            url = f"{self.coingecko_base}/search/trending"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            self.cache[cache_key] = (data, time.time())
            return data
        except Exception as e:
            print(f"Error fetching trending coins: {e}")
            return {"coins": []}
    
    def get_meme_coins(self):
        meme_coin_ids = [
            'dogecoin', 'shiba-inu', 'pepe', 'floki', 'bonk', 
            'dogwifhat', 'official-trump', 'baby-doge-coin',
            'memecoin-2', 'dogelon-mars', 'samoyedcoin', 
            'mog-coin', 'turbo', 'myro'
        ]
        
        try:
            url = f"{self.coingecko_base}/coins/markets"
            params = {
                "vs_currency": "usd",
                "ids": ",".join(meme_coin_ids),
                "order": "market_cap_desc",
                "sparkline": False,
                "price_change_percentage": "1h,24h,7d"
            }
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching meme coins: {e}")
            return []
    
    def get_global_market_data(self):
        try:
            url = f"{self.coingecko_base}/global"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json().get('data', {})
        except Exception as e:
            print(f"Error fetching global market data: {e}")
            return {}

fetcher = CryptoDataFetcher()
