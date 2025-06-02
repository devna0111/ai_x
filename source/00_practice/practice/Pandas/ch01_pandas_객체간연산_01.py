import pandas as pd

# pandas는 데이터 전처리에 용이한 DataFrame 구조를 지원한다.
# tensor, array 구조와 동일한 모습을 보임

# ch01-객체간 연산 : 사칙연산

# 사칙연산도 작동하지만 가장 큰 차이점은 fill_value 인수를 통해 계산 불가한 값을 채워넣는다는 것것
# 더하기 add
data = [[1,10,100],[2,20,200],[3,30,300]]
col = ['col1', 'col2', 'col3']
row = ['row1', 'row2', 'row3']
df = pd.DataFrame(data=data,index=row,columns=col)
# print(df)

result = df.add(1)
result2 = df + 1

data2 = [[3,],[4,],[5,]];
df2 = pd.DataFrame(data=data2,index=['row1','row2','row3'],columns=['col1'])
# print(df2)

# result = df.add(df2)
# print(result)

result = df.add(df2,fill_value=0)
# print(result)

# 빼기 sub
data = [[1,10,100],[2,20,200],[3,30,300]]
col = ['col1', 'col2', 'col3']
row = ['row1', 'row2', 'row3']
df = pd.DataFrame(data=data,index=row,columns=col)
# print(df)

# result = df.sub(1)
result = df - 1
# print(result)

data2 = [[3,],[4,],[5,]];
df2 = pd.DataFrame(data=data2,index=['row1','row2','row3'],columns=['col1'])
# print(df2)

# result = df.sub(df2)
result = df.sub(df2, fill_value=0)
# print(result)

# 곱셈 mul
data = [[1,10,100],[2,20,200],[3,30,300]]
col = ['col1', 'col2', 'col3']
row = ['row1', 'row2', 'row3']
df = pd.DataFrame(data=data,index=row,columns=col)

# print(df*2)
# print(df.mul(2))

data2 = [[3,],[4,],[5,]];
df2 = pd.DataFrame(data=data2,index=['row1','row2','row3'],columns=['col1'])

# print(df.mul(df2))
# print(df.mul(df2,fill_value=0))

# 나눗셈 div : div/0 에러 대신 inf 값 반환하니 주읜읜

# print(df.div(2))
# print(df/(2))

# print(df.div(df2))
# print(df.div(df2,fill_value=1))
