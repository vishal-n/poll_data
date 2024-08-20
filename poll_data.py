import bisect
import logging
import doctest


class Stock:
    def __init__(self, symbol, price, category):
        self.symbol = symbol
        self.price = price
        self.category = category

    def __repr__(self):
        return f"Stock(symbol={self.symbol}, price={self.price}, category={self.category})"


# Hashmap / dictionary to maintain the stock price values
stock_data = {}
stocks = []


### To fetch min and max values
def get_min_max_price(symbol):
    if stock_data.get(symbol):
        current_prices = stock_data[symbol]
        return (current_prices[0], current_prices[-1])
    else:
        print("Symbol not found!")
        return None


def remove_stock():
    global stocks
    stocks = stocks[1:]


def add_new_stock(symbol, price, category):
    global stocks
    if len(stocks) < 10000:
        if symbol not in stock_data:
            stock_data[symbol] = []
        bisect.insort(stock_data[symbol], price)
    
        new_stock = Stock(symbol, price, category)
        stocks.append(new_stock)
    else:
        remove_stock()
        if symbol not in stock_data:
            stock_data[symbol] = [price]
        else:
            stock_data[symbol].append(price)
        
        new_stock = Stock(symbol, price, category)
        stocks.append(new_stock)




add_new_stock("REL", 43, "automobile")
add_new_stock("REL", 51, "automobile")
add_new_stock("xyz", 510, "test")
add_new_stock("REL", 510, "automobile")

print(get_min_max_price("REL"))
