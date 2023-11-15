import streamlit as st
import datetime
import pyupbit

d = st.date_input(
    "choose date",
    datetime.datetime.today()
)

st.write("the first day of bit coin")

ticker = "KRW-BTC"
interval = 'minute60'
to = str(d + datetime.timedelta(days=1))
count = 24
price_now = pyupbit.get_ohlcv(ticker=ticker, interval=interval, to=to, count=count)

st.line_chart(price_now.close)