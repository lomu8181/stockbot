import pandas as pd

# 데이터프레임 생성
data = {'Name': ['Tom', 'Nick', 'John'],
        'Age': [20, 21, 19]}
df = pd.DataFrame(data)

print(df)

# 새로운 열 추가
df['Height'] = [170, 175, 180]

print(df)