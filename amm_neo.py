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

def get_yesterday_price(ticker):
    """전날 마감가"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    yesterday_price = df.iloc[0]['close']
    return yesterday_price


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
print("NEO-autotradestart")
# 시작 메세지 슬랙 전송
post_message(myToken,"#amm", "NEO-autotradestart")

while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-NEO")
        end_time = start_time + datetime.timedelta(days=1)
        
        #오전 9:00 ~ 다음날 오전 8:58 까지 
        if start_time < now < end_time - datetime.timedelta(seconds=120):
            # 코인종류 & k 값 설정
            target_price = get_target_price("KRW-NEO", 0.6)
            btc = get_balance("NEO")
            krw = get_balance("KRW")
            current_price = get_current_price("KRW-NEO")
            yesterday_price = get_yesterday_price("KRW-NEO")

            #타겟 가격돌파 & 현재 가지고있는 코인 평가금이 10,000 이하일 때, 200,000 매수
            if target_price < current_price and 10000 > btc*current_price:
                if krw > 202000:
                    buy_result = upbit.buy_market_order("KRW-NEO", 200000)
                    post_message(myToken,"#amm", "NEO buy : 타겟 구매")

            #타겟 가격보다 20%이상 상승 시, 10만원 밑으로 남기고 25%씩 매도 (마이 묵었다)
            if target_price*1.20 < current_price:
                if btc*current_price > 100000:
                    sell_result = upbit.sell_market_order("KRW-NEO", btc*0.25)
                    post_message(myToken,"#amm", "NEO sell: 익절 흐믓")

            #떨어진거 줍줍 한탕 노리자 (x%~18% 떨어지면 100,000 추가 매수)
            if current_price < yesterday_price*0.9 and current_price > yesterday_price*0.82 and 10000 > btc*current_price:
                if krw > 101000:
                    buy_result = upbit.buy_market_order("KRW-NEO", 100000)
                    post_message(myToken,"#amm", "NEO buy : 가즈아 구매")

            #어제 가격보다 20%이상 하락 시, 다팔아
            if current_price < yesterday_price*0.8:
                if btc*current_price > 5000:
                    sell_result = upbit.sell_market_order("KRW-NEO", btc*0.9995)
                    post_message(myToken,"#amm", "NEO sell all: 망했어요")
            

        #장마감 - 가진거 다팔아
        else:
            btc = get_balance("NEO")
            current_price = get_current_price("KRW-NEO")
            if btc*current_price > 5000:
                sell_result = upbit.sell_market_order("KRW-NEO", btc*0.9995)
                post_message(myToken,"#amm", "NEO sell all : 장마감")
        time.sleep(1)
    
    #에러메세지 출력
    except Exception as e:
        print(e)
        post_message(myToken,"#amm", e)
        time.sleep(1)