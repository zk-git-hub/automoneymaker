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

def get_avgprice(coin):
    """평균단가 조회"""
    avgprice = upbit.get_balances()
    for b in avgprice:
        if b['currency'] == coin:
            if b['avg_buy_price'] is not None:
                return float(b['avg_buy_price'])
            else:
                return 0

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("Autotradestart")
# 시작 메세지 슬랙 전송
post_message(myToken,"#amm", "Autotradestart: 0916_v1")
post_message(myToken,"#amm", "  비트코인-BTC // 이더리움-ETH // 비캐ABC-XEC")
time.sleep(0.3)
post_message(myToken,"#amm", "  라이트-LTC // 이클-ETC // 폴카닷-DOT")
time.sleep(0.3)
post_message(myToken,"#amm", "  체인링크-LINK // 에이다-ADA // 리플-XRP")
time.sleep(0.3)

while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(days=1)
        print("timenow")
        time.sleep(1)
        
        #오전 9:00 ~ 다음날 오전 8:56 까지 
        if start_time + datetime.timedelta(seconds=3600) < now < end_time - datetime.timedelta(seconds=200):
            # 코인종류 & k 값 설정
            krw = get_balance("KRW")

            target_price_btc = get_target_price("KRW-BTC", 0.2)
            target_price_eth = get_target_price("KRW-ETH", 0.3)
            target_price_xec = get_target_price("KRW-XEC", 0.1)
            print ("targetprice1")
            time.sleep(0.5)
            target_price_ltc = get_target_price("KRW-LTC", 0.4)
            target_price_etc = get_target_price("KRW-ETC", 0.5)
            target_price_dot = get_target_price("KRW-DOT", 0.4)
            print ("targetprice2")
            time.sleep(0.5)
            target_price_link = get_target_price("KRW-LINK", 0.3)
            target_price_ada = get_target_price("KRW-ADA", 0.4)
            target_price_xrp = get_target_price("KRW-XRP", 0.7)
            print ("targetprice3")
            time.sleep(0.5)

            btc = get_balance("BTC")
            btc_avg = get_avgprice("BTC")
            eth = get_balance("ETH")
            eth_avg = get_avgprice("ETH")
            xec = get_balance("XEC")
            xec_avg = get_avgprice("XEC")
            print ("balance1")
            time.sleep(0.5)
            ltc = get_balance("LTC")
            ltc_avg = get_avgprice("LTC")
            etc = get_balance("ETC")
            etc_avg = get_avgprice("ETC")
            dot = get_balance("DOT")
            dot_avg = get_avgprice("DOT")
            print ("balance2")
            time.sleep(0.5)
            link = get_balance("LINK")
            link_avg = get_avgprice("LINK")
            ada = get_balance("ADA")
            ada_avg = get_avgprice("ADA")
            xrp = get_balance("XRP")
            xrp_avg = get_avgprice("XRP")
            print ("balance3")
            time.sleep(0.5)

            current_price_btc = get_current_price("KRW-BTC")
            yesterday_price_btc = get_yesterday_price("KRW-BTC")
            current_price_eth = get_current_price("KRW-ETH")
            yesterday_price_eth = get_yesterday_price("KRW-ETH")
            current_price_xec = get_current_price("KRW-XEC")
            yesterday_price_xec = get_yesterday_price("KRW-XEC")
            print ("price1")
            time.sleep(0.5)
            current_price_ltc = get_current_price("KRW-LTC")
            yesterday_price_ltc = get_yesterday_price("KRW-LTC")
            current_price_etc = get_current_price("KRW-ETC")
            yesterday_price_etc = get_yesterday_price("KRW-ETC")
            current_price_dot = get_current_price("KRW-DOT")
            yesterday_price_dot = get_yesterday_price("KRW-DOT")
            print ("price2")
            time.sleep(0.5)
            current_price_link = get_current_price("KRW-LINK")
            yesterday_price_link = get_yesterday_price("KRW-LINK")
            current_price_ada = get_current_price("KRW-ADA")
            yesterday_price_ada = get_yesterday_price("KRW-ADA")
            current_price_xrp = get_current_price("KRW-XRP")
            yesterday_price_xrp = get_yesterday_price("KRW-XRP")
            print ("price3")
            time.sleep(0.5)

            #타겟 가격돌파 & 현재 가지고있는 코인 평가금이 10,000 이하 & 어제 가격보다 10%미만 상승일 때, 200,000 매수
            
            print ("buy 1-1")
            if target_price_btc < current_price_btc and 10000 > btc*current_price_btc:
                if krw > 200500 and yesterday_price_btc*1.1 > current_price_btc:
                    buy_result = upbit.buy_market_order("KRW-BTC", 200000)
                    post_message(myToken,"#amm", "BTC buy: 타겟가격 돌파_200,000")
            time.sleep(0.5)

            print ("buy 1-2")
            if target_price_eth < current_price_eth and 10000 > eth*current_price_eth:
                if krw > 200500 and yesterday_price_eth*1.1 > current_price_eth:
                    buy_result = upbit.buy_market_order("KRW-ETH", 200000)
                    post_message(myToken,"#amm", "ETH buy: 타겟가격 돌파_200,000")
            time.sleep(0.5)

            print ("buy 1-3")
            if target_price_xec < current_price_xec and 10000 > xec*current_price_xec:
                if krw > 200500 and yesterday_price_xec*1.1 > current_price_xec:
                    buy_result = upbit.buy_market_order("KRW-XEC", 200000)
                    post_message(myToken,"#amm", "XEC buy: 타겟가격 돌파_200,000")
            time.sleep(0.5)

            print ("buy 2-1")
            if target_price_ltc < current_price_ltc and 10000 > ltc*current_price_ltc:
                if krw > 200500 and yesterday_price_ltc*1.1 > current_price_ltc:
                    buy_result = upbit.buy_market_order("KRW-LTC", 200000)
                    post_message(myToken,"#amm", "LTC buy: 타겟가격 돌파_200,000")
            time.sleep(0.5)

            print ("buy 2-2")
            if target_price_etc < current_price_etc and 10000 > etc*current_price_etc:
                if krw > 200500 and yesterday_price_etc*1.1 > current_price_etc:
                    buy_result = upbit.buy_market_order("KRW-ETC", 200000)
                    post_message(myToken,"#amm", "ETC buy: 타겟가격 돌파_200,000")
            time.sleep(0.5)

            print ("buy 2-3")
            if target_price_dot < current_price_dot and 10000 > dot*current_price_dot:
                if krw > 200500 and yesterday_price_dot*1.1 > current_price_dot:
                    buy_result = upbit.buy_market_order("KRW-DOT", 200000)
                    post_message(myToken,"#amm", "DOT buy: 타겟가격 돌파_200,000")
            time.sleep(0.5)

            print ("buy 3-1")
            if target_price_link < current_price_link and 10000 > link*current_price_link:
                if krw > 200500 and yesterday_price_link*1.1 > current_price_link:
                    buy_result = upbit.buy_market_order("KRW-LINK", 200000)
                    post_message(myToken,"#amm", "LINK buy: 타겟가격 돌파_200,000")
            time.sleep(0.5)

            print ("buy 3-2")
            if target_price_ada < current_price_ada and 10000 > ada*current_price_ada:
                if krw > 200500 and yesterday_price_ada*1.1 > current_price_ada:
                    buy_result = upbit.buy_market_order("KRW-ADA", 200000)
                    post_message(myToken,"#amm", "ADA buy: 타겟가격 돌파_200,000")
            time.sleep(0.5)

            print ("buy 3-3")
            if target_price_xrp < current_price_xrp and 10000 > xrp*current_price_xrp:
                if krw > 200500 and yesterday_price_xrp*1.1 > current_price_xrp:
                    buy_result = upbit.buy_market_order("KRW-XRP", 200000)
                    post_message(myToken,"#amm", "XRP buy: 타겟가격 돌파_200,000")
            time.sleep(0.5)

            #떨어진거 줍줍 한탕 노리자 (어제보다 10%~18% 떨어지면 200,000 추가 매수)
            
            print ("gazua 1-1")
            if current_price_btc < yesterday_price_btc*0.90 and current_price_btc > yesterday_price_btc*0.82 and 200000 > btc*current_price_btc:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-BTC", 200000)
                    post_message(myToken,"#amm", "BTC buy: 종가-10%_200,000")
            time.sleep(0.5)

            print ("gazua 1-2")
            if current_price_eth < yesterday_price_eth*0.90 and current_price_eth > yesterday_price_eth*0.82 and 200000 > eth*current_price_eth:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-ETH", 200000)
                    post_message(myToken,"#amm", "ETH buy: 종가-10%_200,000")
            time.sleep(0.5)

            print ("gazua 1-3")
            if current_price_xec < yesterday_price_xec*0.90 and current_price_xec > yesterday_price_xec*0.82 and 200000 > xec*current_price_xec:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-XEC", 200000)
                    post_message(myToken,"#amm", "XEC buy: 종가-10%_200,000")
            time.sleep(0.5)

            print ("gazua 2-1")
            if current_price_ltc < yesterday_price_ltc*0.90 and current_price_ltc > yesterday_price_ltc*0.82 and 200000 > ltc*current_price_ltc:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-LTC", 200000)
                    post_message(myToken,"#amm", "LTC buy: 종가-10%_200,000")
            time.sleep(0.5)

            print ("gazua 2-2")
            if current_price_etc < yesterday_price_etc*0.90 and current_price_etc > yesterday_price_etc*0.82 and 200000 > etc*current_price_etc:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-ETC", 200000)
                    post_message(myToken,"#amm", "ETC buy: 종가-10%_200,000")
            time.sleep(0.5)

            print ("gazua 2-3")
            if current_price_dot < yesterday_price_dot*0.90 and current_price_dot > yesterday_price_dot*0.82 and 200000 > dot*current_price_dot:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-DOT", 200000)
                    post_message(myToken,"#amm", "DOT buy: 종가-10%_200,000")
            time.sleep(0.5)

            print ("gazua 3-1")
            if current_price_link < yesterday_price_link*0.90 and current_price_link > yesterday_price_link*0.82 and 200000 > link*current_price_link:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-LINK", 200000)
                    post_message(myToken,"#amm", "LINK buy: 종가-10%_200,000")
            time.sleep(0.5)

            print ("gazua 3-2")
            if current_price_ada < yesterday_price_ada*0.90 and current_price_ada > yesterday_price_ada*0.82 and 200000 > ada*current_price_ada:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-ADA", 200000)
                    post_message(myToken,"#amm", "ADA buy: 종가-10%_200,000")
            time.sleep(0.5)

            print ("gazua 3-3")
            if current_price_xrp < yesterday_price_xrp*0.90 and current_price_xrp > yesterday_price_xrp*0.82 and 200000 > xrp*current_price_xrp:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-XRP", 200000)
                    post_message(myToken,"#amm", "XRP buy: 종가-10%_200,000")
            time.sleep(0.5)

            #타겟 가격구매 후 5%이상 하락 시, 75%팔아
            
            print ("sonjul 1-1")            
            if current_price_btc < btc_avg*0.95:
                if btc*current_price_btc > 160000:
                    sell_result = upbit.sell_market_order("KRW-BTC", btc*0.75)
                    post_message(myToken,"#amm", "BTC sell: 손실 관리_75% 매도")
            time.sleep(0.5)

            print ("sonjul 1-2")            
            if current_price_eth < eth_avg*0.95:
                if eth*current_price_eth > 160000:
                    sell_result = upbit.sell_market_order("KRW-ETH", eth*0.75)
                    post_message(myToken,"#amm", "ETH sell: 손실 관리_75% 매도")
            time.sleep(0.5)

            print ("sonjul 1-3")            
            if current_price_xec < xec_avg*0.95:
                if xec*current_price_xec > 160000:
                    sell_result = upbit.sell_market_order("KRW-XEC", xec*0.75)
                    post_message(myToken,"#amm", "XEC sell: 손실 관리_75% 매도")
            time.sleep(0.5)

            print ("sonjul 2-1")            
            if current_price_ltc < ltc_avg*0.95:
                if ltc*current_price_ltc > 160000:
                    sell_result = upbit.sell_market_order("KRW-LTC", ltc*0.75)
                    post_message(myToken,"#amm", "LTC sell: 손실 관리_75% 매도")
            time.sleep(0.5)

            print ("sonjul 2-2")            
            if current_price_etc < etc_avg*0.95:
                if etc*current_price_etc > 160000:
                    sell_result = upbit.sell_market_order("KRW-ETC", etc*0.75)
                    post_message(myToken,"#amm", "ETC sell: 손실 관리_75% 매도")
            time.sleep(0.5)

            print ("sonjul 2-3")            
            if current_price_dot < dot_avg*0.95:
                if dot*current_price_dot > 160000:
                    sell_result = upbit.sell_market_order("KRW-DOT", dot*0.75)
                    post_message(myToken,"#amm", "DOT sell: 손실 관리_75% 매도")
            time.sleep(0.5)

            print ("sonjul 3-1")            
            if current_price_link < link_avg*0.95:
                if link*current_price_link > 160000:
                    sell_result = upbit.sell_market_order("KRW-LINK", link*0.75)
                    post_message(myToken,"#amm", "LINK sell: 손실 관리_75% 매도")
            time.sleep(0.5)

            print ("sonjul 3-2")            
            if current_price_ada < ada_avg*0.95:
                if ada*current_price_ada > 160000:
                    sell_result = upbit.sell_market_order("KRW-ADA", ada*0.75)
                    post_message(myToken,"#amm", "ADA sell: 손실 관리_75% 매도")
            time.sleep(0.5)

            print ("sonjul 3-3")            
            if current_price_xrp < xrp_avg*0.95:
                if xrp*current_price_xrp > 160000:
                    sell_result = upbit.sell_market_order("KRW-XRP", xrp*0.75)
                    post_message(myToken,"#amm", "XRP sell: 손실 관리_75% 매도")
            time.sleep(0.5)

            
            #어제 가격보다 20%이상 하락 시, 다팔아
            
            print ("mang 1-1")            
            if current_price_btc < yesterday_price_btc*0.8:
                if btc*current_price_btc > 5000:
                    sell_result = upbit.sell_market_order("KRW-BTC", btc*0.9995)
                    post_message(myToken,"#amm", "BTC sell: 종가-20%_전체매도")
            time.sleep(0.5)

            print ("mang 1-2")            
            if current_price_eth < yesterday_price_eth*0.8:
                if eth*current_price_eth > 5000:
                    sell_result = upbit.sell_market_order("KRW-ETH", eth*0.9995)
                    post_message(myToken,"#amm", "ETH sell: 종가-20%_전체매도")
            time.sleep(0.5)

            print ("mang 1-3")            
            if current_price_xec < yesterday_price_xec*0.8:
                if xec*current_price_xec > 5000:
                    sell_result = upbit.sell_market_order("KRW-XEC", xec*0.9995)
                    post_message(myToken,"#amm", "XEC sell: 종가-20%_전체매도")
            time.sleep(0.5)

            print ("mang 2-1")            
            if current_price_ltc < yesterday_price_ltc*0.8:
                if ltc*current_price_ltc > 5000:
                    sell_result = upbit.sell_market_order("KRW-LTC", ltc*0.9995)
                    post_message(myToken,"#amm", "LTC sell: 종가-20%_전체매도")
            time.sleep(0.5)

            print ("mang 2-2")            
            if current_price_etc < yesterday_price_etc*0.8:
                if etc*current_price_etc > 5000:
                    sell_result = upbit.sell_market_order("KRW-ETC", etc*0.9995)
                    post_message(myToken,"#amm", "ETC sell: 종가-20%_전체매도")
            time.sleep(0.5)

            print ("mang 2-3")            
            if current_price_dot < yesterday_price_dot*0.8:
                if dot*current_price_dot > 5000:
                    sell_result = upbit.sell_market_order("KRW-DOT", dot*0.9995)
                    post_message(myToken,"#amm", "DOT sell: 종가-20%_전체매도")
            time.sleep(0.5)

            print ("mang 3-1")            
            if current_price_link < yesterday_price_link*0.8:
                if link*current_price_link > 5000:
                    sell_result = upbit.sell_market_order("KRW-LINK", link*0.9995)
                    post_message(myToken,"#amm", "LINK sell: 종가-20%_전체매도")
            time.sleep(0.5)

            print ("mang 3-2")            
            if current_price_ada < yesterday_price_ada*0.8:
                if ada*current_price_ada > 5000:
                    sell_result = upbit.sell_market_order("KRW-ADA", ada*0.9995)
                    post_message(myToken,"#amm", "ADA sell: 종가-20%_전체매도")
            time.sleep(0.5)

            print ("mang 3-3")            
            if current_price_xrp < yesterday_price_xrp*0.8:
                if xrp*current_price_xrp > 5000:
                    sell_result = upbit.sell_market_order("KRW-XRP", xrp*0.9995)
                    post_message(myToken,"#amm", "XRP sell: 종가-20%_전체매도")
            time.sleep(0.5)

            
            print("done")

            
        #장마감 - 가진거 다팔아
        else:
            btc = get_balance("BTC")
            current_price_btc = get_current_price("KRW-BTC")
            time.sleep(0.5)
            if btc*current_price_btc > 5000:
                sell_result = upbit.sell_market_order("KRW-BTC", btc*0.9995)
                post_message(myToken,"#amm", "BTC sell: 장마감")

            eth = get_balance("ETH")
            current_price_eth = get_current_price("KRW-ETH")
            time.sleep(0.5)
            if eth*current_price_eth > 5000:
                sell_result = upbit.sell_market_order("KRW-ETH", eth*0.9995)
                post_message(myToken,"#amm", "ETH sell: 장마감")

            xec = get_balance("XEC")
            current_price_xec = get_current_price("KRW-XEC")
            time.sleep(0.5)
            if xec*current_price_xec > 5000:
                sell_result = upbit.sell_market_order("KRW-XEC", xec*0.9995)
                post_message(myToken,"#amm", "XEC sell: 장마감")

            ltc = get_balance("LTC")
            current_price_ltc = get_current_price("KRW-LTC")
            time.sleep(0.5)
            if ltc*current_price_ltc > 5000:
                sell_result = upbit.sell_market_order("KRW-LTC", ltc*0.9995)
                post_message(myToken,"#amm", "LTC sell: 장마감")

            etc = get_balance("ETC")
            current_price_etc = get_current_price("KRW-ETC")
            time.sleep(0.5)
            if etc*current_price_etc > 5000:
                sell_result = upbit.sell_market_order("KRW-ETC", etc*0.9995)
                post_message(myToken,"#amm", "ETC sell: 장마감")

            dot = get_balance("DOT")
            current_price_dot = get_current_price("KRW-DOT")
            time.sleep(0.5)
            if dot*current_price_dot > 5000:
                sell_result = upbit.sell_market_order("KRW-DOT", dot*0.9995)
                post_message(myToken,"#amm", "DOT sell: 장마감")

            link = get_balance("LINK")
            current_price_link = get_current_price("KRW-LINK")
            time.sleep(0.5)
            if link*current_price_link > 5000:
                sell_result = upbit.sell_market_order("KRW-LINK", link*0.9995)
                post_message(myToken,"#amm", "LINK sell: 장마감")

            ada = get_balance("ADA")
            current_price_ada = get_current_price("KRW-ADA")
            time.sleep(0.5)
            if ada*current_price_ada > 5000:
                sell_result = upbit.sell_market_order("KRW-ADA", ada*0.9995)
                post_message(myToken,"#amm", "ADA sell: 장마감")

            xrp = get_balance("XRP")
            current_price_xrp = get_current_price("KRW-XRP")
            time.sleep(0.5)
            if xrp*current_price_xrp > 5000:
                sell_result = upbit.sell_market_order("KRW-XRP", xrp*0.9995)
                post_message(myToken,"#amm", "XRP sell: 장마감")

        time.sleep(1)

    #에러메세지 출력
    except Exception as e:
        print(e)
        post_message(myToken,"#amm", e)
        time.sleep(1)

