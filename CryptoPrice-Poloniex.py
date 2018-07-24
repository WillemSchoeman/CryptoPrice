###############################################################################
## Python script to check cryptocurrency prices using API's
###############################################################################

## Using Poloniex API python wrapper by github user s4w3d0ff

from poloniex import Poloniex
polo = Poloniex()

bitcoin = polo.returnTicker()['USDT_BTC']
ethereum = polo.returnTicker()['USDT_ETH']
litecoin = polo.returnTicker()['USDT_LTC']
ripple = polo.returnTicker()['USDT_XRP']
monero = polo.returnTicker()['USDT_XMR']

BTC = float(bitcoin.get('last'))
ETH = float(ethereum.get('last'))
LTC = float(litecoin.get('last'))
XRP = float(ripple.get('last'))
XMR = float(monero.get('last'))

print('Getting current prices from Poloniex.com...')
print('Bitcoin (USD): ', BTC)
print('Ethereum (USD): ', ETH)
print('Litecoin (USD): ', LTC)
print('Ripple (USD): ', XRP)
print('Monero (USD): ', XMR)

print('Calculating value of current cryptocurrencies...')

## Change the values below to the amount you own.

My_BTC = 10
My_ETH = 10
My_LTC = 10
My_XRP = 10
My_XMR = 10

BTC_value = BTC * My_BTC
ETH_value = ETH * My_ETH
LTC_value = LTC * My_LTC
XRP_value = XRP * My_XRP
XMR_value = XMR * My_XMR

print('Bitcoin (USD)= ', BTC_value)
print('Ethereum (USD)= ', ETH_value)
print('Litecoin (USD)= ', LTC_value)
print('Ripple (USD)= ', XRP_value)
print('Monero (USD)= ', XMR_value)

print('Total Holdings (USD): ', BTC_value + ETH_value + LTC_value + XRP_value + XMR_value)
print('Estimated Rand Value at R11.60/$: ', (BTC_value + ETH_value + LTC_value + XRP_value + XMR_value)*float(11.60))


