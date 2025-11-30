import time
from src.utils import logger
from src.market_orders import execute_market_order

def execute_twap(bot, symbol, side, total_quantity, duration_seconds, num_orders):
    """
    Time-Weighted Average Price Strategy:
    Splits total_quantity into num_orders, executed every (duration / num_orders) seconds.
    """
    logger.info(f"Starting TWAP Strategy: {side} {total_quantity} {symbol} over {duration_seconds}s")
    
    qty_per_order = round(total_quantity / num_orders, 3)
    interval = duration_seconds / num_orders

    for i in range(num_orders):
        logger.info(f"TWAP Execution {i+1}/{num_orders}")
        execute_market_order(bot, symbol, side, qty_per_order)
        
        if i < num_orders - 1:
            logger.info(f"Sleeping for {interval} seconds...")
            time.sleep(interval)
    
    logger.info("TWAP Strategy Completed.")