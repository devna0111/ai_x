import pandas as pd
# 나머지 mod

# %연산과 동일하나 fill_value 인수를 통해 불가한 값을 채워넣는다.

data = [[1,2,3,],[4,5,6,],[7,8,9,]]
col = ['col1','col2','col3']
row = ['row1','row2','row3']

df = pd.DataFrame(data = data, index= row, columns= col)
print(df)

# print(df%7)
# print(df.mod(7))

data2 = [[2],[3],[5]]
df2 = pd.DataFrame(data = data2,index = ['row1','row2','row3'], columns=['col1'])

print(df%df2)
print(df.mod(df2,fill_value=1))

# 거듭제곱 pow
# ** 연산과 동일하나 fill_value 인수를 통해 불가한 값을 채워넣는다.

print(df**3)
print(df.pow(3))

df2 = pd.DataFrame(data = [[0],[3],[5]], index=['row1','row2','row3'], columns=['col1'])
print(df2)

print(df.pow(df2, fill_value= 0))

#  행렬 곱 dot : 수학적 의미에서의 행렬곱 

col = ['col1','col2']
row = ['row1','row2']
data1 = [[1,2],
         [3,4]]
data2 = [[5,6],
         [7,8]]
df1 = pd.DataFrame(data=data1)
df2 = pd.DataFrame(data=data2)

print(df1.dot(df2))