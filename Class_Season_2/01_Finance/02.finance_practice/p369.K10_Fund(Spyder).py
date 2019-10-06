import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

# 그래프에서 한글 사용 세팅
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False

plt.rcParams['figure.figsize'] = (10, 5)
plt.rcParams['grid.linestyle'] = '--'
plt.rcParams['grid.alpha'] = 0.7
plt.rcParams['lines.antialiased'] = True

k10_info = pd.read_csv('./stockData/siga.csv')[:10]
k10_info

k10_historical_price = pd.read_csv('./stockData/k10StockPrice.csv', index_col=0, parse_dates=True)
k10_historical_price.head()

k10_historical_mc = pd.read_csv('./stockData/k10SigaPrice.csv', index_col=0, parse_dates=True)
k10_historical_mc.head()

K10 = pd.read_csv('./stockData/k10_kp200.csv', index_col=0, parse_dates=True)
K10.head()

CU = 50000     # 설정/환매 단위
base_date = dt.date(2016, 11, 10)     # 설정 기준일
volume = 1000000     # 최초 설정수량
interest_rate = 0.02     # 이자율

def creation_redemption(v):
    creation = np.random.randint(0, 5) * CU
    if v>500000:
        redemption = np.random.randint(0, 5) * CU
    else:
        redemption = 0
    volume = v + creation - redemption
    return(creation, redemption, volume)
    
# 보유비중 산정
k10_stock_ratio = pd.DataFrame()
for s in k10_info.code:
    k10_stock_ratio[s] = k10_historical_mc[s] / k10_historical_mc.sum(axis=1)

k10_stock_ratio.head()

Fund_NAV = pd.DataFrame()
Fund_Chg = pd.DataFrame()

for d in k10_historical_price.index:
    
    # 포트폴리오 구성용 정보 (당일 주가 / 자산비중)
    stock_price = np.array(k10_historical_price.loc[d])
    stock_weight = np.array(k10_stock_ratio.loc[d])
    
    # 기존 주식 포트폴리오 NAV 계산
    if (d.date() <= base_date):     # 기준일 이전
        # 최초 주식 포트폴리오 (보유량 0)
        stock_holdings = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        NAV_cash = 0     # 최초 현금 보유량
    else:     # 기준일 이후
        NAV_stock = sum(stock_holdings * stock_price)     # 주식 잔고
        NAV = NAV_stock + NAV_cash     # 전체 잔고
        
    # 기준가격 산정
    if (d.date() <= base_date):
        # 최초 기준가를 10,000원으로 설정함
        price = 10000
    else:
        price = NAV / volume
        
    # 신규 펀드 설정/환매 좌수 계산
    if (d.date() == base_date):
        volume = 0     # 펀드 좌수.
        volume_chg = 1000000     # 첫날 설정액. 첫날 이만큼 들어옴.
    else:
        vol = creation_redemption(volume)     # 설정/환매 함수 호출
        volume_chg = vol[0] - vol[1]     # 좌수 변동 
        
    # 총 펀드 좌수에 반영
    volume = volume + volume_chg
    
    # 펀드의 총 가치의 증감 (기준가 * 증감된 좌수)
    # AUM = 설정 좌수 * 기준가
    aum_chg = price * volume_chg
    
    # 신규 주식 거래량 계산. AUM 변화분만큼 주식을 매입함
    stock_trade = np.floor( aum_chg * stock_weight / stock_price)
    
    # 주식 매매금액 (매매수량 * 주가)
    trade_amt = np.sum(stock_trade * stock_price)
    
    # 현금 잔고 변동 
    cash_chg = aum_chg - trade_amt
    
    # 총 주식 보유량 = 기 보유량 + 신규 거래량
    stock_holdings = stock_holdings + stock_trade
    
    # 현금 보유량 증가 (이자율 반영)
    cash_holdings = np.floor( NAV_cash * np.exp(interest_rate/365) ) 

    # NAV 업데이트
    NAV_stock = sum(stock_holdings * stock_price)     # 주식 잔고
    NAV_cash = cash_holdings + cash_chg     # 현금 잔고
    NAV = NAV_stock + NAV_cash     # 전체 잔고

    date = pd.Series(d)
    
    # Fund NAV 정보를 DataFrame에 저장
    NAV_tmp = {'Stock' : NAV_stock, 'Cash' : NAV_cash, 'Total' : NAV, 'Price' : price}
    tmp = pd.DataFrame(NAV_tmp, index=date)
    Fund_NAV = Fund_NAV.append(tmp)
    
    # 일자별 설정&환매 좌수 정보를 DataFrame에 저장
    Chg_tmp = {'Amount Change' : aum_chg, 'Trade Amount' : trade_amt, 'Cash Change' : cash_chg}
    tmp = pd.DataFrame(Chg_tmp, index=date)
    Fund_Chg = Fund_Chg.append(tmp)

# 펀드 수익률 vs 지수 수익률
Earnings = pd.DataFrame()
Earnings['K10'] = ( K10['K10'] - K10['K10'][base_date] ) / K10['K10'][base_date] * 100
Earnings['KOSPI200'] = ( K10['kpi200'] - K10['kpi200'][base_date] ) / K10['kpi200'][base_date] * 100
Earnings['Fund'] = ( Fund_NAV['Price'] - Fund_NAV['Price'][base_date] )/ Fund_NAV['Price'][base_date] * 100

ax = Earnings.plot(color = ['orange', 'blue', 'red'])
ax.legend(loc=0)
ax.set_ylabel('(누적 수익률, %)')
ax.grid(True)

