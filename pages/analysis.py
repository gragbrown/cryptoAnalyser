import streamlit as st
from pages import utility

def app():

    symbols = st.multiselect("Select Coin(s)", utility.symbols[:3000])

    # if len(symbols) == 1:
    #     df = utility.getDataBySymbol(symbols[0])
    #     name = df.iloc['name',0]
    #     symbol = df.iloc['symbol',0]
    #     marketCap = df['market_cap',0]
    #     p24h = df['percent_change_24h']
    #     volatility = df['volatility']

    #     col1, col2 = st.columns((1,1))

    #     col1.subheader(f"{symbol} {name}")
    #     col1.subheader(p24h)

    #     col2.subheader("Market Cap:")
    #     col2.write(marketCap)
    #     col2.subheader("Volatility")
    #     col2.write(volatility)


    if len(symbols):

        
        st.header("Price")
        closedf = utility.compMultiCryptoBasesAttr(symbols, "close")

        st.area_chart(closedf)

        st.header("Volume")
        volumedf = utility.compMultiCryptoBasesAttr(symbols, "volume")
        st.bar_chart(volumedf)

        st.header("Volatility")
        volatilitydf = utility.compMultiCryptoBasesAttr(symbols, "volatility")
        st.line_chart(volatilitydf)

        st.header("Percent Change 24h")
        perChange24hdf = utility.compMultiCryptoBasesAttr(symbols, "percent_change_24h")
        st.bar_chart(perChange24hdf)

        st.header("Market Dominance")
        marketdominancedf = utility.compMultiCryptoBasesAttr(symbols, "market_dominance")
        st.line_chart(marketdominancedf)
 