import time
import json
import requests
import mysql.connector
while True:
    url = "https://api.binance.com/api/v3/ticker/24hr"
    response = requests.get(url)
    data_json = json.loads(response.text)
    for a in data_json:
        if a['symbol'] == "BTCUSDT":
            try:
                connector = mysql.connector.connect(host="localhost", port="3306", user="root", password="1234", database="practice")
                cursor = connector.cursor()
            except mysql.connector.Error as err:
                print(err)
            add_data = "INSERT INTO coin_price (coin_name, last_price) VALUES(%s, %s)"
            data = ("BTCUSDT", a['lastPrice'])
            try:
                cursor.execute(add_data, data)
                connector.commit()
            except mysql.connector.Error as err:
                print(err)
            cursor.close()
            connector.close()
    time.sleep(10)



#코인시세 10초에 한번씩 db insert
# import time
# while True:
#     print("hello world")
#     time.sleep(10)