import streamlit as st
import utility
import json
import sqlite3

def createDbAndTable():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE Coins
                (symbol varchar(20), qty real, price real, totalprice real)''')
    con.commit()
    con.close()

createDbAndTable()

# def add(symbol, quantity, price,totalprice):
#     con = sqlite3.connect('data.db')
#     cur = con.cursor()    
#     cur.execute("SELECT * FROM Coins")
#     rows = cur.fetchall()
#     for row in rows:
#         if symbol in row:
#             totalprice+=row[3]
#             price = (row[1]*row[2] + quantity*price)/(row[1] + quantity)
#             qty+=row[1]
#     cur.execute("INSERT INTO Coins VALUES ({},{},{},{})".format(symbol, quantity, price,totalprice))
#     con.commit()
#     con.close()

# def deletetable():
#     con = sqlite3.connect('data.db')
#     cur = con.cursor()
#     cur.execute('Drop Table Coins'); 
#     con.commit()
#     con.close()  

# def app():
#     st.write("Portfolio")
#     coins = {}
#     with st.form("Add To Portfolio", clear_on_submit=False): 
#         with st.expander("Add To Portfolio", expanded=False):
#             col1, col2, col3 = st.columns(3)

#             with col1:
#                 coin = st.selectbox("Coin", utility.symbols[:3000])

#             with col2:
#                 quantity = st.number_input('Quantity')

#             with col3:
#                 price = st.number_input('Price')

#             submitted = st.form_submit_button("Add")
        
#         # createDbAndTable()
#         if submitted:
#             add(coin,quantity,price,quantity*price)
#         # deletetable()