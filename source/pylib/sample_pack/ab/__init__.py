# 패키지로서 import 하기 위해 필요한 파일 : 패키지 임을 알려주는 파일일
'''
sample_pack/ab/__init__.py
from sample_pack.ab import 함수|클래스|변수
from sample_pack.ab import * : 수행할 경우 자동 import될 모듈 지정할 수 있음(__all__)

sample_pack/ab/a.py
sample_pack/ab/b.py
'''

__all__ = ['a'] # import * 시 사용할 함수 초기 설정 

print('sample_pack 안의 ab 패키지를 load 했습니다.')