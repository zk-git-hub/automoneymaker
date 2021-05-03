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

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("Autotradestart")
# 시작 메세지 슬랙 전송
post_message(myToken,"#amm", "Autotradestart")
post_message(myToken,"#amm", "###타겟리스트###")
post_message(myToken,"#amm", "  비트코인-BTC")
time.sleep(0.2)
post_message(myToken,"#amm", "  이더리움-ETH")
time.sleep(0.2)
post_message(myToken,"#amm", "  이오스-EOS")
time.sleep(0.2)
post_message(myToken,"#amm", "  도지코인-DOGE")
time.sleep(0.2)
post_message(myToken,"#amm", "  리플-XRP")
time.sleep(0.2)
post_message(myToken,"#amm", "  에이다-ADA")
time.sleep(0.2)
post_message(myToken,"#amm", "  칠리즈-CHZ")
time.sleep(0.2)
post_message(myToken,"#amm", "  던프로토콜-DAWN")
time.sleep(0.2)
post_message(myToken,"#amm", "  페이코인-PCI")
time.sleep(0.2)
post_message(myToken,"#amm", "  비체인-VET")
time.sleep(0.2)
post_message(myToken,"#amm", "  이더리움클래식-ETC")
time.sleep(0.2)
post_message(myToken,"#amm", "  비트토렌트-BTT")
time.sleep(0.2)
post_message(myToken,"#amm", "  비트코인골드-BTG")
time.sleep(0.2)
post_message(myToken,"#amm", "  비트코인캐시-BCH")
time.sleep(0.2)
post_message(myToken,"#amm", "  네오-NEO")
time.sleep(0.2)

while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(days=1)
        print("timenow")
        time.sleep(1)
        
        #오전 9:00 ~ 다음날 오전 8:56 까지 
        if start_time < now < end_time - datetime.timedelta(seconds=200):
            # 코인종류 & k 값 설정
            krw = get_balance("KRW")

            target_price_btc = get_target_price("KRW-BTC", 0.2)
            target_price_eth = get_target_price("KRW-ETH", 0.1)
            target_price_eos = get_target_price("KRW-EOS", 0.4)
            print ("targetprice1")
            time.sleep(0.5)
            target_price_doge = get_target_price("KRW-DOGE", 0.3)
            target_price_xrp = get_target_price("KRW-XRP", 0.4)
            target_price_ada = get_target_price("KRW-ADA", 0.4)
            print ("targetprice2")
            time.sleep(0.5)
            target_price_chz = get_target_price("KRW-CHZ", 0.4)
            target_price_dawn = get_target_price("KRW-DAWN", 0.4)
            target_price_pci = get_target_price("KRW-PCI", 0.4)
            print ("targetprice3")
            time.sleep(0.5)
            target_price_vet = get_target_price("KRW-VET", 0.3)
            target_price_etc = get_target_price("KRW-ETC", 0.1)
            target_price_btt = get_target_price("KRW-BTT", 0.2)
            print ("targetprice4")
            time.sleep(0.5)
            target_price_btg = get_target_price("KRW-BTG", 0.2)
            target_price_bch = get_target_price("KRW-BCH", 0.2)
            target_price_neo = get_target_price("KRW-NEO", 0.2)
            print ("targetprice5")
            time.sleep(0.5)

            btc = get_balance("BTC")
            eth = get_balance("ETH")
            eos = get_balance("EOS")
            print ("balance1")
            time.sleep(0.5)
            doge = get_balance("DOGE")
            xrp = get_balance("XRP")
            ada = get_balance("ADA")
            print ("balance2")
            time.sleep(0.5)
            chz = get_balance("CHZ")
            dawn = get_balance("DAWN")
            pci = get_balance("PCI")
            print ("balance3")
            time.sleep(0.5)
            vet = get_balance("VET")
            etc = get_balance("ETC")
            btt = get_balance("BTT")
            print ("balance4")
            time.sleep(0.5)
            btg = get_balance("BTG")
            bch = get_balance("BCH")
            neo = get_balance("NEO")
            print ("balance5")
            time.sleep(0.5)

            current_price_btc = get_current_price("KRW-BTC")
            yesterday_price_btc = get_yesterday_price("KRW-BTC")
            current_price_eth = get_current_price("KRW-ETH")
            yesterday_price_eth = get_yesterday_price("KRW-ETH")
            current_price_eos = get_current_price("KRW-EOS")
            yesterday_price_eos = get_yesterday_price("KRW-EOS")
            print ("price1")
            time.sleep(0.5)
            current_price_doge = get_current_price("KRW-DOGE")
            yesterday_price_doge = get_yesterday_price("KRW-DOGE")
            current_price_xrp = get_current_price("KRW-XRP")
            yesterday_price_xrp = get_yesterday_price("KRW-XRP")
            current_price_ada = get_current_price("KRW-ADA")
            yesterday_price_ada = get_yesterday_price("KRW-ADA")
            print ("price2")
            time.sleep(0.5)
            current_price_chz = get_current_price("KRW-CHZ")
            yesterday_price_chz = get_yesterday_price("KRW-CHZ")
            current_price_dawn = get_current_price("KRW-DAWN")
            yesterday_price_dawn = get_yesterday_price("KRW-DAWN")
            current_price_pci = get_current_price("KRW-PCI")
            yesterday_price_pci = get_yesterday_price("KRW-PCI")
            print ("price3")
            time.sleep(0.5)
            current_price_vet = get_current_price("KRW-VET")
            yesterday_price_vet = get_yesterday_price("KRW-VET")
            current_price_etc = get_current_price("KRW-ETC")
            yesterday_price_etc = get_yesterday_price("KRW-ETC")
            current_price_btt = get_current_price("KRW-BTT")
            yesterday_price_btt = get_yesterday_price("KRW-BTT")
            print ("price4")
            time.sleep(0.5)
            current_price_btg = get_current_price("KRW-BTG")
            yesterday_price_btg = get_yesterday_price("KRW-BTG")
            current_price_bch = get_current_price("KRW-BCH")
            yesterday_price_bch = get_yesterday_price("KRW-BCH")
            current_price_neo = get_current_price("KRW-NEO")
            yesterday_price_neo = get_yesterday_price("KRW-NEO")
            print ("price5")
            time.sleep(0.5)


            #타겟 가격돌파 & 현재 가지고있는 코인 평가금이 10,000 이하일 때, 500,000 매수
            
            print ("buy1")
            if target_price_btc < current_price_btc and 10000 > btc*current_price_btc:
                if krw > 500500:
                    buy_result = upbit.buy_market_order("KRW-BTC", 500000)
                    post_message(myToken,"#amm", "BTC buy : 타겟 구매")
            time.sleep(0.5)

            print ("buy2")
            if target_price_eth < current_price_eth and 10000 > eth*current_price_eth:
                if krw > 500500:
                    buy_result = upbit.buy_market_order("KRW-ETH", 500000)
                    post_message(myToken,"#amm", "ETH buy : 타겟 구매")
            time.sleep(0.5)

            print ("buy3")
            if target_price_eos < current_price_eos and 10000 > eos*current_price_eos:
                if krw > 500500:
                    buy_result = upbit.buy_market_order("KRW-EOS", 500000)
                    post_message(myToken,"#amm", "EOS buy : 타겟 구매")
            time.sleep(0.5)
            
            print ("buy4")
            if target_price_doge < current_price_doge and 10000 > doge*current_price_doge:
                if krw > 500500:
                    buy_result = upbit.buy_market_order("KRW-DOGE", 500000)
                    post_message(myToken,"#amm", "DOGE buy : 타겟 구매")
            time.sleep(0.5)

            print ("buy5")
            if target_price_xrp < current_price_xrp and 10000 > xrp*current_price_xrp:
                if krw > 500500:
                    buy_result = upbit.buy_market_order("KRW-XRP", 500000)
                    post_message(myToken,"#amm", "XRP buy : 타겟 구매")
            time.sleep(0.5)

            print ("buy6")
            if target_price_ada < current_price_ada and 10000 > ada*current_price_ada:
                if krw > 500500:
                    buy_result = upbit.buy_market_order("KRW-ADA", 500000)
                    post_message(myToken,"#amm", "ADA buy : 타겟 구매")
            time.sleep(0.5)

            print ("buy7")
            if target_price_chz < current_price_chz and 10000 > chz*current_price_chz:
                if krw > 500500:
                    buy_result = upbit.buy_market_order("KRW-CHZ", 500000)
                    post_message(myToken,"#amm", "CHZ buy : 타겟 구매")
            time.sleep(0.5)

            print ("buy8")
            if target_price_dawn < current_price_dawn and 10000 > dawn*current_price_dawn:
                if krw > 500500:
                    buy_result = upbit.buy_market_order("KRW-DAWN", 500000)
                    post_message(myToken,"#amm", "DAWN buy : 타겟 구매")
            time.sleep(0.5)

            print ("buy9")
            if target_price_pci < current_price_pci and 10000 > pci*current_price_pci:
                if krw > 500500:
                    buy_result = upbit.buy_market_order("KRW-PCI", 500000)
                    post_message(myToken,"#amm", "PCI buy : 타겟 구매")
            time.sleep(0.5)

            print ("buy10")
            if target_price_vet < current_price_vet and 10000 > vet*current_price_vet:
                if krw > 500500:
                    buy_result = upbit.buy_market_order("KRW-VET", 500000)
                    post_message(myToken,"#amm", "VET buy : 타겟 구매")
            time.sleep(0.5)
            
            print ("buy11")
            if target_price_etc < current_price_etc and 10000 > etc*current_price_etc:
                if krw > 500500:
                    buy_result = upbit.buy_market_order("KRW-ETC", 500000)
                    post_message(myToken,"#amm", "ETC buy : 타겟 구매")
            time.sleep(0.5)

            print ("buy12")
            if target_price_btt < current_price_btt and 10000 > btt*current_price_btt:
                if krw > 500500:
                    buy_result = upbit.buy_market_order("KRW-BTT", 500000)
                    post_message(myToken,"#amm", "BTT buy : 타겟 구매")
            time.sleep(0.5)

            print ("buy13")
            if target_price_btg < current_price_btg and 10000 > btg*current_price_btg:
                if krw > 500500:
                    buy_result = upbit.buy_market_order("KRW-BTG", 500000)
                    post_message(myToken,"#amm", "BTG buy : 타겟 구매")
            time.sleep(0.5)
            
            print ("buy14")
            if target_price_bch < current_price_bch and 10000 > bch*current_price_bch:
                if krw > 500500:
                    buy_result = upbit.buy_market_order("KRW-BCH", 500000)
                    post_message(myToken,"#amm", "BCH buy : 타겟 구매")
            time.sleep(0.5)

            print ("buy15")
            if target_price_neo < current_price_neo and 10000 > neo*current_price_neo:
                if krw > 500500:
                    buy_result = upbit.buy_market_order("KRW-NEO", 500000)
                    post_message(myToken,"#amm", "NEO buy : 타겟 구매")
            time.sleep(0.5)


            #타겟 가격보다 20%이상 상승 시, 20만원 밑으로 남기고 25%씩 매도 (마이 묵었다)
            print ("sell1")
            if target_price_btc*1.20 < current_price_btc:
                if btc*current_price_btc > 200000:
                    sell_result = upbit.sell_market_order("KRW-BTC", btc*0.25)
                    post_message(myToken,"#amm", "BTC sell: 익절 흐믓")
            time.sleep(0.5)

            print ("sell2")
            if target_price_eth*1.20 < current_price_eth:
                if eth*current_price_eth > 200000:
                    sell_result = upbit.sell_market_order("KRW-ETH", eth*0.25)
                    post_message(myToken,"#amm", "ETH sell: 익절 흐믓")
            time.sleep(0.5)

            print ("sell3")
            if target_price_eos*1.20 < current_price_eos:
                if eos*current_price_eos > 200000:
                    sell_result = upbit.sell_market_order("KRW-EOS", eos*0.25)
                    post_message(myToken,"#amm", "EOS sell: 익절 흐믓")
            time.sleep(0.5)

            print ("sell4")
            if target_price_doge*1.20 < current_price_doge:
                if doge*current_price_doge > 200000:
                    sell_result = upbit.sell_market_order("KRW-DOGE", doge*0.25)
                    post_message(myToken,"#amm", "DOGE sell: 익절 흐믓")
            time.sleep(0.5)

            print ("sell5")
            if target_price_xrp*1.20 < current_price_xrp:
                if xrp*current_price_xrp > 200000:
                    sell_result = upbit.sell_market_order("KRW-XRP", xrp*0.25)
                    post_message(myToken,"#amm", "XRP sell: 익절 흐믓")
            time.sleep(0.5)

            print ("sell6")
            if target_price_ada*1.20 < current_price_ada:
                if ada*current_price_ada > 200000:
                    sell_result = upbit.sell_market_order("KRW-ADA", ada*0.25)
                    post_message(myToken,"#amm", "ADA sell: 익절 흐믓")
            time.sleep(0.5)
            
            print ("sell7")
            if target_price_chz*1.20 < current_price_chz:
                if chz*current_price_chz > 200000:
                    sell_result = upbit.sell_market_order("KRW-CHZ", chz*0.25)
                    post_message(myToken,"#amm", "CHZ sell: 익절 흐믓")
            time.sleep(0.5)

            print ("sell8")
            if target_price_dawn*1.20 < current_price_dawn:
                if dawn*current_price_dawn > 200000:
                    sell_result = upbit.sell_market_order("KRW-DAWN", dawn*0.25)
                    post_message(myToken,"#amm", "DAWN sell: 익절 흐믓")
            time.sleep(0.5)

            print ("sell9")
            if target_price_pci*1.20 < current_price_pci:
                if pci*current_price_pci > 200000:
                    sell_result = upbit.sell_market_order("KRW-PCI", pci*0.25)
                    post_message(myToken,"#amm", "PCI sell: 익절 흐믓")
            time.sleep(0.5)

            print ("sell10")
            if target_price_vet*1.20 < current_price_vet:
                if vet*current_price_vet > 200000:
                    sell_result = upbit.sell_market_order("KRW-VET", vet*0.25)
                    post_message(myToken,"#amm", "VET sell: 익절 흐믓")
            time.sleep(0.5)

            print ("sell11")
            if target_price_etc*1.20 < current_price_etc:
                if etc*current_price_etc > 200000:
                    sell_result = upbit.sell_market_order("KRW-ETC", etc*0.25)
                    post_message(myToken,"#amm", "ETC sell: 익절 흐믓")
            time.sleep(0.5)

            print ("sell12")
            if target_price_btt*1.20 < current_price_btt:
                if btt*current_price_btt > 200000:
                    sell_result = upbit.sell_market_order("KRW-BTT", btt*0.25)
                    post_message(myToken,"#amm", "BTT sell: 익절 흐믓")
            time.sleep(0.5)

            print ("sell13")
            if target_price_btg*1.20 < current_price_btg:
                if btg*current_price_btg > 200000:
                    sell_result = upbit.sell_market_order("KRW-BTG", btg*0.25)
                    post_message(myToken,"#amm", "BTG sell: 익절 흐믓")
            time.sleep(0.5)

            print ("sell14")
            if target_price_bch*1.20 < current_price_bch:
                if bch*current_price_bch > 200000:
                    sell_result = upbit.sell_market_order("KRW-BCH", bch*0.25)
                    post_message(myToken,"#amm", "BCH sell: 익절 흐믓")
            time.sleep(0.5)

            print ("sell15")
            if target_price_neo*1.20 < current_price_neo:
                if neo*current_price_neo > 200000:
                    sell_result = upbit.sell_market_order("KRW-NEO", neo*0.25)
                    post_message(myToken,"#amm", "NEO sell: 익절 흐믓")
            time.sleep(0.5)


            #떨어진거 줍줍 한탕 노리자 (10%~18% 떨어지면 200,000 추가 매수)
            
            print ("gazua1")
            if current_price_btc < yesterday_price_btc*0.90 and current_price_btc > yesterday_price_btc*0.82 and 10000 > btc*current_price_btc:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-BTC", 200000)
                    post_message(myToken,"#amm", "BTC buy : 가즈아 구매")
            time.sleep(0.5)

            print ("gazua2")
            if current_price_eth < yesterday_price_eth*0.90 and current_price_eth > yesterday_price_eth*0.82 and 10000 > eth*current_price_eth:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-ETH", 200000)
                    post_message(myToken,"#amm", "ETH buy : 가즈아 구매")
            time.sleep(0.5)

            print ("gazua3")
            if current_price_eos < yesterday_price_eos*0.90 and current_price_eos > yesterday_price_eos*0.82 and 10000 > eos*current_price_eos:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-EOS", 200000)
                    post_message(myToken,"#amm", "EOS buy : 가즈아 구매")
            time.sleep(0.5)
            
            print ("gazua4")
            if current_price_doge < yesterday_price_doge*0.90 and current_price_doge > yesterday_price_doge*0.82 and 10000 > doge*current_price_doge:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-DOGE", 200000)
                    post_message(myToken,"#amm", "DOGE buy : 가즈아 구매")
            time.sleep(0.5)

            print ("gazua5")
            if current_price_xrp < yesterday_price_xrp*0.90 and current_price_xrp > yesterday_price_xrp*0.82 and 10000 > xrp*current_price_xrp:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-XRP", 200000)
                    post_message(myToken,"#amm", "XRP buy : 가즈아 구매")
            time.sleep(0.5)

            print ("gazua6")
            if current_price_ada < yesterday_price_ada*0.90 and current_price_ada > yesterday_price_ada*0.82 and 10000 > ada*current_price_ada:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-ADA", 200000)
                    post_message(myToken,"#amm", "ADA buy : 가즈아 구매")
            time.sleep(0.5)

            print ("gazua7")
            if current_price_chz < yesterday_price_chz*0.90 and current_price_chz > yesterday_price_chz*0.82 and 10000 > chz*current_price_chz:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-CHZ", 200000)
                    post_message(myToken,"#amm", "CHZ buy : 가즈아 구매")
            time.sleep(0.5)

            print ("gazua8")
            if current_price_dawn < yesterday_price_dawn*0.90 and current_price_dawn > yesterday_price_dawn*0.82 and 10000 > dawn*current_price_dawn:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-DAWN", 200000)
                    post_message(myToken,"#amm", "DAWN buy : 가즈아 구매")
            time.sleep(0.5)

            print ("gazua9")
            if current_price_pci < yesterday_price_pci*0.90 and current_price_pci > yesterday_price_pci*0.82 and 10000 > pci*current_price_pci:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-PCI", 200000)
                    post_message(myToken,"#amm", "PCI buy : 가즈아 구매")
            time.sleep(0.5)

            print ("gazua10")
            if current_price_vet < yesterday_price_vet*0.90 and current_price_vet > yesterday_price_vet*0.82 and 10000 > vet*current_price_vet:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-VET", 200000)
                    post_message(myToken,"#amm", "VET buy : 가즈아 구매")
            time.sleep(0.5)

            print ("gazua11")
            if current_price_etc < yesterday_price_etc*0.90 and current_price_etc > yesterday_price_etc*0.82 and 10000 > etc*current_price_etc:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-ETC", 200000)
                    post_message(myToken,"#amm", "ETC buy : 가즈아 구매")
            time.sleep(0.5)

            print ("gazua12")
            if current_price_btt < yesterday_price_btt*0.90 and current_price_btt > yesterday_price_btt*0.82 and 10000 > btt*current_price_btt:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-BTT", 200000)
                    post_message(myToken,"#amm", "BTT buy : 가즈아 구매")
            time.sleep(0.5)

            print ("gazua13")
            if current_price_btg < yesterday_price_btg*0.90 and current_price_btg > yesterday_price_btg*0.82 and 10000 > btg*current_price_btg:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-BTG", 200000)
                    post_message(myToken,"#amm", "BTG buy : 가즈아 구매")
            time.sleep(0.5)

            print ("gazua14")
            if current_price_bch < yesterday_price_bch*0.90 and current_price_bch > yesterday_price_bch*0.82 and 10000 > bch*current_price_bch:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-BCH", 200000)
                    post_message(myToken,"#amm", "BCH buy : 가즈아 구매")
            time.sleep(0.5)

            print ("gazua15")
            if current_price_neo < yesterday_price_neo*0.90 and current_price_neo > yesterday_price_neo*0.82 and 10000 > neo*current_price_neo:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-NEO", 200000)
                    post_message(myToken,"#amm", "NEO buy : 가즈아 구매")
            time.sleep(0.5)


            #어제 가격보다 20%이상 하락 시, 다팔아
            
            print ("mang1")            
            if current_price_btc < yesterday_price_btc*0.8:
                if btc*current_price_btc > 5000:
                    sell_result = upbit.sell_market_order("KRW-BTC", btc*0.9995)
                    post_message(myToken,"#amm", "BTC sell all: 망했어요")
            time.sleep(0.5)

            print ("mang2")
            if current_price_eth < yesterday_price_eth*0.8:
                if eth*current_price_eth > 5000:
                    sell_result = upbit.sell_market_order("KRW-ETH", eth*0.9995)
                    post_message(myToken,"#amm", "ETH sell all: 망했어요")
            time.sleep(0.5)

            print ("mang3")
            if current_price_eos < yesterday_price_eos*0.8:
                if eos*current_price_eos > 5000:
                    sell_result = upbit.sell_market_order("KRW-EOS", eos*0.9995)
                    post_message(myToken,"#amm", "EOS sell all: 망했어요")
            time.sleep(0.5)

            print ("mang4")
            if current_price_doge < yesterday_price_doge*0.8:
                if doge*current_price_doge > 5000:
                    sell_result = upbit.sell_market_order("KRW-DOGE", doge*0.9995)
                    post_message(myToken,"#amm", "DOGE sell all: 망했어요")
            time.sleep(0.5)

            print ("mang5")
            if current_price_xrp < yesterday_price_xrp*0.8:
                if xrp*current_price_xrp > 5000:
                    sell_result = upbit.sell_market_order("KRW-XRP", xrp*0.9995)
                    post_message(myToken,"#amm", "XRP sell all: 망했어요")
            time.sleep(0.5)


            print ("mang6")
            if current_price_ada < yesterday_price_ada*0.8:
                if ada*current_price_ada > 5000:
                    sell_result = upbit.sell_market_order("KRW-ADA", ada*0.9995)
                    post_message(myToken,"#amm", "ADA sell all: 망했어요")
            time.sleep(0.5)

            print ("mang7")    
            if current_price_chz < yesterday_price_chz*0.8:
                if chz*current_price_chz > 5000:
                    sell_result = upbit.sell_market_order("KRW-CHZ", chz*0.9995)
                    post_message(myToken,"#amm", "CHZ sell all: 망했어요")
            time.sleep(0.5)

            print ("mang8")
            if current_price_dawn < yesterday_price_dawn*0.8:
                if dawn*current_price_dawn > 5000:
                    sell_result = upbit.sell_market_order("KRW-DAWN", dawn*0.9995)
                    post_message(myToken,"#amm", "DAWN sell all: 망했어요")
            time.sleep(0.5)

            print ("mang9")
            if current_price_pci < yesterday_price_pci*0.8:
                if pci*current_price_pci > 5000:
                    sell_result = upbit.sell_market_order("KRW-PCI", pci*0.9995)
                    post_message(myToken,"#amm", "PCI sell all: 망했어요")
            time.sleep(0.5)

            print ("mang10")
            if current_price_vet < yesterday_price_vet*0.8:
                if vet*current_price_vet > 5000:
                    sell_result = upbit.sell_market_order("KRW-VET", vet*0.9995)
                    post_message(myToken,"#amm", "VET sell all: 망했어요")
            time.sleep(0.5)

            print ("mang11")
            if current_price_etc < yesterday_price_etc*0.8:
                if etc*current_price_etc > 5000:
                    sell_result = upbit.sell_market_order("KRW-ETC", etc*0.9995)
                    post_message(myToken,"#amm", "ETC sell all: 망했어요")
            time.sleep(0.5)

            print ("mang12")
            if current_price_btt < yesterday_price_btt*0.8:
                if btt*current_price_btt > 5000:
                    sell_result = upbit.sell_market_order("KRW-BTT", btt*0.9995)
                    post_message(myToken,"#amm", "BTT sell all: 망했어요")
            time.sleep(0.5)

            print ("mang13")
            if current_price_btg < yesterday_price_btg*0.8:
                if btg*current_price_btg > 5000:
                    sell_result = upbit.sell_market_order("KRW-BTG", btg*0.9995)
                    post_message(myToken,"#amm", "BTG sell all: 망했어요")
            time.sleep(0.5)

            print ("mang14")
            if current_price_bch < yesterday_price_bch*0.8:
                if bch*current_price_bch > 5000:
                    sell_result = upbit.sell_market_order("KRW-BCH", bch*0.9995)
                    post_message(myToken,"#amm", "BCH sell all: 망했어요")
            time.sleep(0.5)

            print ("mang15")
            if current_price_neo < yesterday_price_neo*0.8:
                if neo*current_price_neo > 5000:
                    sell_result = upbit.sell_market_order("KRW-NEO", neo*0.9995)
                    post_message(myToken,"#amm", "NEO sell all: 망했어요")
            time.sleep(0.5)
            
            print("done")

            
        #장마감 - 가진거 다팔아
        else:
            btc = get_balance("BTC")
            current_price_btc = get_current_price("KRW-BTC")
            time.sleep(0.5)
            if btc*current_price_btc > 5000:
                sell_result = upbit.sell_market_order("KRW-BTC", btc*0.9995)
                post_message(myToken,"#amm", "BTC sell all : 장마감")

            eth = get_balance("ETH")
            current_price_eth = get_current_price("KRW-ETH")
            time.sleep(0.5)
            if eth*current_price_eth > 5000:
                sell_result = upbit.sell_market_order("KRW-ETH", eth*0.9995)
                post_message(myToken,"#amm", "ETH sell all : 장마감")

            eos = get_balance("EOS")
            current_price_eos = get_current_price("KRW-EOS")
            time.sleep(0.5)
            if eos*current_price_eos > 5000:
                sell_result = upbit.sell_market_order("KRW-EOS", eos*0.9995)
                post_message(myToken,"#amm", "EOS sell all : 장마감")
            
            doge = get_balance("DOGE")
            current_price_doge = get_current_price("KRW-DOGE")
            time.sleep(0.5)
            if doge*current_price_doge > 5000:
                sell_result = upbit.sell_market_order("KRW-DOGE", doge*0.9995)
                post_message(myToken,"#amm", "DOGE sell all : 장마감")

            xrp = get_balance("XRP")
            current_price_xrp = get_current_price("KRW-XRP")
            time.sleep(0.5)
            if xrp*current_price_xrp > 5000:
                sell_result = upbit.sell_market_order("KRW-XRP", xrp*0.9995)
                post_message(myToken,"#amm", "XRP sell all : 장마감")

            ada = get_balance("ADA")
            current_price_ada = get_current_price("KRW-ADA")
            time.sleep(0.5)
            if ada*current_price_ada > 5000:
                sell_result = upbit.sell_market_order("KRW-ADA", ada*0.9995)
                post_message(myToken,"#amm", "ADA sell all : 장마감")

            chz = get_balance("CHZ")
            current_price_chz = get_current_price("KRW-CHZ")
            time.sleep(0.5)
            if chz*current_price_chz > 5000:
                sell_result = upbit.sell_market_order("KRW-CHZ", chz*0.9995)
                post_message(myToken,"#amm", "CHZ sell all : 장마감")

            dawn = get_balance("DAWN")
            current_price_dawn = get_current_price("KRW-DAWN")
            time.sleep(0.5)
            if dawn*current_price_dawn > 5000:
                sell_result = upbit.sell_market_order("KRW-DAWN", dawn*0.9995)
                post_message(myToken,"#amm", "DAWN sell all : 장마감")

            pci = get_balance("PCI")
            current_price_pci = get_current_price("KRW-PCI")
            time.sleep(0.5)
            if pci*current_price_pci > 5000:
                sell_result = upbit.sell_market_order("KRW-PCI", pci*0.9995)
                post_message(myToken,"#amm", "PCI sell all : 장마감")

            vet = get_balance("VET")
            current_price_vet = get_current_price("KRW-VET")
            time.sleep(0.5)
            if vet*current_price_vet > 5000:
                sell_result = upbit.sell_market_order("KRW-VET", vet*0.9995)
                post_message(myToken,"#amm", "VET sell all : 장마감")

            etc = get_balance("ETC")
            current_price_etc = get_current_price("KRW-ETC")
            time.sleep(0.5)
            if etc*current_price_etc > 5000:
                sell_result = upbit.sell_market_order("KRW-ETC", etc*0.9995)
                post_message(myToken,"#amm", "ETC sell all : 장마감")

            btt = get_balance("BTT")
            current_price_btt = get_current_price("KRW-BTT")
            time.sleep(0.5)
            if btt*current_price_btt > 5000:
                sell_result = upbit.sell_market_order("KRW-BTT", btt*0.9995)
                post_message(myToken,"#amm", "BTT sell all : 장마감")
            
            btg = get_balance("BTG")
            current_price_btg = get_current_price("KRW-BTG")
            time.sleep(0.5)
            if btg*current_price_btg > 5000:
                sell_result = upbit.sell_market_order("KRW-BTG", btg*0.9995)
                post_message(myToken,"#amm", "BTG sell all : 장마감")

            bch = get_balance("BCH")
            current_price_bch = get_current_price("KRW-BCH")
            time.sleep(0.5)
            if bch*current_price_bch > 5000:
                sell_result = upbit.sell_market_order("KRW-BCH", bch*0.9995)
                post_message(myToken,"#amm", "BCH sell all : 장마감")

            neo = get_balance("NEO")
            current_price_neo = get_current_price("KRW-NEO")
            time.sleep(0.5)
            if neo*current_price_neo > 5000:
                sell_result = upbit.sell_market_order("KRW-NEO", neo*0.9995)
                post_message(myToken,"#amm", "NEO sell all : 장마감")

        time.sleep(1)

    #에러메세지 출력
    except Exception as e:
        print(e)
        post_message(myToken,"#amm", e)
        time.sleep(1)