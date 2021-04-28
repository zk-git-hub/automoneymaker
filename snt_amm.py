import time
import pyupbit
import datetime
import requests

access = "mRqsuThtvvMM1zjixsM8oTRi3Z4AglepTlXkheje"
secret = "gTy5pvLJfNVsK2fpDMHIQIzYtifpKEhbczLmJmyT"
myToken = "xoxb-1992218678086-1998997054034-smkHJ0NLCOqLj69z5TbmHeFW"

def post_message(token, channel, text):
    """슬랙 메시지 전송"""
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )

def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

# def get_ma15(ticker):
#     """15일 이동 평균선 조회"""
#     df = pyupbit.get_ohlcv(ticker, interval="day", count=15)
#     ma15 = df['close'].rolling(15).mean().iloc[-1]
#     return ma15

def get_balance(coin):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == coin:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("SNT-autotradestart")
# 시작 메세지 슬랙 전송
post_message(myToken,"#amm", "SNT-autotradestart")

while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-SNT")
        end_time = start_time + datetime.timedelta(days=1)

        if start_time < now < end_time - datetime.timedelta(seconds=120):
            target_price = get_target_price("KRW-SNT", 0.1)
            btc = get_balance("SNT")
            krw = get_balance("KRW")
            current_price = get_current_price("KRW-SNT")
            if target_price < current_price and krw > 5*btc*current_price and target_price*1.15 > current_price:             
                krw = get_balance("KRW")
                if krw > 5000:
                    buy_result = upbit.buy_market_order("KRW-SNT", krw*0.3)
                    post_message(myToken,"#amm", "SNT buy : 보유금액 30%")
            if target_price*1.18 < current_price:
                btc = get_balance("SNT")
                krw = get_balance("KRW")
                current_price = get_current_price("KRW-SNT")
                if btc*current_price > 200000:
                    sell_result = upbit.sell_market_order("KRW-SNT", btc*0.25)
                    post_message(myToken,"#amm", "SNT sell on profit: 보유코인 25%")
        else:
            btc = get_balance("SNT")
            current_price = get_current_price("KRW-SNT")
            if btc*current_price > 5000:
                sell_result = upbit.sell_market_order("KRW-SNT", btc*0.9995)
                post_message(myToken,"#amm", "SNT sell all : 장마감")
        time.sleep(1)
    except Exception as e:
        print(e)
        post_message(myToken,"#amm", e)
        time.sleep(1)
