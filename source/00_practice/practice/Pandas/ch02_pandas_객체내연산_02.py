import pandas as pd
import numpy as np

# 전치 transpose, T

# DataFrame.transpose(args, copy=False)
# DataFrame.T(args, copy=False)

# T = transpose
# (n,m) DataFrame => (0,0) -> (n,m) 을 연결하는 대각선을 중심으로 뒤집는 것
# 행렬 전환

'''
기본 사용법
df.transpose(args, copy=False)
copy : 사본을 반환할지 여부입니다. 여러 dtype으로 이루어진 경우 자동으로 True가 됩니다.
'''

col = ['col1','col2','col3']
row = ['row1','row2','row3','row4']
data = [['A',1,2],['B',3,4],['C',5,6],['D',7,8]]
df = pd.DataFrame(data=data,index=row,columns=col)
print(df)

print(df.transpose())
print(df.T)

# 순위 rank

# DataFrame.rank(axis=0, method='average', numeric_only=None, na_option='keep', ascending=True, pct=False)
# 축에 대해서 순위를 매기는 메서드. 동일 순위일 경우 평균을 반환

'''
기본 사용법
df.rank(axis=0, method='average', numeric_only=None, na_option='keep', ascending=True, pct=False)
axis : {0 : index / 1 : columns} 순위를 매길 레이블입니다.
method : {'average' / 'min' / 'max' / 'first' / 'dense'} 동순위 일때 처리 방법입니다.
average는 평균, min은 낮은순위, max는 높은순위, first는 나타나는순서대로
dense의 경우는 min과 같지만 그룹간 순위는 항상 1씩 증가합니다.
numeric_only : {True / False} 숫자만 순위를 매길지 여부 입니다.
na_option : {'keep' / 'top' / 'bottom'} NaN값의 처리 방법입니다.
keep의 경우 NaN순위 할당, top의 경우 낮은순위 할당, bottom의 경우 높은 순위를 할당합니다.
ascending : {True / False} 오름차순으로 할지의 여부 입니다.
pct : {True / False} 순위를 백분위수형식으로 할지 여부입니다.
'''

# 먼저, pd.NA가 포함된 간단한 9x1 객체를 하나 생성
# 같은 수의 경우 보기 쉽도록 인덱스에 기호(★, ☆)
data = [[5],[5],[pd.NA],[3],[-3.1],[5],[0.4],[6.7],[3]]
row = ['A★','B★','C','D☆','E','F★','G','H','I☆']
df = pd.DataFrame(data=data, index=row, columns=['val'])
print(df)

df['avg'] = df['val'].rank(method='average') # 3.5등을 반환
df['min'] = df['val'].rank(method='min') # 5,6,7등이 동점이면 5등 반환
df['max'] = df['val'].rank(method='max') # 5,6,7등이 동점이면 7등 반환
df['first'] = df['val'].rank(method='first') # 동점일 경우 위에서부터 순위 매김
df['dense'] = df['val'].rank(method='dense') # 공동 2등 공동 3등...
print(df)

# na_option에 따라 Na가 포함된 경우 순위가 어떻게 매겨지는 지 확인 가능
# pct 추가

df['keep'] = df['val'].rank(na_option='keep') # Na -> NaN부여, 그대로 활용
df['top'] = df['val'].rank(na_option='top') # Na에 가장 높은 순위 부여
df['bottom'] = df['val'].rank(na_option='bottom') # Na에 가장 낮은 순위 부여
df['pct'] = df['val'].rank(pct=True) # True일 경우 백분위 수로 표시(상위 @@% 형식)
print(df)

# 차이 이산 diff
# DataFrame.diff(periods = 1, axis = 0)
# diff : 한 객체 내에서 열과 열/행의 차이를 출력하는 메서드

a = [1,2,3,4,5,6,7,8]
b = [1,2,4,8,16,32,64,128]
c = [8,7,6,5,4,3,2,1]
data = {"col1":a,"col2":b,"col3":c}
df = pd.DataFrame(data=data)
print(df)

# 기본적인 사용법
# axis에 따라서 행끼리 비교할지 열 끼리 비교할지 설정 가능
# axis = 0인 경우 행 - 바로 전 행 의 값을 출력. 비교할 값이 없으면 NaN출력 0행 : NaN // 1행 : 1행 - 0 행
print(df.diff(axis=0))

# axis = 1일 경우 열 - 바로 전 열 값 출력, 비교값 없으면  NaN
print(df.diff(axis=1)) # 1열 : 1열 - 0열(NaN) = NaN, 2열 : 2열 - 1열, 3열 : 3열 -2열

# periods 사용
# periods의 경우 기본값은 +1로 +1인 경우 바로 이전 값과의 차를 출력
# +3의 경우 3칸 이전 값과 비교하고 -2인 경우 +2인 경우의 값과 비교
print(df.diff(periods=3)) # 0,1,2행의 경우 -3,-2,-1의 행이 없어서 NaN, 3행의 경우 0행을 뺀 값
print(df.diff(periods=-2)) # 6,7행의 경우 8,9의 행이 없어서 NaN, 5행의 경우 (5+2)행을 뺀 값