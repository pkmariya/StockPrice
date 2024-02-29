
import matplotlib.pyplot as plt
import streamlit as st 
import yfinance as yf
import datetime

st.title("Welcome to StockWiz!")
ticker_symbol = 'AAPL'

ticker_Data = yf.Ticker(ticker_symbol)
ticker_df = ticker_Data.history(period="1mo")

st.dataframe(ticker_df, use_container_width=True)
# st.table(ticker_df)

# for index, row in ticker_df.iterrows():
#     st.write(row)

# import streamlit as st
# import pandas as pd
# import numpy as np

# df = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))

# st.table(df)

# Line plot
plt.plot(ticker_df.index, ticker_df['Close'])
plt.title("Apple Stock - Feb 2024")
st.pyplot(plt)

st.title("Daily Low Trend")
st.line_chart(ticker_df, y='Low')

st.title("Daily High Trend")
st.line_chart(ticker_df, y='High')

dc1, dc2 = st.columns(2)
with dc1:
    start = st.date_input("Start Date", datetime.date(2022, 1, 1))
with dc2:
    end = st.date_input("End Date", datetime.date(2022, 12, 31))

ticker_df = ticker_Data.history(period="1d", start=start, end=end)

col1, col2 = st.columns(2)

with col1:
    st.header("Close Trend")
    st.line_chart(ticker_df, y='Close')

with col2:
    st.header("Volume Trend")
    st.line_chart(ticker_df, y='Volume')



