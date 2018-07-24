###############################################################################
## Python script to check cryptocurrency prices using API's
###############################################################################

## Using Coinmarketcap API python wrapper by github user mrsmn

import coinmarketcap

market = coinmarketcap.Market()

bitcoin = market.ticker('bitcoin', convert='ZAR')
ethereum = market.ticker("ethereum", convert='ZAR')
litecoin = market.ticker("litecoin", convert='ZAR')
ripple = market.ticker("ripple", convert='ZAR')
monero = market.ticker("monero", convert='ZAR')
vertcoin = market.ticker("vertcoin", convert='ZAR')

print('Getting current prices from Coinmarketcap.com...')

for item in bitcoin:
    BTC = float(item['price_zar'])
    print('Bitcoin (ZAR): ', BTC)

for item in ethereum:
    ETH = float(item['price_zar'])
    print('Ethereum (ZAR): ', ETH)

for item in litecoin:
    LTC = float(item['price_zar'])
    print('Litecoin (ZAR): ', LTC)

for item in ripple:
    XRP = float(item['price_zar'])
    print('Ripple (ZAR): ', XRP)

for item in monero:
    XMR = float(item['price_zar'])
    print('Monero (ZAR): ', XMR)

for item in  vertcoin:
    VTC = float(item['price_zar'])
    print('Vertcoin (ZAR): ', VTC)

print('Calculating value of current cryptocurrencies...')

## Change the below values to the amount you own

My_BTC = 10
My_ETH = 10
My_LTC = 10
My_XRP = 10
My_XMR = 10
My_VTC = 10

BTC_value = BTC * My_BTC
ETH_value = ETH * My_ETH
LTC_value = LTC * My_LTC
XRP_value = XRP * My_XRP
XMR_value = XMR * My_XMR
VTC_value = VTC * My_VTC

print('Bitcoin (ZAR)= ', BTC_value)
print('Ethereum (ZAR)= ', ETH_value)
print('Litecoin (ZAR)= ', LTC_value)
print('Ripple (ZAR)= ', XRP_value)
print('Monero (ZAR)= ', XMR_value)
print('Vertcoin (ZAR)= ', VTC_value)

print('Total Holdings (ZAR): ', BTC_value + ETH_value + LTC_value + XRP_value + XMR_value + VTC_value)
