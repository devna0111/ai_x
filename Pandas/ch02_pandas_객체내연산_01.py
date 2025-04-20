# pandas 객체 내 연산
import pandas as pd
import numpy as np

# 반올림(round)
# DataFrame.round(decimals=0, args, kwargs)
# DataFrame 객체 내의 요소를 반올림하는 메서드

# df.round(decimals=0, args, kwargs) decimals : 
# 소수 n번째 자리 '까지' 반올림을 합니다.
# 만약 음수면 10의 n승 자리 까지 반올림 합니다.

# 예시 : numpy의 random 메서드를 이용하여 3*3 난수 객체 하나 생성
col = ['col1','col2','col3']
row = ['row1','row2','row3']
data = np.random.rand(3,3) * 100
df = pd.DataFrame(data=data,index=row,columns=col)
print(df)

# decimals = 0 : 일의 자리 까지 반올림
print(df.round(decimals=0))

# decimals = n > 0 : 양수인 경우 소수 n번째 자리 까지 반올림
print(df.round(1))
print(df.round(2))

# decimals = n < 0 : 음수의 경우 10의 n승까지 반올림
print(df.round(-1))

# 합계 sum 
# DataFrame.sum(axis=None, skipna=None, level=None, numeric_only=None, min_count=0, kwargs)
# 객체의 행이나 열의 총 합계를 구하는 메서드
'''
기본 사용법
df.sum(axis=None, skipna=None, level=None, numeric_only=None, min_count=0, kwargs)
axis : { 0 : 행 / 1 : 열} 더할 레이블을 선택합니다.
skipna : {True or False} Na가 존재할 경우 무시할지의 여부입니다. 기본값은 True입니다.
level : Multi Index일 경우 레벨을 설정합니다.
numeric_only : 숫자 데이터만 사용할지의 여부 입니다.
min_count : 계산에 필요한 숫자의 최소 갯수입니다
'''
# Nan이 포함된 3*3객체 생성 : np.nan 변수 활용
col = ['col1','col2','col3']
row = ['row1','row2','row3']
data = [[1,2,3],[4,5,6],[7,np.nan,9]]
df = pd.DataFrame(data=data,index=row,columns=col)
print(df)

# axis를 설정하여 더하기 수행 : 0 = 열의 합 // 1 = 행의 합
print(df.sum(axis=0))
print(df.sum(axis=1))

# 위의 경우 NaN 결측치를 무시하고 합산하였으나 skipna = False 수행 시 NaN 반환
print(df.sum(axis=1,skipna=False))

# min_count를 변경하여 계산
# min_count는 계산에 필요한 숫자의 최소갯수를 의미
# min_count = 3 이라면 NaN을 포함하는 행의 경우 숫자가 2개로
# skipna = True 여도 NaN을 출력
print(df.sum(axis=1,min_count=3))

# 곱 prod, product
# DataFrame.prod(axis=None, skipna=None, level=None, numeric_only=None, min_count=0, kwargs)
# DataFrame.product(axis=None, skipna=None, level=None, numeric_only=None, min_count=0, kwargs)

# prod = product 행이나 열의 곱을 구하는 메서드

'''
기본 사용법
df.prod(axis=None, skipna=None, level=None, numeric_only=None, min_count=0, kwargs)
axis : { 0 : 행 / 1 : 열} 곱할 레이블을 선택합니다.
skipna : {True or False} Na가 존재할 경우 무시할지의 여부입니다. 기본값은 True입니다.
level : Multi Index일 경우 레벨을 설정합니다.
numeric_only : 숫자 데이터만 사용할지의 여부 입니다.
min_count : 계산에 필요한 숫자의 최소 갯수입니다.
'''

# Nan이 포함된 3*3객체 생성 : np.nan 변수 활용
col = ['col1','col2','col3']
row = ['row1','row2','row3']
data = [[1,2,3],[4,5,6],[7,np.nan,9]]
df = pd.DataFrame(data=data,index=row,columns=col)
print(df)

# 행/열의 설정만 진행 후 계산하면 NaN 무시(skipna=True 기본)
print(df.prod(axis=0))
print(df.prod(axis=1))

# skipna = False 라면 NaN이 포함된 행열의 계산은 NaN 반환
print(df.prod(axis=0,skipna=False))
print(df.prod(axis=1,skipna=False))

# min_count : NaN을 제외 실제 값이 min_count개 미만이면 NaN 반환환
print(df.prod(axis=0,min_count=3))
print(df.prod(axis=1,min_count=3))

# 절대값 abs()

# DataFrame.abs()

'''
기본 사용법
df.abs( )
숫자의 경우 절댓값을 반환하며, 복소수의 경우 복소수의 크기가 반환됩니다.
※ 복소수가 a+bj인 경우 복소수의크기 (a**2+b**2)**0.5
NaN의 경우는 NaN을 그대로 출력합니다.
'''

data = [[-1,2,-3.5],[4,-5.5,3+4j],[7,np.nan,0]]
df = pd.DataFrame(data=data,index=row,columns=col)
print(df)

print(df.abs())