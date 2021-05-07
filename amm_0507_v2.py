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
post_message(myToken,"#amm", "Autotradestart: 0507_v2")
post_message(myToken,"#amm", "  비트코인-BTC // 이더리움-ETH // 이오스-EOS")
time.sleep(0.3)
post_message(myToken,"#amm", "  도지코인-DOGE // 리플-XRP // 에이다-ADA")
time.sleep(0.3)
post_message(myToken,"#amm", "  베이직어텐션-BAT // 라이트코인-LTC // 페이코인-PCI")
time.sleep(0.3)
post_message(myToken,"#amm", "  비체인-VET // 이더리움클래식-ETC // 체인링크-LINK")
time.sleep(0.3)
post_message(myToken,"#amm", "  비트코인골드-BTG // 비트코인캐시-BCH // 네오-NEO")
time.sleep(0.3)

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
            target_price_eos = get_target_price("KRW-EOS", 0.3)
            print ("targetprice1")
            time.sleep(0.5)
            target_price_doge = get_target_price("KRW-DOGE", 0.2)
            target_price_xrp = get_target_price("KRW-XRP", 0.4)
            target_price_ada = get_target_price("KRW-ADA", 0.4)
            print ("targetprice2")
            time.sleep(0.5)
            target_price_bat = get_target_price("KRW-BAT", 0.4)
            target_price_ltc = get_target_price("KRW-LTC", 0.2)
            target_price_pci = get_target_price("KRW-PCI", 0.4)
            print ("targetprice3")
            time.sleep(0.5)
            target_price_vet = get_target_price("KRW-VET", 0.3)
            target_price_etc = get_target_price("KRW-ETC", 0.1)
            target_price_link = get_target_price("KRW-LINK", 0.2)
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
            bat = get_balance("BAT")
            ltc = get_balance("LTC")
            pci = get_balance("PCI")
            print ("balance3")
            time.sleep(0.5)
            vet = get_balance("VET")
            etc = get_balance("ETC")
            link = get_balance("LINK")
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
            current_price_bat = get_current_price("KRW-BAT")
            yesterday_price_bat = get_yesterday_price("KRW-BAT")
            current_price_ltc = get_current_price("KRW-LTC")
            yesterday_price_ltc = get_yesterday_price("KRW-LTC")
            current_price_pci = get_current_price("KRW-PCI")
            yesterday_price_pci = get_yesterday_price("KRW-PCI")
            print ("price3")
            time.sleep(0.5)
            current_price_vet = get_current_price("KRW-VET")
            yesterday_price_vet = get_yesterday_price("KRW-VET")
            current_price_etc = get_current_price("KRW-ETC")
            yesterday_price_etc = get_yesterday_price("KRW-ETC")
            current_price_link = get_current_price("KRW-LINK")
            yesterday_price_link = get_yesterday_price("KRW-LINK")
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

            #타겟 가격돌파 & 현재 가지고있는 코인 평가금이 10,000 이하 & 어제 가격보다 10%미만 상승일 때, 500,000 매수
            
            print ("buy 1")
            if target_price_btc < current_price_btc and 10000 > btc*current_price_btc:
                if krw > 500500 and yesterday_price_btc*1.1 > current_price_btc:
                    buy_result = upbit.buy_market_order("KRW-BTC", 500000)
                    post_message(myToken,"#amm", "BTC buy: 타겟가격 돌파_500,000")
            time.sleep(0.5)

            print ("buy 2")
            if target_price_eth < current_price_eth and 10000 > eth*current_price_eth:
                if krw > 500500 and yesterday_price_eth*1.1 > current_price_eth:
                    buy_result = upbit.buy_market_order("KRW-ETH", 500000)
                    post_message(myToken,"#amm", "ETH buy: 타겟가격 돌파_500,000")
            time.sleep(0.5)

            print ("buy 3")
            if target_price_eos < current_price_eos and 10000 > eos*current_price_eos:
                if krw > 500500 and yesterday_price_eos*1.1 > current_price_eos:
                    buy_result = upbit.buy_market_order("KRW-EOS", 500000)
                    post_message(myToken,"#amm", "EOS buy: 타겟가격 돌파_500,000")
            time.sleep(0.5)
            
            print ("buy 4")
            if target_price_doge < current_price_doge and 10000 > doge*current_price_doge:
                if krw > 500500 and yesterday_price_doge*1.1 > current_price_doge:
                    buy_result = upbit.buy_market_order("KRW-DOGE", 500000)
                    post_message(myToken,"#amm", "DOGE buy: 타겟가격 돌파_500,000")
            time.sleep(0.5)

            print ("buy 5")
            if target_price_xrp < current_price_xrp and 10000 > xrp*current_price_xrp:
                if krw > 500500 and yesterday_price_xrp*1.1 > current_price_xrp:
                    buy_result = upbit.buy_market_order("KRW-XRP", 500000)
                    post_message(myToken,"#amm", "XRP buy: 타겟가격 돌파_500,000")
            time.sleep(0.5)

            print ("buy 6")
            if target_price_ada < current_price_ada and 10000 > ada*current_price_ada:
                if krw > 500500 and yesterday_price_ada*1.1 > current_price_ada:
                    buy_result = upbit.buy_market_order("KRW-ADA", 500000)
                    post_message(myToken,"#amm", "ADA buy: 타겟가격 돌파_500,000")
            time.sleep(0.5)

            print ("buy 7")
            if target_price_bat < current_price_bat and 10000 > bat*current_price_bat:
                if krw > 500500 and yesterday_price_bat*1.1 > current_price_bat:
                    buy_result = upbit.buy_market_order("KRW-BAT", 500000)
                    post_message(myToken,"#amm", "BAT buy: 타겟가격 돌파_500,000")
            time.sleep(0.5)

            print ("buy 8")
            if target_price_ltc < current_price_ltc and 10000 > ltc*current_price_ltc:
                if krw > 500500 and yesterday_price_ltc*1.1 > current_price_ltc:
                    buy_result = upbit.buy_market_order("KRW-LTC", 500000)
                    post_message(myToken,"#amm", "LTC buy: 타겟가격 돌파_500,000")
            time.sleep(0.5)

            print ("buy 9")
            if target_price_pci < current_price_pci and 10000 > pci*current_price_pci:
                if krw > 500500 and yesterday_price_pci*1.1 > current_price_pci:
                    buy_result = upbit.buy_market_order("KRW-PCI", 500000)
                    post_message(myToken,"#amm", "PCI buy: 타겟가격 돌파_500,000")
            time.sleep(0.5)

            print ("buy 10")
            if target_price_vet < current_price_vet and 10000 > vet*current_price_vet:
                if krw > 500500 and yesterday_price_vet*1.1 > current_price_vet:
                    buy_result = upbit.buy_market_order("KRW-VET", 500000)
                    post_message(myToken,"#amm", "VET buy: 타겟가격 돌파_500,000")
            time.sleep(0.5)
            
            print ("buy 11")
            if target_price_etc < current_price_etc and 10000 > etc*current_price_etc:
                if krw > 500500 and yesterday_price_etc*1.1 > current_price_etc:
                    buy_result = upbit.buy_market_order("KRW-ETC", 500000)
                    post_message(myToken,"#amm", "ETC buy: 타겟가격 돌파_500,000")
            time.sleep(0.5)

            print ("buy 12")
            if target_price_link < current_price_link and 10000 > link*current_price_link:
                if krw > 500500 and yesterday_price_link*1.1 > current_price_link:
                    buy_result = upbit.buy_market_order("KRW-LINK", 500000)
                    post_message(myToken,"#amm", "LINK buy: 타겟가격 돌파_500,000")
            time.sleep(0.5)

            print ("buy 13")
            if target_price_btg < current_price_btg and 10000 > btg*current_price_btg:
                if krw > 500500 and yesterday_price_btg*1.1 > current_price_btg:
                    buy_result = upbit.buy_market_order("KRW-BTG", 500000)
                    post_message(myToken,"#amm", "BTG buy: 타겟가격 돌파_500,000")
            time.sleep(0.5)
            
            print ("buy 14")
            if target_price_bch < current_price_bch and 10000 > bch*current_price_bch:
                if krw > 500500 and yesterday_price_bch*1.1 > current_price_bch:
                    buy_result = upbit.buy_market_order("KRW-BCH", 500000)
                    post_message(myToken,"#amm", "BCH buy: 타겟가격 돌파_500,000")
            time.sleep(0.5)

            print ("buy 15")
            if target_price_neo < current_price_neo and 10000 > neo*current_price_neo:
                if krw > 500500 and yesterday_price_neo*1.1 > current_price_neo:
                    buy_result = upbit.buy_market_order("KRW-NEO", 500000)
                    post_message(myToken,"#amm", "NEO buy: 타겟가격 돌파_500,000")
            time.sleep(0.5)

            #타겟 가격보다 20%이상 상승 시, 30만원 밑으로 남기고 50%씩 매도 (마이 묵었다)
            print ("sell 1")
            if target_price_btc*1.20 < current_price_btc:
                if btc*current_price_btc > 299999:
                    sell_result = upbit.sell_market_order("KRW-BTC", btc*0.5)
                    post_message(myToken,"#amm", "BTC sell: 타겟+20%_절반 매도")
            time.sleep(0.5)

            print ("sell 2")
            if target_price_eth*1.20 < current_price_eth:
                if eth*current_price_eth > 299999:
                    sell_result = upbit.sell_market_order("KRW-ETH", eth*0.5)
                    post_message(myToken,"#amm", "ETH sell: 타겟+20%_절반 매도")
            time.sleep(0.5)

            print ("sell 3")
            if target_price_eos*1.20 < current_price_eos:
                if eos*current_price_eos > 299999:
                    sell_result = upbit.sell_market_order("KRW-EOS", eos*0.5)
                    post_message(myToken,"#amm", "EOS sell: 타겟+20%_절반 매도")
            time.sleep(0.5)

            print ("sell 4")
            if target_price_doge*1.20 < current_price_doge:
                if doge*current_price_doge > 299999:
                    sell_result = upbit.sell_market_order("KRW-DOGE", doge*0.5)
                    post_message(myToken,"#amm", "DOGE sell: 타겟+20%_절반 매도")
            time.sleep(0.5)

            print ("sell 5")
            if target_price_xrp*1.20 < current_price_xrp:
                if xrp*current_price_xrp > 299999:
                    sell_result = upbit.sell_market_order("KRW-XRP", xrp*0.5)
                    post_message(myToken,"#amm", "XRP sell: 타겟+20%_절반 매도")
            time.sleep(0.5)

            print ("sell 6")
            if target_price_ada*1.20 < current_price_ada:
                if ada*current_price_ada > 299999:
                    sell_result = upbit.sell_market_order("KRW-ADA", ada*0.5)
                    post_message(myToken,"#amm", "ADA sell: 타겟+20%_절반 매도")
            time.sleep(0.5)
            
            print ("sell 7")
            if target_price_bat*1.20 < current_price_bat:
                if bat*current_price_bat > 299999:
                    sell_result = upbit.sell_market_order("KRW-BAT", bat*0.5)
                    post_message(myToken,"#amm", "BAT sell: 타겟+20%_절반 매도")
            time.sleep(0.5)

            print ("sell 8")
            if target_price_ltc*1.20 < current_price_ltc:
                if ltc*current_price_ltc > 299999:
                    sell_result = upbit.sell_market_order("KRW-LTC", ltc*0.5)
                    post_message(myToken,"#amm", "LTC sell: 타겟+20%_절반 매도")
            time.sleep(0.5)

            print ("sell 9")
            if target_price_pci*1.20 < current_price_pci:
                if pci*current_price_pci > 299999:
                    sell_result = upbit.sell_market_order("KRW-PCI", pci*0.5)
                    post_message(myToken,"#amm", "PCI sell: 타겟+20%_절반 매도")
            time.sleep(0.5)

            print ("sell 10")
            if target_price_vet*1.20 < current_price_vet:
                if vet*current_price_vet > 299999:
                    sell_result = upbit.sell_market_order("KRW-VET", vet*0.5)
                    post_message(myToken,"#amm", "VET sell: 타겟+20%_절반 매도")
            time.sleep(0.5)

            print ("sell 11")
            if target_price_etc*1.20 < current_price_etc:
                if etc*current_price_etc > 299999:
                    sell_result = upbit.sell_market_order("KRW-ETC", etc*0.5)
                    post_message(myToken,"#amm", "ETC sell: 타겟+20%_절반 매도")
            time.sleep(0.5)

            print ("sell 12")
            if target_price_link*1.20 < current_price_link:
                if link*current_price_link > 299999:
                    sell_result = upbit.sell_market_order("KRW-LINK", link*0.5)
                    post_message(myToken,"#amm", "LINK sell: 타겟+20%_절반 매도")
            time.sleep(0.5)

            print ("sell 13")
            if target_price_btg*1.20 < current_price_btg:
                if btg*current_price_btg > 299999:
                    sell_result = upbit.sell_market_order("KRW-BTG", btg*0.5)
                    post_message(myToken,"#amm", "BTG sell: 타겟+20%_절반 매도")
            time.sleep(0.5)

            print ("sell 14")
            if target_price_bch*1.20 < current_price_bch:
                if bch*current_price_bch > 299999:
                    sell_result = upbit.sell_market_order("KRW-BCH", bch*0.5)
                    post_message(myToken,"#amm", "BCH sell: 타겟+20%_절반 매도")
            time.sleep(0.5)

            print ("sell 15")
            if target_price_neo*1.20 < current_price_neo:
                if neo*current_price_neo > 299999:
                    sell_result = upbit.sell_market_order("KRW-NEO", neo*0.5)
                    post_message(myToken,"#amm", "NEO sell: 타겟+20%_절반 매도")
            time.sleep(0.5)

            #떨어진거 줍줍 한탕 노리자 (어제보다 10%~18% 떨어지면 200,000 추가 매수)
            
            print ("gazua 1")
            if current_price_btc < yesterday_price_btc*0.90 and current_price_btc > yesterday_price_btc*0.82 and 200000 > btc*current_price_btc:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-BTC", 200000)
                    post_message(myToken,"#amm", "BTC buy: 종가-10%_200,000")
            time.sleep(0.5)

            print ("gazua 2")
            if current_price_eth < yesterday_price_eth*0.90 and current_price_eth > yesterday_price_eth*0.82 and 200000 > eth*current_price_eth:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-ETH", 200000)
                    post_message(myToken,"#amm", "ETH buy: 종가-10%_200,000")
            time.sleep(0.5)

            print ("gazua 3")
            if current_price_eos < yesterday_price_eos*0.90 and current_price_eos > yesterday_price_eos*0.82 and 200000 > eos*current_price_eos:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-EOS", 200000)
                    post_message(myToken,"#amm", "EOS buy: 종가-10%_200,000")
            time.sleep(0.5)
            
            print ("gazua 4")
            if current_price_doge < yesterday_price_doge*0.90 and current_price_doge > yesterday_price_doge*0.82 and 200000 > doge*current_price_doge:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-DOGE", 200000)
                    post_message(myToken,"#amm", "DOGE buy: 종가-10%_200,000")
            time.sleep(0.5)

            print ("gazua 5")
            if current_price_xrp < yesterday_price_xrp*0.90 and current_price_xrp > yesterday_price_xrp*0.82 and 200000 > xrp*current_price_xrp:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-XRP", 200000)
                    post_message(myToken,"#amm", "XRP buy: 종가-10%_200,000")
            time.sleep(0.5)

            print ("gazua 6")
            if current_price_ada < yesterday_price_ada*0.90 and current_price_ada > yesterday_price_ada*0.82 and 200000 > ada*current_price_ada:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-ADA", 200000)
                    post_message(myToken,"#amm", "ADA buy: 종가-10%_200,000")
            time.sleep(0.5)

            print ("gazua 7")
            if current_price_bat < yesterday_price_bat*0.90 and current_price_bat > yesterday_price_bat*0.82 and 200000 > bat*current_price_bat:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-BAT", 200000)
                    post_message(myToken,"#amm", "BAT buy: 종가-10%_200,000")
            time.sleep(0.5)

            print ("gazua 8")
            if current_price_ltc < yesterday_price_ltc*0.90 and current_price_ltc > yesterday_price_ltc*0.82 and 200000 > ltc*current_price_ltc:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-LTC", 200000)
                    post_message(myToken,"#amm", "LTC buy: 종가-10%_200,000")
            time.sleep(0.5)

            print ("gazua 9")
            if current_price_pci < yesterday_price_pci*0.90 and current_price_pci > yesterday_price_pci*0.82 and 200000 > pci*current_price_pci:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-PCI", 200000)
                    post_message(myToken,"#amm", "PCI buy: 종가-10%_200,000")
            time.sleep(0.5)

            print ("gazua 10")
            if current_price_vet < yesterday_price_vet*0.90 and current_price_vet > yesterday_price_vet*0.82 and 200000 > vet*current_price_vet:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-VET", 200000)
                    post_message(myToken,"#amm", "VET buy: 종가-10%_200,000")
            time.sleep(0.5)

            print ("gazua 11")
            if current_price_etc < yesterday_price_etc*0.90 and current_price_etc > yesterday_price_etc*0.82 and 200000 > etc*current_price_etc:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-ETC", 200000)
                    post_message(myToken,"#amm", "ETC buy: 종가-10%_200,000")
            time.sleep(0.5)

            print ("gazua 12")
            if current_price_link < yesterday_price_link*0.90 and current_price_link > yesterday_price_link*0.82 and 200000 > link*current_price_link:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-LINK", 200000)
                    post_message(myToken,"#amm", "LINK buy: 종가-10%_200,000")
            time.sleep(0.5)

            print ("gazua 13")
            if current_price_btg < yesterday_price_btg*0.90 and current_price_btg > yesterday_price_btg*0.82 and 200000 > btg*current_price_btg:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-BTG", 200000)
                    post_message(myToken,"#amm", "BTG buy: 종가-10%_200,000")
            time.sleep(0.5)

            print ("gazua 14")
            if current_price_bch < yesterday_price_bch*0.90 and current_price_bch > yesterday_price_bch*0.82 and 200000 > bch*current_price_bch:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-BCH", 200000)
                    post_message(myToken,"#amm", "BCH buy: 종가-10%_200,000")
            time.sleep(0.5)

            print ("gazua 15")
            if current_price_neo < yesterday_price_neo*0.90 and current_price_neo > yesterday_price_neo*0.82 and 200000 > neo*current_price_neo:
                if krw > 200100:
                    buy_result = upbit.buy_market_order("KRW-NEO", 200000)
                    post_message(myToken,"#amm", "NEO buy: 종가-10%_200,000")
            time.sleep(0.5)

            #타겟 가격구매 후 5%이상 하락 시, 75%팔아
            
            print ("sonjul 1")            
            if current_price_btc < target_price_btc*0.95:
                if btc*current_price_btc > 400000:
                    sell_result = upbit.sell_market_order("KRW-BTC", btc*0.75)
                    post_message(myToken,"#amm", "BTC sell: 손실 관리_75% 매도")
            time.sleep(0.5)

            print ("sonjul 2")
            if current_price_eth < target_price_eth*0.95:
                if eth*current_price_eth > 400000:
                    sell_result = upbit.sell_market_order("KRW-ETH", eth*0.75)
                    post_message(myToken,"#amm", "ETH sell: 손실 관리_75% 매도")
            time.sleep(0.5)

            print ("sonjul 3")
            if current_price_eos < target_price_eos*0.95:
                if eos*current_price_eos > 400000:
                    sell_result = upbit.sell_market_order("KRW-EOS", eos*0.75)
                    post_message(myToken,"#amm", "EOS sell: 손실 관리_75% 매도")
            time.sleep(0.5)

            print ("sonjul 4")
            if current_price_doge < target_price_doge*0.95:
                if doge*current_price_doge > 400000:
                    sell_result = upbit.sell_market_order("KRW-DOGE", doge*0.75)
                    post_message(myToken,"#amm", "DOGE sell: 손실 관리_75% 매도")
            time.sleep(0.5)

            print ("sonjul 5")
            if current_price_xrp < target_price_xrp*0.95:
                if xrp*current_price_xrp > 400000:
                    sell_result = upbit.sell_market_order("KRW-XRP", xrp*0.75)
                    post_message(myToken,"#amm", "XRP sell: 손실 관리_75% 매도")
            time.sleep(0.5)

            print ("sonjul 6")
            if current_price_ada < target_price_ada*0.95:
                if ada*current_price_ada > 400000:
                    sell_result = upbit.sell_market_order("KRW-ADA", ada*0.75)
                    post_message(myToken,"#amm", "ADA sell: 손실 관리_75% 매도")
            time.sleep(0.5)

            print ("sonjul 7")    
            if current_price_bat < target_price_bat*0.95:
                if bat*current_price_bat > 400000:
                    sell_result = upbit.sell_market_order("KRW-BAT", bat*0.75)
                    post_message(myToken,"#amm", "BAT sell: 손실 관리_75% 매도")
            time.sleep(0.5)

            print ("sonjul 8")
            if current_price_ltc < target_price_ltc*0.95:
                if ltc*current_price_ltc > 400000:
                    sell_result = upbit.sell_market_order("KRW-LTC", ltc*0.75)
                    post_message(myToken,"#amm", "LTC sell: 손실 관리_75% 매도")
            time.sleep(0.5)

            print ("sonjul 9")
            if current_price_pci < target_price_pci*0.95:
                if pci*current_price_pci > 400000:
                    sell_result = upbit.sell_market_order("KRW-PCI", pci*0.75)
                    post_message(myToken,"#amm", "PCI sell: 손실 관리_75% 매도")
            time.sleep(0.5)

            print ("sonjul 10")
            if current_price_vet < target_price_vet*0.95:
                if vet*current_price_vet > 400000:
                    sell_result = upbit.sell_market_order("KRW-VET", vet*0.75)
                    post_message(myToken,"#amm", "VET sell: 손실 관리_75% 매도")
            time.sleep(0.5)

            print ("sonjul 11")
            if current_price_etc < target_price_etc*0.95:
                if etc*current_price_etc > 400000:
                    sell_result = upbit.sell_market_order("KRW-ETC", etc*0.75)
                    post_message(myToken,"#amm", "ETC sell: 손실 관리_75% 매도")
            time.sleep(0.5)

            print ("sonjul 12")
            if current_price_link < target_price_link*0.95:
                if link*current_price_link > 400000:
                    sell_result = upbit.sell_market_order("KRW-LINK", link*0.75)
                    post_message(myToken,"#amm", "LINK sell: 손실 관리_75% 매도")
            time.sleep(0.5)

            print ("sonjul 13")
            if current_price_btg < target_price_btg*0.95:
                if btg*current_price_btg > 400000:
                    sell_result = upbit.sell_market_order("KRW-BTG", btg*0.75)
                    post_message(myToken,"#amm", "BTG sell: 손실 관리_75% 매도")
            time.sleep(0.5)

            print ("sonjul 14")
            if current_price_bch < target_price_bch*0.95:
                if bch*current_price_bch > 400000:
                    sell_result = upbit.sell_market_order("KRW-BCH", bch*0.75)
                    post_message(myToken,"#amm", "BCH sell: 손실 관리_75% 매도")
            time.sleep(0.5)

            print ("sonjul 15")
            if current_price_neo < target_price_neo*0.95:
                if neo*current_price_neo > 400000:
                    sell_result = upbit.sell_market_order("KRW-NEO", neo*0.75)
                    post_message(myToken,"#amm", "NEO sell: 손실 관리_75% 매도")
            time.sleep(0.5)
            

            #어제 가격보다 20%이상 하락 시, 다팔아
            
            print ("mang 1")            
            if current_price_btc < yesterday_price_btc*0.8:
                if btc*current_price_btc > 5000:
                    sell_result = upbit.sell_market_order("KRW-BTC", btc*0.9995)
                    post_message(myToken,"#amm", "BTC sell: 종가-20%_전체매도")
            time.sleep(0.5)

            print ("mang 2")
            if current_price_eth < yesterday_price_eth*0.8:
                if eth*current_price_eth > 5000:
                    sell_result = upbit.sell_market_order("KRW-ETH", eth*0.9995)
                    post_message(myToken,"#amm", "ETH sell: 종가-20%_전체매도")
            time.sleep(0.5)

            print ("mang 3")
            if current_price_eos < yesterday_price_eos*0.8:
                if eos*current_price_eos > 5000:
                    sell_result = upbit.sell_market_order("KRW-EOS", eos*0.9995)
                    post_message(myToken,"#amm", "EOS sell: 종가-20%_전체매도")
            time.sleep(0.5)

            print ("mang 4")
            if current_price_doge < yesterday_price_doge*0.8:
                if doge*current_price_doge > 5000:
                    sell_result = upbit.sell_market_order("KRW-DOGE", doge*0.9995)
                    post_message(myToken,"#amm", "DOGE sell: 종가-20%_전체매도")
            time.sleep(0.5)

            print ("mang 5")
            if current_price_xrp < yesterday_price_xrp*0.8:
                if xrp*current_price_xrp > 5000:
                    sell_result = upbit.sell_market_order("KRW-XRP", xrp*0.9995)
                    post_message(myToken,"#amm", "XRP sell: 종가-20%_전체매도")
            time.sleep(0.5)

            print ("mang 6")
            if current_price_ada < yesterday_price_ada*0.8:
                if ada*current_price_ada > 5000:
                    sell_result = upbit.sell_market_order("KRW-ADA", ada*0.9995)
                    post_message(myToken,"#amm", "ADA sell: 종가-20%_전체매도")
            time.sleep(0.5)

            print ("mang 7")    
            if current_price_bat < yesterday_price_bat*0.8:
                if bat*current_price_bat > 5000:
                    sell_result = upbit.sell_market_order("KRW-BAT", bat*0.9995)
                    post_message(myToken,"#amm", "BAT sell: 종가-20%_전체매도")
            time.sleep(0.5)

            print ("mang 8")
            if current_price_ltc < yesterday_price_ltc*0.8:
                if ltc*current_price_ltc > 5000:
                    sell_result = upbit.sell_market_order("KRW-LTC", ltc*0.9995)
                    post_message(myToken,"#amm", "LTC sell: 종가-20%_전체매도")
            time.sleep(0.5)

            print ("mang 9")
            if current_price_pci < yesterday_price_pci*0.8:
                if pci*current_price_pci > 5000:
                    sell_result = upbit.sell_market_order("KRW-PCI", pci*0.9995)
                    post_message(myToken,"#amm", "PCI sell: 종가-20%_전체매도")
            time.sleep(0.5)

            print ("mang 10")
            if current_price_vet < yesterday_price_vet*0.8:
                if vet*current_price_vet > 5000:
                    sell_result = upbit.sell_market_order("KRW-VET", vet*0.9995)
                    post_message(myToken,"#amm", "VET sell: 종가-20%_전체매도")
            time.sleep(0.5)

            print ("mang 11")
            if current_price_etc < yesterday_price_etc*0.8:
                if etc*current_price_etc > 5000:
                    sell_result = upbit.sell_market_order("KRW-ETC", etc*0.9995)
                    post_message(myToken,"#amm", "ETC sell: 종가-20%_전체매도")
            time.sleep(0.5)

            print ("mang 12")
            if current_price_link < yesterday_price_link*0.8:
                if link*current_price_link > 5000:
                    sell_result = upbit.sell_market_order("KRW-LINK", link*0.9995)
                    post_message(myToken,"#amm", "LINK sell: 종가-20%_전체매도")
            time.sleep(0.5)

            print ("mang 13")
            if current_price_btg < yesterday_price_btg*0.8:
                if btg*current_price_btg > 5000:
                    sell_result = upbit.sell_market_order("KRW-BTG", btg*0.9995)
                    post_message(myToken,"#amm", "BTG sell: 종가-20%_전체매도")
            time.sleep(0.5)

            print ("mang 14")
            if current_price_bch < yesterday_price_bch*0.8:
                if bch*current_price_bch > 5000:
                    sell_result = upbit.sell_market_order("KRW-BCH", bch*0.9995)
                    post_message(myToken,"#amm", "BCH sell: 종가-20%_전체매도")
            time.sleep(0.5)

            print ("mang 15")
            if current_price_neo < yesterday_price_neo*0.8:
                if neo*current_price_neo > 5000:
                    sell_result = upbit.sell_market_order("KRW-NEO", neo*0.9995)
                    post_message(myToken,"#amm", "NEO sell: 종가-20%_전체매도")
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

            eos = get_balance("EOS")
            current_price_eos = get_current_price("KRW-EOS")
            time.sleep(0.5)
            if eos*current_price_eos > 5000:
                sell_result = upbit.sell_market_order("KRW-EOS", eos*0.9995)
                post_message(myToken,"#amm", "EOS sell: 장마감")
            
            doge = get_balance("DOGE")
            current_price_doge = get_current_price("KRW-DOGE")
            time.sleep(0.5)
            if doge*current_price_doge > 5000:
                sell_result = upbit.sell_market_order("KRW-DOGE", doge*0.9995)
                post_message(myToken,"#amm", "DOGE sell: 장마감")

            xrp = get_balance("XRP")
            current_price_xrp = get_current_price("KRW-XRP")
            time.sleep(0.5)
            if xrp*current_price_xrp > 5000:
                sell_result = upbit.sell_market_order("KRW-XRP", xrp*0.9995)
                post_message(myToken,"#amm", "XRP sell: 장마감")

            ada = get_balance("ADA")
            current_price_ada = get_current_price("KRW-ADA")
            time.sleep(0.5)
            if ada*current_price_ada > 5000:
                sell_result = upbit.sell_market_order("KRW-ADA", ada*0.9995)
                post_message(myToken,"#amm", "ADA sell: 장마감")

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

            pci = get_balance("PCI")
            current_price_pci = get_current_price("KRW-PCI")
            time.sleep(0.5)
            if pci*current_price_pci > 5000:
                sell_result = upbit.sell_market_order("KRW-PCI", pci*0.9995)
                post_message(myToken,"#amm", "PCI sell: 장마감")

            vet = get_balance("VET")
            current_price_vet = get_current_price("KRW-VET")
            time.sleep(0.5)
            if vet*current_price_vet > 5000:
                sell_result = upbit.sell_market_order("KRW-VET", vet*0.9995)
                post_message(myToken,"#amm", "VET sell: 장마감")

            etc = get_balance("ETC")
            current_price_etc = get_current_price("KRW-ETC")
            time.sleep(0.5)
            if etc*current_price_etc > 5000:
                sell_result = upbit.sell_market_order("KRW-ETC", etc*0.9995)
                post_message(myToken,"#amm", "ETC sell: 장마감")

            link = get_balance("LINK")
            current_price_link = get_current_price("KRW-LINK")
            time.sleep(0.5)
            if link*current_price_link > 5000:
                sell_result = upbit.sell_market_order("KRW-LINK", link*0.9995)
                post_message(myToken,"#amm", "LINK sell: 장마감")
            
            btg = get_balance("BTG")
            current_price_btg = get_current_price("KRW-BTG")
            time.sleep(0.5)
            if btg*current_price_btg > 5000:
                sell_result = upbit.sell_market_order("KRW-BTG", btg*0.9995)
                post_message(myToken,"#amm", "BTG sell: 장마감")

            bch = get_balance("BCH")
            current_price_bch = get_current_price("KRW-BCH")
            time.sleep(0.5)
            if bch*current_price_bch > 5000:
                sell_result = upbit.sell_market_order("KRW-BCH", bch*0.9995)
                post_message(myToken,"#amm", "BCH sell: 장마감")

            neo = get_balance("NEO")
            current_price_neo = get_current_price("KRW-NEO")
            time.sleep(0.5)
            if neo*current_price_neo > 5000:
                sell_result = upbit.sell_market_order("KRW-NEO", neo*0.9995)
                post_message(myToken,"#amm", "NEO sell: 장마감")

        time.sleep(1)

    #에러메세지 출력
    except Exception as e:
        print(e)
        post_message(myToken,"#amm", e)
        time.sleep(1)