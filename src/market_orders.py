from src.utils import logger, validate_input
from binance.enums import SIDE_BUY, SIDE_SELL, ORDER_TYPE_MARKET

def execute_market_order(bot, symbol, side, quantity):
    try:
        validate_input(symbol, quantity)
        
        binance_side = SIDE_BUY if side.upper() == 'BUY' else SIDE_SELL
        
        logger.info(f"Submitting MARKET {binance_side} order for {quantity} {symbol}...")
        
        order = bot.client.futures_create_order(
            symbol=symbol,
            side=binance_side,
            type=ORDER_TYPE_MARKET,
            quantity=quantity
        )
        
        logger.info(f"Order Filled! ID: {order['orderId']} | Avg Price: {order.get('avgPrice', 'N/A')}")
        return order
    except Exception as e:
        logger.error(f"Market Order Failed: {e}")
        return None