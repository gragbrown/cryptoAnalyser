import sqlite3

def createDbAndTable():
    con = sqlite3.connect('data.db')
    cur = con.cursor()

    cur.execute('''CREATE TABLE Coins
                (Symbol text, qty real, price real, totalPrice real )''')

    con.commit()
    con.close()


def add(symbol, quantity, price):
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    
    rows = read()
    con.commit()
   
    cur.execute(f"INSERT INTO Coins VALUES ('{symbol}',{quantity},{price}, {quantity*price})")
    
    con.commit()
    con.close()

def read():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM Coins")
    con.commit()
    
    rows = cur.fetchall()
    con.close()
    for row in rows:
        print(row)

    return rows

# createDbAndTable()
# add('BTC',1.0,50.20)
# data = read()
    

