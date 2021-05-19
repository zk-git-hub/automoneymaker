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
post_message(myToken,"#amm", "Project Danta_0519")


while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(days=1)
        print("timenow")
        time.sleep(0.2)
        
        #오전 9:00 ~ 다음날 오전 8:56 까지 
        if start_time < now < end_time - datetime.timedelta(seconds=200):
            
            krw = get_balance("KRW")

            ##### 코인_DOGE #####
            print ("coin_doge")
            doge = get_balance("DOGE")        
            doge_avg = get_avgprice("DOGE")
            current_price_doge = get_current_price("KRW-DOGE")
            yesterday_price_doge = get_yesterday_price("KRW-DOGE")
            
            #상승장 매수 시나리오 
            print ("upbuy_doge")
            if current_price_doge > yesterday_price_doge and 10000 > doge*doge_avg and (doge_avg*0.98 > current_price_doge or doge_avg*1.04 < current_price_doge):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-DOGE", 200000)
                    post_message(myToken,"#amm", "DOGE buy: 상승장")

            #상승장 매도 시나리오: 평단가 1%이상 상승 시
            print ("upsell_doge")
            if current_price_doge > yesterday_price_doge and doge_avg*1.02 < current_price_doge :
                if doge*current_price_doge > 5000:
                    sell_result = upbit.sell_market_order("KRW-DOGE", doge*0.9995)
                    post_message(myToken,"#amm", "DOGE sell: 상승장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-DOGE", 5000)

            #하락장 매수 시나리오 
            print ("downbuy_doge")
            if current_price_doge < yesterday_price_doge and 10000 > doge*doge_avg and (doge_avg*0.96 > current_price_doge or doge_avg*1.02 < current_price_doge):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-DOGE", 200000)
                    post_message(myToken,"#amm", "DOGE buy: 하락장")

            #하락장 매도 시나리오: 평단가 2%이상 상승 시
            print ("downsell_doge")
            if current_price_doge < yesterday_price_doge and doge_avg*1.02 < current_price_doge :
                if doge*current_price_doge > 5000:
                    sell_result = upbit.sell_market_order("KRW-DOGE", doge*0.9995)
                    post_message(myToken,"#amm", "DOGE sell: 하락장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-DOGE", 5000)

            #하락장 매수 시나리오 : 가즈아
            print ("gazua_doge")
            if current_price_doge < yesterday_price_doge*0.90 and 10000 > doge*doge_avg :
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-DOGE", 200000)
                    post_message(myToken,"#amm", "DOGE gazua: 하락장")

            #평단가 1%이상 하락시, 팔아
            print ("sonjul_doge")
            if doge_avg*0.99 > current_price_doge:
                if doge*current_price_doge > 5000:
                    sell_result = upbit.sell_market_order("KRW-DOGE", doge*0.9995)
                    post_message(myToken,"#amm", "DOGE sell: -1% 손절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-DOGE", 5000)
            time.sleep(0.5)

            ##### 코인_ETH #####
            print ("coin_eth")
            eth = get_balance("ETH")        
            eth_avg = get_avgprice("ETH")
            current_price_eth = get_current_price("KRW-ETH")
            yesterday_price_eth = get_yesterday_price("KRW-ETH")
            
            #상승장 매수 시나리오 
            print ("upbuy_eth")
            if current_price_eth > yesterday_price_eth and 10000 > eth*eth_avg and (eth_avg*0.98 > current_price_eth or eth_avg*1.04 < current_price_eth):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-ETH", 200000)
                    post_message(myToken,"#amm", "ETH buy: 상승장")

            #상승장 매도 시나리오: 평단가 1%이상 상승 시
            print ("upsell_eth")
            if current_price_eth > yesterday_price_eth and eth_avg*1.02 < current_price_eth :
                if eth*current_price_eth > 5000:
                    sell_result = upbit.sell_market_order("KRW-ETH", eth*0.9995)
                    post_message(myToken,"#amm", "ETH sell: 상승장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-ETH", 5000)

            #하락장 매수 시나리오 
            print ("downbuy_eth")
            if current_price_eth < yesterday_price_eth and 10000 > eth*eth_avg and (eth_avg*0.96 > current_price_eth or eth_avg*1.02 < current_price_eth):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-ETH", 200000)
                    post_message(myToken,"#amm", "ETH buy: 하락장")

            #하락장 매도 시나리오: 평단가 2%이상 상승 시
            print ("downsell_eth")
            if current_price_eth < yesterday_price_eth and eth_avg*1.02 < current_price_eth :
                if eth*current_price_eth > 5000:
                    sell_result = upbit.sell_market_order("KRW-ETH", eth*0.9995)
                    post_message(myToken,"#amm", "ETH sell: 하락장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-ETH", 5000)

            #하락장 매수 시나리오 : 가즈아
            print ("gazua_eth")
            if current_price_eth < yesterday_price_eth*0.90 and 10000 > eth*eth_avg :
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-ETH", 200000)
                    post_message(myToken,"#amm", "ETH gazua: 하락장")

            #평단가 1%이상 하락시, 팔아
            print ("sonjul_eth")
            if eth_avg*0.99 > current_price_eth:
                if eth*current_price_eth > 5000:
                    sell_result = upbit.sell_market_order("KRW-ETH", eth*0.9995)
                    post_message(myToken,"#amm", "ETH sell: -1% 손절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-ETH", 5000)
            time.sleep(0.5)

            ##### 코인_EOS #####
            print ("coin_eos")
            eos = get_balance("EOS")        
            eos_avg = get_avgprice("EOS")
            current_price_eos = get_current_price("KRW-EOS")
            yesterday_price_eos = get_yesterday_price("KRW-EOS")
            
            #상승장 매수 시나리오 
            print ("upbuy_eos")
            if current_price_eos > yesterday_price_eos and 10000 > eos*eos_avg and (eos_avg*0.98 > current_price_eos or eos_avg*1.04 < current_price_eos):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-EOS", 200000)
                    post_message(myToken,"#amm", "EOS buy: 상승장")

            #상승장 매도 시나리오: 평단가 1%이상 상승 시
            print ("upsell_eos")
            if current_price_eos > yesterday_price_eos and eos_avg*1.02 < current_price_eos :
                if eos*current_price_eos > 5000:
                    sell_result = upbit.sell_market_order("KRW-EOS", eos*0.9995)
                    post_message(myToken,"#amm", "EOS sell: 상승장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-EOS", 5000)

            #하락장 매수 시나리오 
            print ("downbuy_eos")
            if current_price_eos < yesterday_price_eos and 10000 > eos*eos_avg and (eos_avg*0.96 > current_price_eos or eos_avg*1.02 < current_price_eos):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-EOS", 200000)
                    post_message(myToken,"#amm", "EOS buy: 하락장")

            #하락장 매도 시나리오: 평단가 2%이상 상승 시
            print ("downsell_eos")
            if current_price_eos < yesterday_price_eos and eos_avg*1.02 < current_price_eos :
                if eos*current_price_eos > 5000:
                    sell_result = upbit.sell_market_order("KRW-EOS", eos*0.9995)
                    post_message(myToken,"#amm", "EOS sell: 하락장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-EOS", 5000)

            #하락장 매수 시나리오 : 가즈아
            print ("gazua_eos")
            if current_price_eos < yesterday_price_eos*0.90 and 10000 > eos*eos_avg :
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-EOS", 200000)
                    post_message(myToken,"#amm", "EOS gazua: 하락장")

            #평단가 1%이상 하락시, 팔아
            print ("sonjul_eos")
            if eos_avg*0.99 > current_price_eos:
                if eos*current_price_eos > 5000:
                    sell_result = upbit.sell_market_order("KRW-EOS", eos*0.9995)
                    post_message(myToken,"#amm", "EOS sell: -1% 손절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-EOS", 5000)
            time.sleep(0.5)

            ##### 코인_ETC #####
            print ("coin_etc")
            etc = get_balance("ETC")        
            etc_avg = get_avgprice("ETC")
            current_price_etc = get_current_price("KRW-ETC")
            yesterday_price_etc = get_yesterday_price("KRW-ETC")
            
            #상승장 매수 시나리오 
            print ("upbuy_etc")
            if current_price_etc > yesterday_price_etc and 10000 > etc*etc_avg and (etc_avg*0.98 > current_price_etc or etc_avg*1.04 < current_price_etc):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-ETC", 200000)
                    post_message(myToken,"#amm", "ETC buy: 상승장")

            #상승장 매도 시나리오: 평단가 1%이상 상승 시
            print ("upsell_etc")
            if current_price_etc > yesterday_price_etc and etc_avg*1.02 < current_price_etc :
                if etc*current_price_etc > 5000:
                    sell_result = upbit.sell_market_order("KRW-ETC", etc*0.9995)
                    post_message(myToken,"#amm", "ETC sell: 상승장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-ETC", 5000)

            #하락장 매수 시나리오 
            print ("downbuy_etc")
            if current_price_etc < yesterday_price_etc and 10000 > etc*etc_avg and (etc_avg*0.96 > current_price_etc or etc_avg*1.02 < current_price_etc):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-ETC", 200000)
                    post_message(myToken,"#amm", "ETC buy: 하락장")

            #하락장 매도 시나리오: 평단가 2%이상 상승 시
            print ("downsell_etc")
            if current_price_etc < yesterday_price_etc and etc_avg*1.02 < current_price_etc :
                if etc*current_price_etc > 5000:
                    sell_result = upbit.sell_market_order("KRW-ETC", etc*0.9995)
                    post_message(myToken,"#amm", "ETC sell: 하락장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-ETC", 5000)

            #하락장 매수 시나리오 : 가즈아
            print ("gazua_etc")
            if current_price_etc < yesterday_price_etc*0.90 and 10000 > etc*etc_avg :
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-ETC", 200000)
                    post_message(myToken,"#amm", "ETC gazua: 하락장")

            #평단가 1%이상 하락시, 팔아
            print ("sonjul_etc")
            if etc_avg*0.99 > current_price_etc:
                if etc*current_price_etc > 5000:
                    sell_result = upbit.sell_market_order("KRW-ETC", etc*0.9995)
                    post_message(myToken,"#amm", "ETC sell: -1% 손절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-ETC", 5000)
            time.sleep(0.5)

            ##### 코인_XRP #####
            print ("coin_xrp")
            xrp = get_balance("XRP")        
            xrp_avg = get_avgprice("XRP")
            current_price_xrp = get_current_price("KRW-XRP")
            yesterday_price_xrp = get_yesterday_price("KRW-XRP")
            
            #상승장 매수 시나리오 
            print ("upbuy_xrp")
            if current_price_xrp > yesterday_price_xrp and 10000 > xrp*xrp_avg and (xrp_avg*0.98 > current_price_xrp or xrp_avg*1.04 < current_price_xrp):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-XRP", 200000)
                    post_message(myToken,"#amm", "XRP buy: 상승장")

            #상승장 매도 시나리오: 평단가 1%이상 상승 시
            print ("upsell_xrp")
            if current_price_xrp > yesterday_price_xrp and xrp_avg*1.02 < current_price_xrp :
                if xrp*current_price_xrp > 5000:
                    sell_result = upbit.sell_market_order("KRW-XRP", xrp*0.9995)
                    post_message(myToken,"#amm", "XRP sell: 상승장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-XRP", 5000)

            #하락장 매수 시나리오 
            print ("downbuy_xrp")
            if current_price_xrp < yesterday_price_xrp and 10000 > xrp*xrp_avg and (xrp_avg*0.96 > current_price_xrp or xrp_avg*1.02 < current_price_xrp):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-XRP", 200000)
                    post_message(myToken,"#amm", "XRP buy: 하락장")

            #하락장 매도 시나리오: 평단가 2%이상 상승 시
            print ("downsell_xrp")
            if current_price_xrp < yesterday_price_xrp and xrp_avg*1.02 < current_price_xrp :
                if xrp*current_price_xrp > 5000:
                    sell_result = upbit.sell_market_order("KRW-XRP", xrp*0.9995)
                    post_message(myToken,"#amm", "XRP sell: 하락장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-XRP", 5000)

            #하락장 매수 시나리오 : 가즈아
            print ("gazua_xrp")
            if current_price_xrp < yesterday_price_xrp*0.90 and 10000 > xrp*xrp_avg :
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-XRP", 200000)
                    post_message(myToken,"#amm", "XRP gazua: 하락장")

            #평단가 1%이상 하락시, 팔아
            print ("sonjul_xrp")
            if xrp_avg*0.99 > current_price_xrp:
                if xrp*current_price_xrp > 5000:
                    sell_result = upbit.sell_market_order("KRW-XRP", xrp*0.9995)
                    post_message(myToken,"#amm", "XRP sell: -1% 손절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-XRP", 5000)
            time.sleep(0.5)

            ##### 코인_BTC #####
            print ("coin_btc")
            btc = get_balance("BTC")        
            btc_avg = get_avgprice("BTC")
            current_price_btc = get_current_price("KRW-BTC")
            yesterday_price_btc = get_yesterday_price("KRW-BTC")
            
            #상승장 매수 시나리오 
            print ("upbuy_btc")
            if current_price_btc > yesterday_price_btc and 10000 > btc*btc_avg and (btc_avg*0.98 > current_price_btc or btc_avg*1.04 < current_price_btc):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-BTC", 200000)
                    post_message(myToken,"#amm", "BTC buy: 상승장")

            #상승장 매도 시나리오: 평단가 1%이상 상승 시
            print ("upsell_btc")
            if current_price_btc > yesterday_price_btc and btc_avg*1.02 < current_price_btc :
                if btc*current_price_btc > 5000:
                    sell_result = upbit.sell_market_order("KRW-BTC", btc*0.9995)
                    post_message(myToken,"#amm", "BTC sell: 상승장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-BTC", 5000)

            #하락장 매수 시나리오 
            print ("downbuy_btc")
            if current_price_btc < yesterday_price_btc and 10000 > btc*btc_avg and (btc_avg*0.96 > current_price_btc or btc_avg*1.02 < current_price_btc):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-BTC", 200000)
                    post_message(myToken,"#amm", "BTC buy: 하락장")

            #하락장 매도 시나리오: 평단가 2%이상 상승 시
            print ("downsell_btc")
            if current_price_btc < yesterday_price_btc and btc_avg*1.02 < current_price_btc :
                if btc*current_price_btc > 5000:
                    sell_result = upbit.sell_market_order("KRW-BTC", btc*0.9995)
                    post_message(myToken,"#amm", "BTC sell: 하락장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-BTC", 5000)

            #하락장 매수 시나리오 : 가즈아
            print ("gazua_btc")
            if current_price_btc < yesterday_price_btc*0.90 and 10000 > btc*btc_avg :
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-BTC", 200000)
                    post_message(myToken,"#amm", "BTC gazua: 하락장")

            #평단가 1%이상 하락시, 팔아
            print ("sonjul_btc")
            if btc_avg*0.99 > current_price_btc:
                if btc*current_price_btc > 5000:
                    sell_result = upbit.sell_market_order("KRW-BTC", btc*0.9995)
                    post_message(myToken,"#amm", "BTC sell: -1% 손절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-BTC", 5000)
            time.sleep(0.5)

            ##### 코인_ADA #####
            print ("coin_ada")
            ada = get_balance("ADA")        
            ada_avg = get_avgprice("ADA")
            current_price_ada = get_current_price("KRW-ADA")
            yesterday_price_ada = get_yesterday_price("KRW-ADA")
            
            #상승장 매수 시나리오 
            print ("upbuy_ada")
            if current_price_ada > yesterday_price_ada and 10000 > ada*ada_avg and (ada_avg*0.98 > current_price_ada or ada_avg*1.04 < current_price_ada):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-ADA", 200000)
                    post_message(myToken,"#amm", "ADA buy: 상승장")

            #상승장 매도 시나리오: 평단가 1%이상 상승 시
            print ("upsell_ada")
            if current_price_ada > yesterday_price_ada and ada_avg*1.02 < current_price_ada :
                if ada*current_price_ada > 5000:
                    sell_result = upbit.sell_market_order("KRW-ADA", ada*0.9995)
                    post_message(myToken,"#amm", "ADA sell: 상승장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-ADA", 5000)

            #하락장 매수 시나리오 
            print ("downbuy_ada")
            if current_price_ada < yesterday_price_ada and 10000 > ada*ada_avg and (ada_avg*0.96 > current_price_ada or ada_avg*1.02 < current_price_ada):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-ADA", 200000)
                    post_message(myToken,"#amm", "ADA buy: 하락장")

            #하락장 매도 시나리오: 평단가 2%이상 상승 시
            print ("downsell_ada")
            if current_price_ada < yesterday_price_ada and ada_avg*1.02 < current_price_ada :
                if ada*current_price_ada > 5000:
                    sell_result = upbit.sell_market_order("KRW-ADA", ada*0.9995)
                    post_message(myToken,"#amm", "ADA sell: 하락장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-ADA", 5000)

            #하락장 매수 시나리오 : 가즈아
            print ("gazua_ada")
            if current_price_ada < yesterday_price_ada*0.90 and 10000 > ada*ada_avg :
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-ADA", 200000)
                    post_message(myToken,"#amm", "ADA gazua: 하락장")

            #평단가 1%이상 하락시, 팔아
            print ("sonjul_ada")
            if ada_avg*0.99 > current_price_ada:
                if ada*current_price_ada > 5000:
                    sell_result = upbit.sell_market_order("KRW-ADA", ada*0.9995)
                    post_message(myToken,"#amm", "ADA sell: -1% 손절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-ADA", 5000)
            time.sleep(0.5)

            ##### 코인_BCH #####
            print ("coin_bch")
            bch = get_balance("BCH")        
            bch_avg = get_avgprice("BCH")
            current_price_bch = get_current_price("KRW-BCH")
            yesterday_price_bch = get_yesterday_price("KRW-BCH")
            
            #상승장 매수 시나리오 
            print ("upbuy_bch")
            if current_price_bch > yesterday_price_bch and 10000 > bch*bch_avg and (bch_avg*0.98 > current_price_bch or bch_avg*1.04 < current_price_bch):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-BCH", 200000)
                    post_message(myToken,"#amm", "BCH buy: 상승장")

            #상승장 매도 시나리오: 평단가 1%이상 상승 시
            print ("upsell_bch")
            if current_price_bch > yesterday_price_bch and bch_avg*1.02 < current_price_bch :
                if bch*current_price_bch > 5000:
                    sell_result = upbit.sell_market_order("KRW-BCH", bch*0.9995)
                    post_message(myToken,"#amm", "BCH sell: 상승장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-BCH", 5000)

            #하락장 매수 시나리오 
            print ("downbuy_bch")
            if current_price_bch < yesterday_price_bch and 10000 > bch*bch_avg and (bch_avg*0.96 > current_price_bch or bch_avg*1.02 < current_price_bch):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-BCH", 200000)
                    post_message(myToken,"#amm", "BCH buy: 하락장")

            #하락장 매도 시나리오: 평단가 2%이상 상승 시
            print ("downsell_bch")
            if current_price_bch < yesterday_price_bch and bch_avg*1.02 < current_price_bch :
                if bch*current_price_bch > 5000:
                    sell_result = upbit.sell_market_order("KRW-BCH", bch*0.9995)
                    post_message(myToken,"#amm", "BCH sell: 하락장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-BCH", 5000)

            #하락장 매수 시나리오 : 가즈아
            print ("gazua_bch")
            if current_price_bch < yesterday_price_bch*0.90 and 10000 > bch*bch_avg :
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-BCH", 200000)
                    post_message(myToken,"#amm", "BCH gazua: 하락장")

            #평단가 1%이상 하락시, 팔아
            print ("sonjul_bch")
            if bch_avg*0.99 > current_price_bch:
                if bch*current_price_bch > 5000:
                    sell_result = upbit.sell_market_order("KRW-BCH", bch*0.9995)
                    post_message(myToken,"#amm", "BCH sell: -1% 손절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-BCH", 5000)
            time.sleep(0.5)

            ##### 코인_VET #####
            print ("coin_vet")
            vet = get_balance("VET")        
            vet_avg = get_avgprice("VET")
            current_price_vet = get_current_price("KRW-VET")
            yesterday_price_vet = get_yesterday_price("KRW-VET")
            
            #상승장 매수 시나리오 
            print ("upbuy_vet")
            if current_price_vet > yesterday_price_vet and 10000 > vet*vet_avg and (vet_avg*0.98 > current_price_vet or vet_avg*1.04 < current_price_vet):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-VET", 200000)
                    post_message(myToken,"#amm", "VET buy: 상승장")

            #상승장 매도 시나리오: 평단가 1%이상 상승 시
            print ("upsell_vet")
            if current_price_vet > yesterday_price_vet and vet_avg*1.02 < current_price_vet :
                if vet*current_price_vet > 5000:
                    sell_result = upbit.sell_market_order("KRW-VET", vet*0.9995)
                    post_message(myToken,"#amm", "VET sell: 상승장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-VET", 5000)

            #하락장 매수 시나리오 
            print ("downbuy_vet")
            if current_price_vet < yesterday_price_vet and 10000 > vet*vet_avg and (vet_avg*0.96 > current_price_vet or vet_avg*1.02 < current_price_vet):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-VET", 200000)
                    post_message(myToken,"#amm", "VET buy: 하락장")

            #하락장 매도 시나리오: 평단가 2%이상 상승 시
            print ("downsell_vet")
            if current_price_vet < yesterday_price_vet and vet_avg*1.02 < current_price_vet :
                if vet*current_price_vet > 5000:
                    sell_result = upbit.sell_market_order("KRW-VET", vet*0.9995)
                    post_message(myToken,"#amm", "VET sell: 하락장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-VET", 5000)

            #하락장 매수 시나리오 : 가즈아
            print ("gazua_vet")
            if current_price_vet < yesterday_price_vet*0.90 and 10000 > vet*vet_avg :
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-VET", 200000)
                    post_message(myToken,"#amm", "VET gazua: 하락장")

            #평단가 1%이상 하락시, 팔아
            print ("sonjul_vet")
            if vet_avg*0.99 > current_price_vet:
                if vet*current_price_vet > 5000:
                    sell_result = upbit.sell_market_order("KRW-VET", vet*0.9995)
                    post_message(myToken,"#amm", "VET sell: -1% 손절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-VET", 5000)
            time.sleep(0.5)

            ##### 코인_NEO #####
            print ("coin_neo")
            neo = get_balance("NEO")        
            neo_avg = get_avgprice("NEO")
            current_price_neo = get_current_price("KRW-NEO")
            yesterday_price_neo = get_yesterday_price("KRW-NEO")
            
            #상승장 매수 시나리오 
            print ("upbuy_neo")
            if current_price_neo > yesterday_price_neo and 10000 > neo*neo_avg and (neo_avg*0.98 > current_price_neo or neo_avg*1.04 < current_price_neo):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-NEO", 200000)
                    post_message(myToken,"#amm", "NEO buy: 상승장")

            #상승장 매도 시나리오: 평단가 1%이상 상승 시
            print ("upsell_neo")
            if current_price_neo > yesterday_price_neo and neo_avg*1.02 < current_price_neo :
                if neo*current_price_neo > 5000:
                    sell_result = upbit.sell_market_order("KRW-NEO", neo*0.9995)
                    post_message(myToken,"#amm", "NEO sell: 상승장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-NEO", 5000)

            #하락장 매수 시나리오 
            print ("downbuy_neo")
            if current_price_neo < yesterday_price_neo and 10000 > neo*neo_avg and (neo_avg*0.96 > current_price_neo or neo_avg*1.02 < current_price_neo):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-NEO", 200000)
                    post_message(myToken,"#amm", "NEO buy: 하락장")

            #하락장 매도 시나리오: 평단가 2%이상 상승 시
            print ("downsell_neo")
            if current_price_neo < yesterday_price_neo and neo_avg*1.02 < current_price_neo :
                if neo*current_price_neo > 5000:
                    sell_result = upbit.sell_market_order("KRW-NEO", neo*0.9995)
                    post_message(myToken,"#amm", "NEO sell: 하락장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-NEO", 5000)

            #하락장 매수 시나리오 : 가즈아
            print ("gazua_neo")
            if current_price_neo < yesterday_price_neo*0.90 and 10000 > neo*neo_avg :
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-NEO", 200000)
                    post_message(myToken,"#amm", "NEO gazua: 하락장")

            #평단가 1%이상 하락시, 팔아
            print ("sonjul_neo")
            if neo_avg*0.99 > current_price_neo:
                if neo*current_price_neo > 5000:
                    sell_result = upbit.sell_market_order("KRW-NEO", neo*0.9995)
                    post_message(myToken,"#amm", "NEO sell: -1% 손절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-NEO", 5000)
            time.sleep(0.5)

            ##### 코인_LINK #####
            print ("coin_link")
            link = get_balance("LINK")        
            link_avg = get_avgprice("LINK")
            current_price_link = get_current_price("KRW-LINK")
            yesterday_price_link = get_yesterday_price("KRW-LINK")
            
            #상승장 매수 시나리오 
            print ("upbuy_link")
            if current_price_link > yesterday_price_link and 10000 > link*link_avg and (link_avg*0.98 > current_price_link or link_avg*1.04 < current_price_link):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-LINK", 200000)
                    post_message(myToken,"#amm", "LINK buy: 상승장")

            #상승장 매도 시나리오: 평단가 1%이상 상승 시
            print ("upsell_link")
            if current_price_link > yesterday_price_link and link_avg*1.02 < current_price_link :
                if link*current_price_link > 5000:
                    sell_result = upbit.sell_market_order("KRW-LINK", link*0.9995)
                    post_message(myToken,"#amm", "LINK sell: 상승장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-LINK", 5000)

            #하락장 매수 시나리오 
            print ("downbuy_link")
            if current_price_link < yesterday_price_link and 10000 > link*link_avg and (link_avg*0.96 > current_price_link or link_avg*1.02 < current_price_link):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-LINK", 200000)
                    post_message(myToken,"#amm", "LINK buy: 하락장")

            #하락장 매도 시나리오: 평단가 2%이상 상승 시
            print ("downsell_link")
            if current_price_link < yesterday_price_link and link_avg*1.02 < current_price_link :
                if link*current_price_link > 5000:
                    sell_result = upbit.sell_market_order("KRW-LINK", link*0.9995)
                    post_message(myToken,"#amm", "LINK sell: 하락장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-LINK", 5000)

            #하락장 매수 시나리오 : 가즈아
            print ("gazua_link")
            if current_price_link < yesterday_price_link*0.90 and 10000 > link*link_avg :
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-LINK", 200000)
                    post_message(myToken,"#amm", "LINK gazua: 하락장")

            #평단가 1%이상 하락시, 팔아
            print ("sonjul_link")
            if link_avg*0.99 > current_price_link:
                if link*current_price_link > 5000:
                    sell_result = upbit.sell_market_order("KRW-LINK", link*0.9995)
                    post_message(myToken,"#amm", "LINK sell: -1% 손절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-LINK", 5000)
            time.sleep(0.5)

            ##### 코인_BAT #####
            print ("coin_bat")
            bat = get_balance("BAT")        
            bat_avg = get_avgprice("BAT")
            current_price_bat = get_current_price("KRW-BAT")
            yesterday_price_bat = get_yesterday_price("KRW-BAT")
            
            #상승장 매수 시나리오 
            print ("upbuy_bat")
            if current_price_bat > yesterday_price_bat and 10000 > bat*bat_avg and (bat_avg*0.98 > current_price_bat or bat_avg*1.04 < current_price_bat):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-BAT", 200000)
                    post_message(myToken,"#amm", "BAT buy: 상승장")

            #상승장 매도 시나리오: 평단가 1%이상 상승 시
            print ("upsell_bat")
            if current_price_bat > yesterday_price_bat and bat_avg*1.02 < current_price_bat :
                if bat*current_price_bat > 5000:
                    sell_result = upbit.sell_market_order("KRW-BAT", bat*0.9995)
                    post_message(myToken,"#amm", "BAT sell: 상승장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-BAT", 5000)

            #하락장 매수 시나리오 
            print ("downbuy_bat")
            if current_price_bat < yesterday_price_bat and 10000 > bat*bat_avg and (bat_avg*0.96 > current_price_bat or bat_avg*1.02 < current_price_bat):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-BAT", 200000)
                    post_message(myToken,"#amm", "BAT buy: 하락장")

            #하락장 매도 시나리오: 평단가 2%이상 상승 시
            print ("downsell_bat")
            if current_price_bat < yesterday_price_bat and bat_avg*1.02 < current_price_bat :
                if bat*current_price_bat > 5000:
                    sell_result = upbit.sell_market_order("KRW-BAT", bat*0.9995)
                    post_message(myToken,"#amm", "BAT sell: 하락장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-BAT", 5000)

            #하락장 매수 시나리오 : 가즈아
            print ("gazua_bat")
            if current_price_bat < yesterday_price_bat*0.90 and 10000 > bat*bat_avg :
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-BAT", 200000)
                    post_message(myToken,"#amm", "BAT gazua: 하락장")

            #평단가 1%이상 하락시, 팔아
            print ("sonjul_bat")
            if bat_avg*0.99 > current_price_bat:
                if bat*current_price_bat > 5000:
                    sell_result = upbit.sell_market_order("KRW-BAT", bat*0.9995)
                    post_message(myToken,"#amm", "BAT sell: -1% 손절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-BAT", 5000)
            time.sleep(0.5)

            ##### 코인_LTC #####
            print ("coin_ltc")
            ltc = get_balance("LTC")        
            ltc_avg = get_avgprice("LTC")
            current_price_ltc = get_current_price("KRW-LTC")
            yesterday_price_ltc = get_yesterday_price("KRW-LTC")
            
            #상승장 매수 시나리오 
            print ("upbuy_ltc")
            if current_price_ltc > yesterday_price_ltc and 10000 > ltc*ltc_avg and (ltc_avg*0.98 > current_price_ltc or ltc_avg*1.04 < current_price_ltc):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-LTC", 200000)
                    post_message(myToken,"#amm", "LTC buy: 상승장")

            #상승장 매도 시나리오: 평단가 1%이상 상승 시
            print ("upsell_ltc")
            if current_price_ltc > yesterday_price_ltc and ltc_avg*1.02 < current_price_ltc :
                if ltc*current_price_ltc > 5000:
                    sell_result = upbit.sell_market_order("KRW-LTC", ltc*0.9995)
                    post_message(myToken,"#amm", "LTC sell: 상승장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-LTC", 5000)

            #하락장 매수 시나리오 
            print ("downbuy_ltc")
            if current_price_ltc < yesterday_price_ltc and 10000 > ltc*ltc_avg and (ltc_avg*0.96 > current_price_ltc or ltc_avg*1.02 < current_price_ltc):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-LTC", 200000)
                    post_message(myToken,"#amm", "LTC buy: 하락장")

            #하락장 매도 시나리오: 평단가 2%이상 상승 시
            print ("downsell_ltc")
            if current_price_ltc < yesterday_price_ltc and ltc_avg*1.02 < current_price_ltc :
                if ltc*current_price_ltc > 5000:
                    sell_result = upbit.sell_market_order("KRW-LTC", ltc*0.9995)
                    post_message(myToken,"#amm", "LTC sell: 하락장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-LTC", 5000)

            #하락장 매수 시나리오 : 가즈아
            print ("gazua_ltc")
            if current_price_ltc < yesterday_price_ltc*0.90 and 10000 > ltc*ltc_avg :
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-LTC", 200000)
                    post_message(myToken,"#amm", "LTC gazua: 하락장")

            #평단가 1%이상 하락시, 팔아
            print ("sonjul_ltc")
            if ltc_avg*0.99 > current_price_ltc:
                if ltc*current_price_ltc > 5000:
                    sell_result = upbit.sell_market_order("KRW-LTC", ltc*0.9995)
                    post_message(myToken,"#amm", "LTC sell: -1% 손절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-LTC", 5000)
            time.sleep(0.5)

            ##### 코인_BTG #####
            print ("coin_btg")
            btg = get_balance("BTG")        
            btg_avg = get_avgprice("BTG")
            current_price_btg = get_current_price("KRW-BTG")
            yesterday_price_btg = get_yesterday_price("KRW-BTG")
            
            #상승장 매수 시나리오 
            print ("upbuy_btg")
            if current_price_btg > yesterday_price_btg and 10000 > btg*btg_avg and (btg_avg*0.98 > current_price_btg or btg_avg*1.04 < current_price_btg):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-BTG", 200000)
                    post_message(myToken,"#amm", "BTG buy: 상승장")

            #상승장 매도 시나리오: 평단가 1%이상 상승 시
            print ("upsell_btg")
            if current_price_btg > yesterday_price_btg and btg_avg*1.02 < current_price_btg :
                if btg*current_price_btg > 5000:
                    sell_result = upbit.sell_market_order("KRW-BTG", btg*0.9995)
                    post_message(myToken,"#amm", "BTG sell: 상승장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-BTG", 5000)

            #하락장 매수 시나리오 
            print ("downbuy_btg")
            if current_price_btg < yesterday_price_btg and 10000 > btg*btg_avg and (btg_avg*0.96 > current_price_btg or btg_avg*1.02 < current_price_btg):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-BTG", 200000)
                    post_message(myToken,"#amm", "BTG buy: 하락장")

            #하락장 매도 시나리오: 평단가 2%이상 상승 시
            print ("downsell_btg")
            if current_price_btg < yesterday_price_btg and btg_avg*1.02 < current_price_btg :
                if btg*current_price_btg > 5000:
                    sell_result = upbit.sell_market_order("KRW-BTG", btg*0.9995)
                    post_message(myToken,"#amm", "BTG sell: 하락장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-BTG", 5000)

            #하락장 매수 시나리오 : 가즈아
            print ("gazua_btg")
            if current_price_btg < yesterday_price_btg*0.90 and 10000 > btg*btg_avg :
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-BTG", 200000)
                    post_message(myToken,"#amm", "BTG gazua: 하락장")

            #평단가 1%이상 하락시, 팔아
            print ("sonjul_btg")
            if btg_avg*0.99 > current_price_btg:
                if btg*current_price_btg > 5000:
                    sell_result = upbit.sell_market_order("KRW-BTG", btg*0.9995)
                    post_message(myToken,"#amm", "BTG sell: -1% 손절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-BTG", 5000)
            time.sleep(0.5)

            ##### 코인_PCI #####
            print ("coin_pci")
            pci = get_balance("PCI")        
            pci_avg = get_avgprice("PCI")
            current_price_pci = get_current_price("KRW-PCI")
            yesterday_price_pci = get_yesterday_price("KRW-PCI")
            
            #상승장 매수 시나리오 
            print ("upbuy_pci")
            if current_price_pci > yesterday_price_pci and 10000 > pci*pci_avg and (pci_avg*0.98 > current_price_pci or pci_avg*1.04 < current_price_pci):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-PCI", 200000)
                    post_message(myToken,"#amm", "PCI buy: 상승장")

            #상승장 매도 시나리오: 평단가 1%이상 상승 시
            print ("upsell_pci")
            if current_price_pci > yesterday_price_pci and pci_avg*1.02 < current_price_pci :
                if pci*current_price_pci > 5000:
                    sell_result = upbit.sell_market_order("KRW-PCI", pci*0.9995)
                    post_message(myToken,"#amm", "PCI sell: 상승장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-PCI", 5000)

            #하락장 매수 시나리오 
            print ("downbuy_pci")
            if current_price_pci < yesterday_price_pci and 10000 > pci*pci_avg and (pci_avg*0.96 > current_price_pci or pci_avg*1.02 < current_price_pci):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-PCI", 200000)
                    post_message(myToken,"#amm", "PCI buy: 하락장")

            #하락장 매도 시나리오: 평단가 2%이상 상승 시
            print ("downsell_pci")
            if current_price_pci < yesterday_price_pci and pci_avg*1.02 < current_price_pci :
                if pci*current_price_pci > 5000:
                    sell_result = upbit.sell_market_order("KRW-PCI", pci*0.9995)
                    post_message(myToken,"#amm", "PCI sell: 하락장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-PCI", 5000)

            #하락장 매수 시나리오 : 가즈아
            print ("gazua_pci")
            if current_price_pci < yesterday_price_pci*0.90 and 10000 > pci*pci_avg :
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-PCI", 200000)
                    post_message(myToken,"#amm", "PCI gazua: 하락장")

            #평단가 1%이상 하락시, 팔아
            print ("sonjul_pci")
            if pci_avg*0.99 > current_price_pci:
                if pci*current_price_pci > 5000:
                    sell_result = upbit.sell_market_order("KRW-PCI", pci*0.9995)
                    post_message(myToken,"#amm", "PCI sell: -1% 손절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-PCI", 5000)
            time.sleep(0.5)

            ##### 코인_QTUM #####
            print ("coin_qtum")
            qtum = get_balance("QTUM")        
            qtum_avg = get_avgprice("QTUM")
            current_price_qtum = get_current_price("KRW-QTUM")
            yesterday_price_qtum = get_yesterday_price("KRW-QTUM")
            
            #상승장 매수 시나리오 
            print ("upbuy_qtum")
            if current_price_qtum > yesterday_price_qtum and 10000 > qtum*qtum_avg and (qtum_avg*0.98 > current_price_qtum or qtum_avg*1.04 < current_price_qtum):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-QTUM", 200000)
                    post_message(myToken,"#amm", "QTUM buy: 상승장")

            #상승장 매도 시나리오: 평단가 1%이상 상승 시
            print ("upsell_qtum")
            if current_price_qtum > yesterday_price_qtum and qtum_avg*1.02 < current_price_qtum :
                if qtum*current_price_qtum > 5000:
                    sell_result = upbit.sell_market_order("KRW-QTUM", qtum*0.9995)
                    post_message(myToken,"#amm", "QTUM sell: 상승장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-QTUM", 5000)

            #하락장 매수 시나리오 
            print ("downbuy_qtum")
            if current_price_qtum < yesterday_price_qtum and 10000 > qtum*qtum_avg and (qtum_avg*0.96 > current_price_qtum or qtum_avg*1.02 < current_price_qtum):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-QTUM", 200000)
                    post_message(myToken,"#amm", "QTUM buy: 하락장")

            #하락장 매도 시나리오: 평단가 2%이상 상승 시
            print ("downsell_qtum")
            if current_price_qtum < yesterday_price_qtum and qtum_avg*1.02 < current_price_qtum :
                if qtum*current_price_qtum > 5000:
                    sell_result = upbit.sell_market_order("KRW-QTUM", qtum*0.9995)
                    post_message(myToken,"#amm", "QTUM sell: 하락장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-QTUM", 5000)

            #하락장 매수 시나리오 : 가즈아
            print ("gazua_qtum")
            if current_price_qtum < yesterday_price_qtum*0.90 and 10000 > qtum*qtum_avg :
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-QTUM", 200000)
                    post_message(myToken,"#amm", "QTUM gazua: 하락장")

            #평단가 1%이상 하락시, 팔아
            print ("sonjul_qtum")
            if qtum_avg*0.99 > current_price_qtum:
                if qtum*current_price_qtum > 5000:
                    sell_result = upbit.sell_market_order("KRW-QTUM", qtum*0.9995)
                    post_message(myToken,"#amm", "QTUM sell: -1% 손절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-QTUM", 5000)
            time.sleep(0.5)

            ##### 코인_DOT #####
            print ("coin_dot")
            dot = get_balance("DOT")        
            dot_avg = get_avgprice("DOT")
            current_price_dot = get_current_price("KRW-DOT")
            yesterday_price_dot = get_yesterday_price("KRW-DOT")
            
            #상승장 매수 시나리오 
            print ("upbuy_dot")
            if current_price_dot > yesterday_price_dot and 10000 > dot*dot_avg and (dot_avg*0.98 > current_price_dot or dot_avg*1.04 < current_price_dot):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-DOT", 200000)
                    post_message(myToken,"#amm", "DOT buy: 상승장")

            #상승장 매도 시나리오: 평단가 1%이상 상승 시
            print ("upsell_dot")
            if current_price_dot > yesterday_price_dot and dot_avg*1.02 < current_price_dot :
                if dot*current_price_dot > 5000:
                    sell_result = upbit.sell_market_order("KRW-DOT", dot*0.9995)
                    post_message(myToken,"#amm", "DOT sell: 상승장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-DOT", 5000)

            #하락장 매수 시나리오 
            print ("downbuy_dot")
            if current_price_dot < yesterday_price_dot and 10000 > dot*dot_avg and (dot_avg*0.96 > current_price_dot or dot_avg*1.02 < current_price_dot):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-DOT", 200000)
                    post_message(myToken,"#amm", "DOT buy: 하락장")

            #하락장 매도 시나리오: 평단가 2%이상 상승 시
            print ("downsell_dot")
            if current_price_dot < yesterday_price_dot and dot_avg*1.02 < current_price_dot :
                if dot*current_price_dot > 5000:
                    sell_result = upbit.sell_market_order("KRW-DOT", dot*0.9995)
                    post_message(myToken,"#amm", "DOT sell: 하락장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-DOT", 5000)

            #하락장 매수 시나리오 : 가즈아
            print ("gazua_dot")
            if current_price_dot < yesterday_price_dot*0.90 and 10000 > dot*dot_avg :
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-DOT", 200000)
                    post_message(myToken,"#amm", "DOT gazua: 하락장")

            #평단가 1%이상 하락시, 팔아
            print ("sonjul_dot")
            if dot_avg*0.99 > current_price_dot:
                if dot*current_price_dot > 5000:
                    sell_result = upbit.sell_market_order("KRW-DOT", dot*0.9995)
                    post_message(myToken,"#amm", "DOT sell: -1% 손절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-DOT", 5000)
            time.sleep(0.5)

            ##### 코인_XLM #####
            print ("coin_xlm")
            xlm = get_balance("XLM")        
            xlm_avg = get_avgprice("XLM")
            current_price_xlm = get_current_price("KRW-XLM")
            yesterday_price_xlm = get_yesterday_price("KRW-XLM")
            
            #상승장 매수 시나리오 
            print ("upbuy_xlm")
            if current_price_xlm > yesterday_price_xlm and 10000 > xlm*xlm_avg and (xlm_avg*0.98 > current_price_xlm or xlm_avg*1.04 < current_price_xlm):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-XLM", 200000)
                    post_message(myToken,"#amm", "XLM buy: 상승장")

            #상승장 매도 시나리오: 평단가 1%이상 상승 시
            print ("upsell_xlm")
            if current_price_xlm > yesterday_price_xlm and xlm_avg*1.02 < current_price_xlm :
                if xlm*current_price_xlm > 5000:
                    sell_result = upbit.sell_market_order("KRW-XLM", xlm*0.9995)
                    post_message(myToken,"#amm", "XLM sell: 상승장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-XLM", 5000)

            #하락장 매수 시나리오 
            print ("downbuy_xlm")
            if current_price_xlm < yesterday_price_xlm and 10000 > xlm*xlm_avg and (xlm_avg*0.96 > current_price_xlm or xlm_avg*1.02 < current_price_xlm):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-XLM", 200000)
                    post_message(myToken,"#amm", "XLM buy: 하락장")

            #하락장 매도 시나리오: 평단가 2%이상 상승 시
            print ("downsell_xlm")
            if current_price_xlm < yesterday_price_xlm and xlm_avg*1.02 < current_price_xlm :
                if xlm*current_price_xlm > 5000:
                    sell_result = upbit.sell_market_order("KRW-XLM", xlm*0.9995)
                    post_message(myToken,"#amm", "XLM sell: 하락장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-XLM", 5000)

            #하락장 매수 시나리오 : 가즈아
            print ("gazua_xlm")
            if current_price_xlm < yesterday_price_xlm*0.90 and 10000 > xlm*xlm_avg :
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-XLM", 200000)
                    post_message(myToken,"#amm", "XLM gazua: 하락장")

            #평단가 1%이상 하락시, 팔아
            print ("sonjul_xlm")
            if xlm_avg*0.99 > current_price_xlm:
                if xlm*current_price_xlm > 5000:
                    sell_result = upbit.sell_market_order("KRW-XLM", xlm*0.9995)
                    post_message(myToken,"#amm", "XLM sell: -1% 손절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-XLM", 5000)
            time.sleep(0.5)

            ##### 코인_CHZ #####
            print ("coin_chz")
            chz = get_balance("CHZ")        
            chz_avg = get_avgprice("CHZ")
            current_price_chz = get_current_price("KRW-CHZ")
            yesterday_price_chz = get_yesterday_price("KRW-CHZ")
            
            #상승장 매수 시나리오 
            print ("upbuy_chz")
            if current_price_chz > yesterday_price_chz and 10000 > chz*chz_avg and (chz_avg*0.98 > current_price_chz or chz_avg*1.04 < current_price_chz):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-CHZ", 200000)
                    post_message(myToken,"#amm", "CHZ buy: 상승장")

            #상승장 매도 시나리오: 평단가 1%이상 상승 시
            print ("upsell_chz")
            if current_price_chz > yesterday_price_chz and chz_avg*1.02 < current_price_chz :
                if chz*current_price_chz > 5000:
                    sell_result = upbit.sell_market_order("KRW-CHZ", chz*0.9995)
                    post_message(myToken,"#amm", "CHZ sell: 상승장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-CHZ", 5000)

            #하락장 매수 시나리오 
            print ("downbuy_chz")
            if current_price_chz < yesterday_price_chz and 10000 > chz*chz_avg and (chz_avg*0.96 > current_price_chz or chz_avg*1.02 < current_price_chz):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-CHZ", 200000)
                    post_message(myToken,"#amm", "CHZ buy: 하락장")

            #하락장 매도 시나리오: 평단가 2%이상 상승 시
            print ("downsell_chz")
            if current_price_chz < yesterday_price_chz and chz_avg*1.02 < current_price_chz :
                if chz*current_price_chz > 5000:
                    sell_result = upbit.sell_market_order("KRW-CHZ", chz*0.9995)
                    post_message(myToken,"#amm", "CHZ sell: 하락장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-CHZ", 5000)

            #하락장 매수 시나리오 : 가즈아
            print ("gazua_chz")
            if current_price_chz < yesterday_price_chz*0.90 and 10000 > chz*chz_avg :
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-CHZ", 200000)
                    post_message(myToken,"#amm", "CHZ gazua: 하락장")

            #평단가 1%이상 하락시, 팔아
            print ("sonjul_chz")
            if chz_avg*0.99 > current_price_chz:
                if chz*current_price_chz > 5000:
                    sell_result = upbit.sell_market_order("KRW-CHZ", chz*0.9995)
                    post_message(myToken,"#amm", "CHZ sell: -1% 손절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-CHZ", 5000)
            time.sleep(0.5)

            ##### 코인_SNT #####
            print ("coin_snt")
            snt = get_balance("SNT")        
            snt_avg = get_avgprice("SNT")
            current_price_snt = get_current_price("KRW-SNT")
            yesterday_price_snt = get_yesterday_price("KRW-SNT")
            
            #상승장 매수 시나리오 
            print ("upbuy_snt")
            if current_price_snt > yesterday_price_snt and 10000 > snt*snt_avg and (snt_avg*0.98 > current_price_snt or snt_avg*1.04 < current_price_snt):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-SNT", 200000)
                    post_message(myToken,"#amm", "SNT buy: 상승장")

            #상승장 매도 시나리오: 평단가 1%이상 상승 시
            print ("upsell_snt")
            if current_price_snt > yesterday_price_snt and snt_avg*1.02 < current_price_snt :
                if snt*current_price_snt > 5000:
                    sell_result = upbit.sell_market_order("KRW-SNT", snt*0.9995)
                    post_message(myToken,"#amm", "SNT sell: 상승장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-SNT", 5000)

            #하락장 매수 시나리오 
            print ("downbuy_snt")
            if current_price_snt < yesterday_price_snt and 10000 > snt*snt_avg and (snt_avg*0.96 > current_price_snt or snt_avg*1.02 < current_price_snt):
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-SNT", 200000)
                    post_message(myToken,"#amm", "SNT buy: 하락장")

            #하락장 매도 시나리오: 평단가 2%이상 상승 시
            print ("downsell_snt")
            if current_price_snt < yesterday_price_snt and snt_avg*1.02 < current_price_snt :
                if snt*current_price_snt > 5000:
                    sell_result = upbit.sell_market_order("KRW-SNT", snt*0.9995)
                    post_message(myToken,"#amm", "SNT sell: 하락장 +2% 익절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-SNT", 5000)

            #하락장 매수 시나리오 : 가즈아
            print ("gazua_snt")
            if current_price_snt < yesterday_price_snt*0.90 and 10000 > snt*snt_avg :
                if krw > 200200:
                    buy_result = upbit.buy_market_order("KRW-SNT", 200000)
                    post_message(myToken,"#amm", "SNT gazua: 하락장")

            #평단가 1%이상 하락시, 팔아
            print ("sonjul_snt")
            if snt_avg*0.99 > current_price_snt:
                if snt*current_price_snt > 5000:
                    sell_result = upbit.sell_market_order("KRW-SNT", snt*0.9995)
                    post_message(myToken,"#amm", "SNT sell: -1% 손절")
                    time.sleep(0.2)
                    buy_result = upbit.buy_market_order("KRW-SNT", 5000)
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
        
            ada = get_balance("ADA")
            current_price_ada = get_current_price("KRW-ADA")
            time.sleep(0.5)
            if ada*current_price_ada > 5000:
                sell_result = upbit.sell_market_order("KRW-ADA", ada*0.9995)
                post_message(myToken,"#amm", "ADA sell: 장마감")

            bch = get_balance("BCH")
            current_price_bch = get_current_price("KRW-BCH")
            time.sleep(0.5)
            if bch*current_price_bch > 5000:
                sell_result = upbit.sell_market_order("KRW-BCH", bch*0.9995)
                post_message(myToken,"#amm", "BCH sell: 장마감")

            vet = get_balance("VET")
            current_price_vet = get_current_price("KRW-VET")
            time.sleep(0.5)
            if vet*current_price_vet > 5000:
                sell_result = upbit.sell_market_order("KRW-VET", vet*0.9995)
                post_message(myToken,"#amm", "VET sell: 장마감")

            neo = get_balance("NEO")
            current_price_neo = get_current_price("KRW-NEO")
            time.sleep(0.5)
            if neo*current_price_neo > 5000:
                sell_result = upbit.sell_market_order("KRW-NEO", neo*0.9995)
                post_message(myToken,"#amm", "NEO sell: 장마감")

            link = get_balance("LINK")
            current_price_link = get_current_price("KRW-LINK")
            time.sleep(0.5)
            if link*current_price_link > 5000:
                sell_result = upbit.sell_market_order("KRW-LINK", link*0.9995)
                post_message(myToken,"#amm", "LINK sell: 장마감")
        
            bat = get_balance("BAT")
            current_price_bat = get_current_price("KRW-BAT")
            time.sleep(0.5)
            if bat*current_price_bat > 5000:
                sell_result = upbit.sell_market_order("KRW-BAT", bat*0.9995)
                post_message(myToken,"#amm", "BAT sell: 장마감")

            ltc = get_balance("LTC")
            current_price_ltc = get_current_price("KRW-LTC")
            time.sleep(0.5)
            if ltc*current_price_ltc > 5000:
                sell_result = upbit.sell_market_order("KRW-LTC", ltc*0.9995)
                post_message(myToken,"#amm", "LTC sell: 장마감")
        
            btg = get_balance("BTG")
            current_price_btg = get_current_price("KRW-BTG")
            time.sleep(0.5)
            if btg*current_price_btg > 5000:
                sell_result = upbit.sell_market_order("KRW-BTG", btg*0.9995)
                post_message(myToken,"#amm", "BTG sell: 장마감")

            pci = get_balance("PCI")
            current_price_pci = get_current_price("KRW-PCI")
            time.sleep(0.5)
            if pci*current_price_pci > 5000:
                sell_result = upbit.sell_market_order("KRW-PCI", pci*0.9995)
                post_message(myToken,"#amm", "PCI sell: 장마감")

            qtum = get_balance("QTUM")
            current_price_qtum = get_current_price("KRW-QTUM")
            time.sleep(0.5)
            if qtum*current_price_qtum > 5000:
                sell_result = upbit.sell_market_order("KRW-QTUM", qtum*0.9995)
                post_message(myToken,"#amm", "QTUM sell: 장마감")
        
            dot = get_balance("DOT")
            current_price_dot = get_current_price("KRW-DOT")
            time.sleep(0.5)
            if dot*current_price_dot > 5000:
                sell_result = upbit.sell_market_order("KRW-DOT", dot*0.9995)
                post_message(myToken,"#amm", "DOT sell: 장마감")

            xlm = get_balance("XLM")
            current_price_xlm = get_current_price("KRW-XLM")
            time.sleep(0.5)
            if xlm*current_price_xlm > 5000:
                sell_result = upbit.sell_market_order("KRW-XLM", xlm*0.9995)
                post_message(myToken,"#amm", "XLM sell: 장마감")
        
            chz = get_balance("CHZ")
            current_price_chz = get_current_price("KRW-CHZ")
            time.sleep(0.5)
            if chz*current_price_chz > 5000:
                sell_result = upbit.sell_market_order("KRW-CHZ", chz*0.9995)
                post_message(myToken,"#amm", "CHZ sell: 장마감")
        
            snt = get_balance("SNT")
            current_price_snt = get_current_price("KRW-SNT")
            time.sleep(0.5)
            if snt*current_price_snt > 5000:
                sell_result = upbit.sell_market_order("KRW-SNT", snt*0.9995)
                post_message(myToken,"#amm", "SNT sell: 장마감")
        
        time.sleep(1)

    #에러메세지 출력
    except Exception as e:
        print(e)
        post_message(myToken,"#amm", e)
        time.sleep(1)