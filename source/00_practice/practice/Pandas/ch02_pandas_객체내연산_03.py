import pandas as pd
import numpy as np

# 차이[백분율] pct_change

# DataFrame.pct_change(periods=1, fill_method='pad', limit=None, freq=None, kwargs)

# pct_change는 한 객체 내에서 행과 행의 차이를 현재값의 백분율로 출력하는 메서드
#즉, (다음행-현재행)/현재행 의미.
'''
기본 사용법
df.pct_change(periods=1, fill_method='pad', limit=None, freq=None, kwargs)
periods : 비교할 간격을 지정합니다. 기본은 +1로 바로 이전 값과 비교합니다.
fill_method : {ffill : 앞의 값으로 채움 / bfill : 뒤의 값으로 채움} 결측치를 대체할 값입니다.
limit : 결측값을 몇개나 대체할지 정할 수 있습니다.
freq : 시계열 API에서 사용할 증분을 지정합니다. (예: 'M' 또는 BDay( ))
'''

# 예시
a = [1,1,4,4,1,1]
b = [1,2,4,8,16,32]
c = [1,np.nan,np.nan,np.nan,16,64]
data = {"col1":a,"col2":b,"col3":c}
df = pd.DataFrame(data)
print(df)

print(df.pct_change())
#   col1  col2  col3
# 0  NaN   NaN   NaN # 첫행은 이전행이 없으므로 NaN출력
# 1  0.00  1.0   0.0 # col1의 경우 이전행과 값이 같으므로 (1-1)/1 = 0 출력
# 2  3.00  1.0   0.0 # col2의 경우 2배씩 커지므로 차이는 자기자신 즉 결과=1
# 3  0.00  1.0   0.0 # col3의 경우 결측치가 위의 값 기준으로 됨. (1-1)/1=0
# 4  -0.75 1.0   15.0 # NaN = 1 보정 / [4][col3] = 16(4,col3)-1(3,col3)/1(3,col3)
# 5  0.00  1.0   3.0

# periods 인수 : 계산할 간격으로 기본값이 1(현행,다음행 비교)
# periods = 2 , -1
print(df.pct_change(periods=2))
print(df.pct_change(periods=-1))

# fill_method / limit 인수 사용
# fill_method 인수는 결측치를 대체할 값을 지정 가능
# fill_method = 'ffill' 의 경우 기본값으로 바로 윗값으로 결측치를 대체
# fill_method = 'bfill' 의 경우 바로 아랫값으로 결측치를 대체

print(df.pct_change(fill_method='bfill'))

# limit 인수는 결측치를 몇 개까지 대체할 지 지정
print(df.pct_change(limit=2))
'''
        col1  col2  col3
    0   NaN   NaN   NaN
    1  0.00   1.0   0.0 # 1번째 결측치 ffill = 1
    2  3.00   1.0   0.0 # 2번째 결측치까지는 'ffill'에따라 1로 채워집니다. 
    3  0.00   1.0   NaN # 3번째 결측치는 limit=2이므로 NaN 그대로 둡니다.
    4 -0.75   1.0   NaN 
    5  0.00   1.0   3.0
'''

# 누적계산 expending
# DataFrame.expanding(min_periods=1, center=None, axis=0, method='single')

# expanding 메서드는 행이나 열의 값에 대해 누적으로 연산을 수행하는 메서드.
# df.expanding().sum() 처럼 추가 메서드를 이용하여 연산을 수행.

'''
기본 사용법
※ 자세한 내용은 아래 예시를 참고 바랍니다.
df.expanding(min_periods=1, center=None, axis=0, method='single').추가메서드()
min_periods : 연산을 수행할 요소의 최소 갯수입니다. 이보다 작으면 NaN을 출력합니다.
center : 미사용
axis : 누적 연산을 수행할 축을 지정합니다.
method : {single / table} 연산을 한 줄씩 수행할지 아니면 전체 테이블에 대해서 롤링을 수행할지 여부입니다.
기본값은 'single'로 한 줄씩 연산을 수행합니다. 'table'을 사용하기 위해서는 numba 라이브러리가 설치되어있어야 하며,
추가 연산 메서드에서 engine=numba로 설정해주어야 합니다.
'''

# 예제
import numba

data = {'col1':[1,2,3,4],'col2':[3,7,5,6]}
idx = ['row1','row2','row3','row4']
df = pd.DataFrame(data = data, index = idx)
print(df)

print(df.expanding().sum()) #열마다 누적으로 sum을 진행

# min_periods 지정 시
print(df.expanding(min_periods=2).sum()) # 입력값 만큼의 개수가 충족되지 않는 값은 NaN 반환

# axis = 1
print(df.expanding(axis=1).sum()) # 열 기준으로 누적값 계산 -> 방향

# method = 'table' 입력 시 numba 라이브러리를 이용해 연산을 테이블 단위로 롤링
# 추가 연산 메서드에 인수로 engine='numba' 지정

# 파이썬은 인터프리티 언어라서 C/C++등과 같은 언어에 비해 느립니다.
# Numba는 파이썬 코드를 LLVM컴파일러를 이용해 머신코드로 바꾸어 수치연산을 가속해주는 라이브러리입니다.
print(df.expanding(method='table').sum(engine='numba')) 
'''
        col1  col2
    row1   1.0   3.0 # 연산의 결과는 singe때와 동일하지만 대량의 데이터 연산에는 빠른 속도를 지원함.
    row2   3.0  10.0
    row3   6.0  15.0
    row4  10.0  21.0
'''