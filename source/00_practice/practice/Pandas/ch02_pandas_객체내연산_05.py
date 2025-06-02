import pandas as pd
import numpy as np
import numba

# 그룹화 계산 groupby

# DataFrame.groupby(by=None, axis=0, 
# level=None, as_index=True, sort=True, group_keys=True, 
# squeeze=NoDefault.no_default, observed=False, dropna=True)

# 데이터를 그룹화하여 연산을 수행하는 메서드

'''
by : 그룹화할 내용입니다. 함수, 축, 리스트 등등이 올 수 있습니다.

axis : 그룹화를 적용할 축입니다.

level : 멀티 인덱스의 경우 레벨을 지정할 수 있습니다.

as_index : 그룹화할 내용을 인덱스로 할지 여부입니다.
False이면 기존 인덱스가 유지됩니다.

sort : 그룹키를 정렬할지 여부입니다.

group_keys : apply메서드 사용시 결과에따라 
그룹화 대상인 열이 인덱스와 중복(group key)이 될 수 있습니다. 
이 때, group_keys=False로 인덱스를 기본값으로 지정할 수 있습니다.

squeeze : 결과가 1행 or 1열짜리 데이터일 경우 Series로, 
1행&1열 짜리 데이터일 경우 스칼라로 출력합니다.

observed : Categorical로 그룹화 할 경우 
Categorical 그룹퍼에 의해 관찰된 값만 표시할 지 여부입니다.

dropna : 결측값을 계산에서 제외할지 여부입니다.
'''

# 예시

idx=['A','A','B','B','B','C','C','C','D','D','D','D','E','E','E']
col=['col1','col2','col3']
data = np.random.randint(0,9,(15,3))
df = pd.DataFrame(data=data,index=idx,columns=col).reset_index()
print(df)
'''
reset_index()란?
DataFrame은 "행 인덱스(index)"를 가지고 있어. (row1, row2, row3 같은 거)
reset_index()는
현재 인덱스를 일반 컬럼으로 빼고
인덱스 번호를 0, 1, 2, 3... 이런 기본 숫자 인덱스로 다시 설정해주는 함수야.
reset_index(drop=True)를 주면, 기존 인덱스를 버리고 아예 없애버릴 수도 있어.
'''

# 추가 메서드 없이 groupby 메서드를 실행하면 DataFrameGroupBy 오브젝트가 생성
print(df.groupby('index'))
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000024E739CB380>
# 여기에 추가 연산 메서드를 입력하면 그룹화 된 열의 데이터에 대한 연산이 수행
print(df.groupby('index').mean())
'''      col1      col2      col3
index                              
A      2.000000  1.500000  2.500000
B      4.000000  4.666667  4.000000
C      4.333333  3.333333  5.000000
D      2.500000  2.250000  3.000000
E      5.000000  4.333333  3.666667
'''

# 추가 메서드로는 단순 연산 뿐 아니라 agg, apply 등이 가능
print(df.groupby('index').count()) 
# col1, col2, col3 모두 같은 값 : index에서 개수를 세고 모든 col의 값에 대입했기 때문

#agg메서드를 이용해 여러 연산을 수행할 경우 MultiColumns 형태로 출력
print(df.groupby('index').agg(['sum','mean']))
'''       col1            col2           col3
        sum    mean    sum    mean    sum    mean
index
A       13  6.500000    9  4.500000    6  3.000000
B       14  4.666667   15  5.000000   10  3.333333
C       12  4.000000   16  5.333333   21  7.000000
D       18  4.500000   21  5.250000   25  6.250000
E       13  4.333333   11  3.666667   10  3.333333
'''

# group_key 인수 사용 : apply 메서드를 이용해 groupby 연산을 수행할 경우
# groupkey가 설정되기 때문에 때에 따라 컬럼과 인덱스가 중복 될 수 있다.
# 이 때 group_keys = False를 통해 기본 인덱스로 출력이 가능하다.
def top(df,n=2,col='col1') :
    return df.sort_values(by=col)[-n:] # 상위 n개의 열을 반환하는 함수 top

print(df.groupby('index').apply(top))
'''
            index  col1  col2  col3 # 인덱스와  index열이 중복
index
A       1      A     5     5     6
        0      A     7     7     5
B       3      B     4     5     6
        4      B     5     8     7
C       5      C     4     1     4
        7      C     5     6     7
D       8      D     7     3     6
        10     D     7     4     2
'''

print(df.groupby('index',group_keys=False).apply(top)) # 중복 제거
'''
    index  col1  col2  col3
0      A     0     1     2
1      A     2     1     7
4      B     5     1     2
2      B     6     0     1
6      C     4     0     8
5      C     7     6     1
8      D     7     1     8
9      D     8     5     3
12     E     7     7     4
13     E     7     3     2
'''

# observed 인수 사용
# categorical 객체를 생성할 때 그룹화(groupby)할 열에 있는 값이 아닌 값을
# 포함하게 되면 그룹화 할 때 해당 값을 표시할 지 여부를 선택 가능

df_cat = pd.Categorical(df['index'],categories=['A','B','C','D','E','F'])
# df의 index열에 대해서 A,B,C,D,E,F로 Categorical을 하여 df_cat 생성
print(df_cat)

# 위 categorical 객체에 대하여 col1열을 groupby 하면 
# 아래와 같이 카테고리에만 존재하는 F에 대한  groupby 값이 출력된다
print(df['col1'].groupby(df_cat).count())
'''  print(df['col1'].groupby(df_cat).count())
A    2
B    3
C    3
D    4
E    3
F    0 
# 인덱스 열에는 F열이 없으나 F열까지 Categorical 객체가 생성. 
# observed = False인 경우 카테고리 전체 출력
'''

# if observed = True :
print(df['col1'].groupby(df_cat,observed=True).count())
'''
A    2
B    3
C    3
D    4
E    3
Name: col1, dtype: int64
'''

# as_index 인수 사용
# 특정 열을 지정하여 groupby 할 경우 해당 열이 인덱스가 되는데
# as_index=False로 하여 기존 인덱스의 유지가 가능하다.
print(df.groupby(['index'],as_index=True).sum())
'''       col1  col2  col3
index
A         9     6     7
B        15    14     8
C         2     4     6
D        24    11    13
E        12    19    11
'''
print(df.groupby(['index'],as_index=False).sum())
'''  index  col1  col2  col3
0     A     5     8     4
1     B     9    13    11
2     C    19    10    15
3     D    28    13    15
4     E     7    14    12
'''

# dropna 인수 : 결측값을 그룹화에서 제외할지 여부 결정
# df index열의 6번행을 결측치 변경
df.loc[6, 'index'] = np.nan
print(df)
'''  index  col1  col2  col3
0      A     4     8     8
1      A     5     3     2
2      B     6     4     8
3      B     6     1     5
4      B     4     8     4
5      C     2     0     5
6    NaN     8     2     3
7      C     8     6     2
8      D     1     1     3
9      D     8     2     5
10     D     7     7     7
11     D     1     8     5
12     E     0     6     7
13     E     0     4     2
14     E     0     0     3
'''
# 일반적으로 nan은 계산에서 제외되어 인덱스에 표시되지 않은 것을 확인 가능
print(df.groupby('index').sum())
'''       col1  col2  col3
index
A         2     6     8
B        13    12    10
C         7     8     6
D        16    15    16
E        10    11    12
'''
# dropna = False의 경우 NaN 확인 가능
print(df.groupby('index', dropna=False).sum())
'''       col1  col2  col3
index
A        10     6     7
B        14     8    17
C        11     6     8
D        17    21    14
E        20    12    11
NaN       7     1     8 # NaN 확인 가능
'''

# level 인수의 사용 Multi Index
# Multi Index의 경우 level을 숫자나 str 형태로 지정해주어 groupby를 실행
idx = [['idx1','idx1','idx2','idx2','idx2'],['row1','row2','row1','row2','row3']]
col = ['col1','col2','col2']
data = np.random.randint(0,9,(5,3))
df = pd.DataFrame(data=data, index = idx, columns = col).rename_axis(index=['lv0','lv1'])
print(df)
'''           col1  col2  col2
lv0  lv1
idx1 row1     5     3     2
     row2     4     3     0
idx2 row1     7     6     7
     row2     8     4     3
     row3     6     6     6''' 
     
# level 을 int로 지정
print(df.groupby(level=1).sum())
'''      col1  col2  col2
lv1
row1    10    13     6
row2     5     7     2
row3     3     1     2'''

# level을 str 지정
print(df.groupby(['lv1','lv0']).sum())