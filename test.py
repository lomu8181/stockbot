
import pandas as pd

# 데이터프레임 생성
data = {'Name': ['Tom', 'Nick', 'John', 'Amy', 'Bob', 'Cindy', 'David', 'Eva', 'Frank', 'Grace', 'Henry'],
        'Age': [20, 21, 19, 22, 23, 24, 25, 26, 27, 28, 29]}
df = pd.DataFrame(data)
print(df)
print(df.iloc[0])
print('#########################################################################################')


# 행의 순서를 거꾸로 바꿈
df = df.iloc[::-1]
print(df)
print(df.iloc[0])

print(tk_ALL.index(value), len(tk_ALL),f'({value})')