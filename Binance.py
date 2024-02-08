from bs4 import BeautifulSoup
import requests
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}


BINANCE_URL = "https://www.binance.com/ru"
s = requests.Session()
r = requests.get(BINANCE_URL, headers=headers)
r_text = r.text

soup_binance = BeautifulSoup(r_text, "lxml")
def binance_bitcoin_price():
    binance_bitcoin = soup_binance.find(class_="coinRow-coinPrice css-1ld3mhe").text
    return binance_bitcoin

def binance_ethereum_price():
    binance_ethereum = soup_binance.find(id="top_crypto_table-2-ETH_USDT").find(class_="coinRow-coinPrice css-1ld3mhe").text
    return binance_ethereum

def binance_BNB_price():
    binance_BNB = soup_binance.find(id="top_crypto_table-3-BNB_USDT").find(class_="coinRow-coinPrice css-1ld3mhe").text
    return binance_BNB

def binance_ripple_price():
    binance_ripple = soup_binance.find(id="top_crypto_table-4-XRP_USDT").find(class_="coinRow-coinPrice css-1ld3mhe").text
    return binance_ripple
