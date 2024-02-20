
import pandas as pd
import time
import json


today = time.strftime("%Y%m%d")

with open('data/TK/000020.json', 'r') as f:
    df = pd.DataFrame(json.load(f))

print(df)

df['1daymove'] = None

print(df)








'''
with open(' 폴더이름 / 파일이름.json', 'r') as f:  
    data = pd.DataFrame(json.load(f))

원하는 폴더의 파일을 불러와 f 변수이 넣음
f변수를 data라는 변수에 판다스 데이터 프레임 형식으로 집어넣음
'''







'''
# 행의 순서를 거꾸로 바꿈
df = df.iloc[::-1]
print(df)
print(df.iloc[0])
'''