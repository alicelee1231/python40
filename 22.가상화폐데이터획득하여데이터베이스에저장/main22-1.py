import pyupbit

coin_list = pyupbit.get_tickers(fiat='KRW')
print(coin_list)


#비트코인, 이더리움 한국 시세 출력
price_now = pyupbit.get_current_price(["KRW-BTC","KRW-ETH"])
print(price_now)