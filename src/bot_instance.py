import os
from binance.client import Client
from src.utils import logger
from dotenv import load_dotenv

load_dotenv()

class BasicBot:
    def __init__(self, testnet=True):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")
        
        if not api_key or not api_secret:
            logger.error("API Credentials not found in .env file")
            raise Exception("Missing Credentials")

        # Initialize Client with Testnet URL handling
        self.client = Client(api_key, api_secret, testnet=testnet)
        logger.info("Binance Client Initialized on Testnet")

    def get_ticker_price(self, symbol):
        try:
            ticker = self.client.futures_symbol_ticker(symbol=symbol)
            return float(ticker['price'])
        except Exception as e:
            logger.error(f"Error fetching price: {e}")
            return None