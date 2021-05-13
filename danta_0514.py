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
post_message(myToken,"#amm", "Project Danta_test")


while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(days=1)
        print("timenow")
        time.sleep(1)
        
        #오전 9:00 ~ 다음날 오전 8:56 까지 
        if start_time < now < end_time - datetime.timedelta(seconds=200):
            
            krw = get_balance("KRW")

            ##### 코인 1 #####
            print ("coin 1")
            doge = get_balance("DOGE")        
            doge_avg = get_avgprice("DOGE")
            current_price_doge = get_current_price("KRW-DOGE")
            yesterday_price_doge = get_yesterday_price("KRW-DOGE")
            
            #어제 종가 90% 이상, 가진 코인 없을때, 평단가보다 현재가가 낮을 때
            print ("buy 1")
            if current_price_doge > yesterday_price_doge*0.90 and 10000 > doge*doge_avg and (doge_avg*0.98 > current_price_doge or doge_avg*1.01 < current_price_doge) :
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-DOGE", 200000)
                    post_message(myToken,"#amm", "DOGE buy: 200,000")
            time.sleep(0.5)

            #어제 종가 90% 이상, 평단보다 추가 2% 이상 떨어졌을때, 가진 코인 있을때 
            print ("add 1")
            if current_price_doge > yesterday_price_doge*0.90 and doge_avg*0.98 > current_price_doge and 200000 < doge*doge_avg and 390000 > doge*doge_avg:
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-DOGE", 200000)
                    post_message(myToken,"#amm", "DOGE add: 200,000")
            time.sleep(0.5)

            #평단가 2%이상 상승 시, 팔아
            print ("sell 1")
            if doge_avg*1.02 < current_price_doge:
                if doge*current_price_doge > 5000:
                    sell_result = upbit.sell_market_order("KRW-DOGE", doge*0.9995)
                    post_message(myToken,"#amm", "DOGE sell: +2% 익절")
            time.sleep(0.5)

            #평단가 5%이상 하락시, 팔아
            print ("sonjul 1")
            if doge_avg*0.95 > current_price_doge:
                if doge*current_price_doge > 5000:
                    sell_result = upbit.sell_market_order("KRW-DOGE", doge*0.9995)
                    post_message(myToken,"#amm", "DOGE sell: -5% 손절")
            time.sleep(0.5)

            ##### 코인 2 #####
            print ("coin 2")
            eth = get_balance("ETH")        
            eth_avg = get_avgprice("ETH")
            current_price_eth = get_current_price("KRW-ETH")
            yesterday_price_eth = get_yesterday_price("KRW-ETH")
            
            #어제 종가 90% 이상, 가진 코인 없을때, 평단가보다 현재가가 낮을 때
            print ("buy 2")
            if current_price_eth > yesterday_price_eth*0.90 and 10000 > eth*eth_avg and (eth_avg*0.98 > current_price_eth or eth_avg*1.01 < current_price_eth) :
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-ETH", 200000)
                    post_message(myToken,"#amm", "ETH buy: 200,000")
            time.sleep(0.5)

            #어제 종가 90% 이상, 평단보다 추가 2% 이상 떨어졌을때, 가진 코인 있을때 
            print ("add 2")
            if current_price_eth > yesterday_price_eth*0.90 and eth_avg*0.98 > current_price_eth and 200000 < eth*eth_avg and 390000 > eth*eth_avg:
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-ETH", 200000)
                    post_message(myToken,"#amm", "ETH add: 200,000")
            time.sleep(0.5)

            #평단가 2%이상 상승 시, 팔아
            print ("sell 2")
            if eth_avg*1.02 < current_price_eth:
                if eth*current_price_eth > 5000:
                    sell_result = upbit.sell_market_order("KRW-ETH", eth*0.9995)
                    post_message(myToken,"#amm", "ETH sell: +2% 익절")
            time.sleep(0.5)

            #평단가 5%이상 하락시, 팔아
            print ("sonjul 2")
            if eth_avg**0.95 > current_price_eth:
                if eth*current_price_eth > 5000:
                    sell_result = upbit.sell_market_order("KRW-ETH", eth*0.9995)
                    post_message(myToken,"#amm", "ETH sell: -5% 손절")
            time.sleep(0.5)

            ##### 코인 3 #####
            print ("coin 3")
            eos = get_balance("EOS")        
            eos_avg = get_avgprice("EOS")
            current_price_eos = get_current_price("KRW-EOS")
            yesterday_price_eos = get_yesterday_price("KRW-EOS")
            
            #어제 종가 90% 이상, 가진 코인 없을때, 평단가보다 현재가가 낮을 때
            print ("buy 3")
            if current_price_eos > yesterday_price_eos*0.90 and 10000 > eos*eos_avg and (eos_avg*0.98 > current_price_eos or eos_avg*1.01 < current_price_eos) :
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-EOS", 200000)
                    post_message(myToken,"#amm", "EOS buy: 200,000")
            time.sleep(0.5)

            #어제 종가 90% 이상, 평단보다 추가 2% 이상 떨어졌을때, 가진 코인 있을때 
            print ("add 3")
            if current_price_eos > yesterday_price_eos*0.90 and eos_avg*0.98 > current_price_eos and 200000 < eos*eos_avg and 390000 > eos*eos_avg:
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-EOS", 200000)
                    post_message(myToken,"#amm", "EOS add: 200,000")
            time.sleep(0.5)

            #평단가 2%이상 상승 시, 팔아
            print ("sell 3")
            if eos_avg*1.02 < current_price_eos:
                if eos*current_price_eos > 5000:
                    sell_result = upbit.sell_market_order("KRW-EOS", eos*0.9995)
                    post_message(myToken,"#amm", "EOS sell: +2% 익절")
            time.sleep(0.5)

            #평단가 5%이상 하락시, 팔아
            print ("sonjul 3")
            if eos_avg**0.95 > current_price_eos:
                if eos*current_price_eos > 5000:
                    sell_result = upbit.sell_market_order("KRW-EOS", eos*0.9995)
                    post_message(myToken,"#amm", "EOS sell: -5% 손절")
            time.sleep(0.5)

            ##### 코인 4 #####
            print ("coin 4")
            etc = get_balance("ETC")        
            etc_avg = get_avgprice("ETC")
            current_price_etc = get_current_price("KRW-ETC")
            yesterday_price_etc = get_yesterday_price("KRW-ETC")
            
            #어제 종가 90% 이상, 가진 코인 없을때, 평단가보다 현재가가 낮을 때
            print ("buy 4")
            if current_price_etc > yesterday_price_etc*0.90 and 10000 > etc*etc_avg and (etc_avg*0.98 > current_price_etc or etc_avg*1.01 < current_price_etc) :
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-ETC", 200000)
                    post_message(myToken,"#amm", "ETC buy: 200,000")
            time.sleep(0.5)

            #어제 종가 90% 이상, 평단보다 추가 2% 이상 떨어졌을때, 가진 코인 있을때 
            print ("add 4")
            if current_price_etc > yesterday_price_etc*0.90 and etc_avg*0.98 > current_price_etc and 200000 < etc*etc_avg and 390000 > etc*etc_avg:
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-ETC", 200000)
                    post_message(myToken,"#amm", "ETC add: 200,000")
            time.sleep(0.5)

            #평단가 2%이상 상승 시, 팔아
            print ("sell 4")
            if etc_avg*1.02 < current_price_etc:
                if etc*current_price_etc > 5000:
                    sell_result = upbit.sell_market_order("KRW-ETC", etc*0.9995)
                    post_message(myToken,"#amm", "ETC sell: +2% 익절")
            time.sleep(0.5)

            #평단가 5%이상 하락시, 팔아
            print ("sonjul 4")
            if etc_avg**0.95 > current_price_etc:
                if etc*current_price_etc > 5000:
                    sell_result = upbit.sell_market_order("KRW-ETC", etc*0.9995)
                    post_message(myToken,"#amm", "ETC sell: -5% 손절")
            time.sleep(0.5)

            ##### 코인 5 #####
            print ("coin 5")
            xrp = get_balance("XRP")        
            xrp_avg = get_avgprice("XRP")
            current_price_xrp = get_current_price("KRW-XRP")
            yesterday_price_xrp = get_yesterday_price("KRW-XRP")
            
            #어제 종가 90% 이상, 가진 코인 없을때, 평단가보다 현재가가 낮을 때
            print ("buy 5")
            if current_price_xrp > yesterday_price_xrp*0.90 and 10000 > xrp*xrp_avg and (xrp_avg*0.98 > current_price_xrp or xrp_avg*1.01 < current_price_xrp) :
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-XRP", 200000)
                    post_message(myToken,"#amm", "XRP buy: 200,000")
            time.sleep(0.5)

            #어제 종가 90% 이상, 평단보다 추가 2% 이상 떨어졌을때, 가진 코인 있을때 
            print ("add 5")
            if current_price_xrp > yesterday_price_xrp*0.90 and xrp_avg*0.98 > current_price_xrp and 200000 < xrp*xrp_avg and 390000 > xrp*xrp_avg:
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-XRP", 200000)
                    post_message(myToken,"#amm", "XRP add: 200,000")
            time.sleep(0.5)

            #평단가 2%이상 상승 시, 팔아
            print ("sell 5")
            if xrp_avg*1.02 < current_price_xrp:
                if xrp*current_price_xrp > 5000:
                    sell_result = upbit.sell_market_order("KRW-XRP", xrp*0.9995)
                    post_message(myToken,"#amm", "XRP sell: +2% 익절")
            time.sleep(0.5)

            #평단가 5%이상 하락시, 팔아
            print ("sonjul 5")
            if xrp_avg*0.95 > current_price_xrp:
                if xrp*current_price_xrp > 5000:
                    sell_result = upbit.sell_market_order("KRW-XRP", xrp*0.9995)
                    post_message(myToken,"#amm", "XRP sell: -5% 손절")
            time.sleep(0.5)

            # 코인 6
            print ("coin 6")
            btc = get_balance("BTC")        
            btc_avg = get_avgprice("BTC")
            current_price_btc = get_current_price("KRW-BTC")
            yesterday_price_btc = get_yesterday_price("KRW-BTC")
            
            #어제 종가 90% 이상, 가진 코인 없을때, 평단가보다 현재가가 낮을 때
            print ("buy 6")
            if current_price_btc > yesterday_price_btc*0.90 and 10000 > btc*btc_avg and (btc_avg*0.98 > current_price_btc or btc_avg*1.01 < current_price_btc) :
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-BTC", 200000)
                    post_message(myToken,"#amm", "BTC buy: 200,000")
            time.sleep(0.5)

            #어제 종가 90% 이상, 평단보다 추가 2% 이상 떨어졌을때, 가진 코인 있을때 
            print ("add 6")
            if current_price_btc > yesterday_price_btc*0.90 and btc_avg*0.98 > current_price_btc and 200000 < btc*btc_avg and 390000 > btc*btc_avg:
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-BTC", 200000)
                    post_message(myToken,"#amm", "BTC add: 200,000")
            time.sleep(0.5)

            #평단가 2%이상 상승 시, 팔아
            print ("sell 6")
            if btc_avg*1.02 < current_price_btc:
                if btc*current_price_btc > 5000:
                    sell_result = upbit.sell_market_order("KRW-BTC", btc*0.9995)
                    post_message(myToken,"#amm", "BTC sell: +2% 익절")
            time.sleep(0.5)

            #평단가 5%이상 하락시, 팔아
            print ("sonjul 6")
            if btc_avg*0.95 > current_price_btc:
                if btc*current_price_btc > 5000:
                    sell_result = upbit.sell_market_order("KRW-BTC", btc*0.9995)
                    post_message(myToken,"#amm", "BTC sell: -5% 손절")
            time.sleep(0.5)



            
        ##########장마감 - 가진거 다팔아###################
        else:

            doge = get_balance("DOGE")
            current_price_doge = get_current_price("KRW-DOGE")
            time.sleep(0.5)
            if doge*current_price_doge > 5000:
                sell_result = upbit.sell_market_order("KRW-DOGE", doge*0.9995)
                post_message(myToken,"#amm", "DOGE sell: 장마감")
        
            eth = get_balance("ETH")
            current_price_eth = get_current_price("KRW-ETH")
            time.sleep(0.5)
            if eth*current_price_eth > 5000:
                sell_result = upbit.sell_market_order("KRW-ETH", eth*0.9995)
                post_message(myToken,"#amm", "ETH sell: 장마감")

            eos = get_balance("EOS")
            current_price_eos = get_current_price("KRW-EOS")
            time.sleep(0.5)
            if eos*current_price_eos > 5000:
                sell_result = upbit.sell_market_order("KRW-EOS", eos*0.9995)
                post_message(myToken,"#amm", "EOS sell: 장마감")
        
            etc = get_balance("ETC")
            current_price_etc = get_current_price("KRW-ETC")
            time.sleep(0.5)
            if etc*current_price_etc > 5000:
                sell_result = upbit.sell_market_order("KRW-ETC", etc*0.9995)
                post_message(myToken,"#amm", "ETC sell: 장마감")

            xrp = get_balance("XRP")
            current_price_xrp = get_current_price("KRW-XRP")
            time.sleep(0.5)
            if xrp*current_price_xrp > 5000:
                sell_result = upbit.sell_market_order("KRW-XRP", xrp*0.9995)
                post_message(myToken,"#amm", "XRP sell: 장마감")

            btc = get_balance("BTC")
            current_price_btc = get_current_price("KRW-BTC")
            time.sleep(0.5)
            if btc*current_price_btc > 5000:
                sell_result = upbit.sell_market_order("KRW-BTC", btc*0.9995)
                post_message(myToken,"#amm", "BTC sell: 장마감")
        

        
        time.sleep(1)

    #에러메세지 출력
    except Exception as e:
        print(e)
        post_message(myToken,"#amm", e)
        time.sleep(1)