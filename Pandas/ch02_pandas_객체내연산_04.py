import pandas as pd
import numpy as np
import numba

# 8. 기간이동 계산 rolling
# DataFrame.rolling
# (window, min_periods=None, center=False, win_type=None, 
# on=None, axis=0, closed=None, method='single')

# rolling 메서드는 현재 열에 대하여 일정크기의 창(window)를 이용하여
# 그 window 안의 값을 추가 메서드를 통해 계산하는 메서드.

'''
기본 사용법
df.rolling(window, min_periods=None, center=False, win_type=None, on=None, axis=0, closed=None, method='single')
window : 계산할 창(window)의 크기 입니다. 
열 기준으로 계산할 경우 행의 수입니다.

min_periods : 계산할 최소 크기(기간) 입니다. 
window 안의 값의 수가 min_periods의 값보다 작을경우 NaN을 출력합니다.
기본적으로 window 크기와 동일합니다.

center : {True / False} 레이블을 window의 중간에 둘지 여부입니다. 
기본값은 False로 레이블이 창 우측에 위치합니다.

win_type : {'triang' / 'gaussian' / ...} 가중치를 넣어 계산할 경우 계산 방식 입니다. 
때에따라 연산 메서드에 추가 인수를 지정해야할수도 있습니다.

on : 시계열 인덱스나, 시계열과 유사한 열이 있을 경우 
이 열을 기준으로 rolling을 수행할 수 있습니다.

axis : 계산의 기준이 될 축입니다.

closed : {'left' / 'right' / 'both' / 'neither'} window가 닫히는 방향. 
자세한건 아래 예시 참고
method :{'single' / 'table'} 
numba 를 이용하여 테이블 계산을 진행하여 속도를 높힐지 여부입니다. 
현재 'single'만 사용가능합니다.
※ method 인수의 numba 사용은 02-09 누적계산(expending)에서 자세히 다루고 있습니다.
'''

# 예시
period = pd.period_range(start='2022-01-13 00:00:00',end='2022-01-13 02:30:00',freq='30T')
data = {'col1':[1,2,3,4,5,6],'col2':period}
idx = ['row1','row2','row3','row4','row5','row6']
df = pd.DataFrame(data= data, index = idx)
print(df)

# window의(<>비교영역역) 크기를 지정해주면 현재 행 이전으로 window 크기 만큼의 계산을 수행
print(df.rolling(window=3).sum(numeric_only=True)) # 뒤에 추가 메서드를 이용하여 연산을 지정해주어야합니다.
'''       col1
    row1   NaN # min_period의 크기는 지정하지 않을 경우 window크기와 동일해 Nan
    row2   NaN # 3개 인자 누적 합 불가
    row3   6.0 # 1행, 2행, 3행의 sum 값
    row4   9.0 # 2행, 3행, 4행의 sum 값
    row5  12.0 # 3행, 4행, 5행의 sum 값
    row6  15.0 # 4행, 5행, 6행의 sum 값
'''
# closed 인수의 사용 : 계산의 닫는 위치를 지정. 만약 6행을 기준으로 window = 3을 계산하면
# 아래와 같은 범위로 window 경계가 지정
'''
left : 3 ≤ x < 6
right : 3 < x ≤ 6
both : 3 ≤ x ≤ 6
neither : 3 < x < 6
'''
# closed='left'인 경우

print(df.rolling(window=3, closed='left').sum(numeric_only=True))
print(df.rolling(window=3, closed='right').sum(numeric_only=True))
print(df.rolling(window=3, closed='both').sum(numeric_only=True))
print(df.rolling(window=3, closed='neither').sum(numeric_only=True))
# neither의 경우 min_period보다 
# window의 크기가 작으므로(1만큼 작아짐(같거나 작다 연산이 없어지면서 1만큼 작아짐))
# 이럴 때는 min_period를 지정해주어야함.
print(df.rolling(window=3, closed='neither',min_periods=2).sum(numeric_only=True))

# center : 윈도우의 기준을 중앙값으로 한다.
'''
윈도우가 [row1, row2, row3] 이면
center=False: 결과를 row3에 씀
center=True : 결과를 row2에 씀 (중앙에)

윈도우가 [row2, row3, row4] 이면
center=False: row4에 씀
center=True : row3에 씀
'''
# 지금까지 window를 통해 period를 통제하면 마지막 값을 기준으로 작성했으나
# center를 이용하면 현재값을 기준으로 창이 형성됨.

print(df.rolling(window=3, center=True).sum(numeric_only=True))

# win_type 인수의 사용 : 가중치를 주며 계산이 가능하다
#삼각함수 가중치
print(df.rolling(window=3,win_type='triang').sum(numeric_only=True))
# 가우시안 분포 가중치
print(df.rolling(window=3,win_type='gaussian').sum(std = 3, numeric_only=True))

# on 인수의 사용 : on = 'col2' 를 이용해 
# col2열의 시계열 인덱스를 기준으로 rolling의 수행이 가능
print(df.rolling(window='60T', on ='col2').sum())
# 지금까지 col1을 기준으로 작동시켰다면 이번에는 col2의 시계열을 기준으로
# 00 ~ 60T 사이의 값을 누적합.
'''    col1      col2
row1   1.0  2022-01-13 00:00 # 그런데 특이점으로 NaN을 반환하지 않음
row2   3.0  2022-01-13 00:30 # 0030 - 60 = -0030 이지만 실제로는 00-0030의 합을 반환
row3   5.0  2022-01-13 01:00 # 0000<-0100 : 2 + 3
row4   7.0  2022-01-13 01:30 # 0030<-0130 : 3 + 4
row5   9.0  2022-01-13 02:00
row6  11.0  2022-01-13 02:30
'''