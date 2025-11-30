import logging
import os

# Setup Logging
def setup_logger():
    # Create a custom logger
    logger = logging.getLogger("BinanceBot")
    logger.setLevel(logging.INFO)

    # Create handlers
    c_handler = logging.StreamHandler() # Console output
    f_handler = logging.FileHandler('bot.log') # File output

    # Create formatters and add it to handlers
    c_format = logging.Formatter('%(levelname)s - %(message)s')
    f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    if not logger.handlers:
        logger.addHandler(c_handler)
        logger.addHandler(f_handler)

    return logger

logger = setup_logger()

def validate_input(symbol, qty, price=None):
    if qty <= 0:
        raise ValueError("Quantity must be greater than 0.")
    if price is not None and price <= 0:
        raise ValueError("Price must be greater than 0.")
    if not symbol.endswith("USDT"):
        logger.warning(f"Symbol {symbol} does not end in USDT. Ensure this is correct.")