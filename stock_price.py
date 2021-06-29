from yahoo_fin import stock_info as si


stockPrice = si.get_live_price("amzn")

print(stockPrice)