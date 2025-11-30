from src.utils import logger, validate_input
from binance.enums import SIDE_BUY, SIDE_SELL, TIME_IN_FORCE_GTC

def execute_stop_limit(bot, symbol, side, quantity, price, stop_price):
    try:
        validate_input(symbol, quantity, price)
        binance_side = SIDE_BUY if side.upper() == 'BUY' else SIDE_SELL
        
        logger.info(f"Placing STOP-LIMIT: Trigger at {stop_price}, Buy/Sell at {price}")
        
        # 'STOP' is the specific type string for Futures Stop-Limit orders
        order = bot.client.futures_create_order(
            symbol=symbol,
            side=binance_side,
            type='STOP', 
            timeInForce=TIME_IN_FORCE_GTC,
            quantity=quantity,
            price=str(price),
            stopPrice=str(stop_price)
        )
        logger.info(f"Stop-Limit Placed. ID: {order['orderId']}")
        return order
    except Exception as e:
        logger.error(f"Stop-Limit Failed: {e}")