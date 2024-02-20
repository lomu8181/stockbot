import time
import json
import os
from pykrx import stock
import pandas as pd
import FinanceDataReader as fdr

'''
fdr.DataReader('종목코드', '시작년도', '종료년도')
read price data (timeseries) from various exchanges or data source
    - symbol: 종목코드나 티커 (with exchange: 'KRX'(default), 'KRX-DETAIL', 'KRX-DELISTING', 'NAVER', 'YAHOO' ...)
    - start: datetime or str 
    - end: datetime or str
usage:
    - fdr.DataReader('KRX:KOSPI', '2020')
    - fdr.DataReader('ECOS:한국은행기준금리', '1990-01-01')

변수.head(갯수)
 : 앞에서부터 갯수만큼의 값을 받음

 변수.tail(갯수)
 : 뒤에서부터 갯수만큼의 값을 받음
'''


print('#########################################################################################')



today = time.strftime("%Y%m%d")

#당일 기준 코스피 코스닥의 상장된 종목 티커 수집
tk_KOSPI = stock.get_market_ticker_list(f"{today}")
tk_KOSDAQ = stock.get_market_ticker_list(f"{today}", market="KOSDAQ")
tk_ALL = tk_KOSPI + tk_KOSDAQ
print(len(tk_ALL))


#리스트를 json으로 저장
with open('data/TK_list.json', 'w') as f:
    json.dump(tk_ALL, f)


print('#########################################################################################')

for value in tk_ALL:
    stock_info = fdr.DataReader(value,'2022')
    stock_info = stock_info.iloc[::-1]
    stock_info.index = stock_info.index.strftime('%Y-%m-%d')  # 인덱스를 문자열로 변환
    with open(f'data/TK/{value}.json', 'w') as f:
        json.dump(stock_info.to_dict(), f)
    print(tk_ALL.index(value) + 1,'/', len(tk_ALL),f'({value})')


print('#########################################################################################')


'''




#krx 주식 목록에서 

df_code = df_KRX.iloc[-1]['Code']
print(df)
a = stock.get_market_ticker_list
# JSON 파일로 저장
df.to_json(f'data/{df_code}.json')
'''