# 유닉스 시간을 datetime으로 변환
import datetime
# timestamp => 유닉스시간을 의미
now_currentSec = datetime.datetime.now().timestamp() # 현재의 유닉스 시간(70. 1. 1. 부터 현재까지의 밀리세컨드)
print(now_currentSec)
# 유닉스 시간 -> 변환
now_current = datetime.datetime.fromtimestamp(now_currentSec) # 현재의 시간
print(now_current)
# 변환 시간 형식 변경
now_time = now_current.strftime('%Y-%m-%d %H:%M:%S') # 시간 형식을 변경
print(now_time)