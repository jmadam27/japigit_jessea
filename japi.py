import urllib.request


def getStockData(symbol):
    connection = urllib.request.urlopen("https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbols="+symbol+"&apikey=KGPO51XWMFFCCH69")
    rString = connection.read().decode()
    lst = rString.split(',\n')
    price = lst[4].split(': ')
    return price[1]


def main():
    f = open('japi.out', 'w')
    while 1:
        symbol = input('Enter the symbol or quit to exit: ')
        if symbol != 'quit':
            response = 'The current price of {} is {}\n'.format(symbol, getStockData(symbol))
            print(response)
            f.write(response)
        else:
            raise SystemExit


main()
