from src.utils import logger, validate_input
from binance.enums import SIDE_BUY, SIDE_SELL, ORDER_TYPE_LIMIT, TIME_IN_FORCE_GTC

def execute_limit_order(bot, symbol, side, quantity, price):
    try:
        validate_input(symbol, quantity, price)
        
        binance_side = SIDE_BUY if side.upper() == 'BUY' else SIDE_SELL
        
        logger.info(f"Submitting LIMIT {binance_side} order: {quantity} {symbol} @ ${price}")
        
        order = bot.client.futures_create_order(
            symbol=symbol,
            side=binance_side,
            type=ORDER_TYPE_LIMIT,
            timeInForce=TIME_IN_FORCE_GTC, # Good Till Cancelled
            quantity=quantity,
            price=str(price)
        )
        
        logger.info(f"Limit Order Placed. ID: {order['orderId']} | Status: {order['status']}")
        return order
    except Exception as e:
        logger.error(f"Limit Order Failed: {e}")
        return None