import argparse
import sys
from src.bot_instance import BasicBot
from src.market_orders import execute_market_order
from src.limit_orders import execute_limit_order
from src.advanced.twap import execute_twap
from src.advanced.stop_loss import execute_stop_limit

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")
    
    # Global Arguments
    parser.add_argument("symbol", type=str, help="Trading Pair (e.g., BTCUSDT)")
    parser.add_argument("side", type=str, choices=["BUY", "SELL"], help="Order Side")
    parser.add_argument("type", type=str, choices=["MARKET", "LIMIT", "TWAP", "STOP_LIMIT"], help="Order Type")
    parser.add_argument("quantity", type=float, help="Order Quantity")
    
    # Optional/Specific Arguments
    parser.add_argument("--price", type=float, help="Limit Price (Required for LIMIT/STOP)")
    parser.add_argument("--stop_price", type=float, help="Stop Trigger Price (Required for STOP_LIMIT)")
    parser.add_argument("--duration", type=int, default=60, help="Duration in seconds (TWAP only)")
    parser.add_argument("--chunks", type=int, default=3, help="Number of chunks (TWAP only)")

    args = parser.parse_args()

    # Initialize Bot
    try:
        bot = BasicBot(testnet=True)
    except Exception:
        sys.exit(1)

    # Route Commands
    if args.type == "MARKET":
        execute_market_order(bot, args.symbol, args.side, args.quantity)
    
    elif args.type == "LIMIT":
        if not args.price:
            print("Error: --price is required for LIMIT orders")
            return
        execute_limit_order(bot, args.symbol, args.side, args.quantity, args.price)

    elif args.type == "STOP_LIMIT":
        if not args.price or not args.stop_price:
            print("Error: --price and --stop_price are required for STOP_LIMIT orders")
            return
        execute_stop_limit(bot, args.symbol, args.side, args.quantity, args.price, args.stop_price)

    elif args.type == "TWAP":
        execute_twap(bot, args.symbol, args.side, args.quantity, args.duration, args.chunks)

if __name__ == "__main__":
    main()