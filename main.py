from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
import os
from dotenv import  load_dotenv
# api_key = "PKT1UMLSH0XD9AIAV2PB"
# secret_key = "SY7JnhILOowabWQhUwSLYXVOwn0esyxvqPAxAXBP"
load_dotenv()
print(os.environ["api_key"])
# use paper for trading
trading_client = TradingClient(os.environ["api_key"], os.environ["api_secret"], paper=True)
# get account
account = trading_client.get_account()
market_order_data = MarketOrderRequest(
                      symbol="BTC/USD",
                      qty=0.05,
                      side=OrderSide.BUY,
                      time_in_force=TimeInForce.GTC
                  )
market_order = trading_client.submit_order(market_order_data)
for property_name, value in market_order:
  print(f"\"{property_name}\": {value}")
